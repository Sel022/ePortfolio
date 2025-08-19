import time
from datetime import datetime
from config import *
from state import ThermostatState, Mode, STATE_NAMES
from sensor import AHT20Sensor
from io_hw import DebouncedButton, LedPairPWM
from display import Lcd16x2
from telemetry import Telemetry, uart_log

def fmt_clock(now: datetime) -> str:
    return now.strftime("%b %d %H:%M:%S")[:LCD_COLS]

def fmt_status_temp(temp_f: float) -> str:
    return f"T:{temp_f:.1f}F"

def fmt_status_mode(mode: Mode, setpoint_f: float) -> str:
    return f"{STATE_NAMES[int(mode)]} {int(setpoint_f)}F"

def main():
    # --- Init hardware services ---
    lcd = Lcd16x2(PIN_LCD_RS, PIN_LCD_EN, PIN_LCD_D4, PIN_LCD_D5, PIN_LCD_D6, PIN_LCD_D7, LCD_COLS, LCD_ROWS)
    leds = LedPairPWM(PIN_LED_RED, PIN_LED_BLUE)
    btn_mode = DebouncedButton(PIN_BTN_STATE)
    btn_up   = DebouncedButton(PIN_BTN_UP)
    btn_down = DebouncedButton(PIN_BTN_DOWN)
    sensor = AHT20Sensor()

    # --- App state ---
    tstat = ThermostatState(DEFAULT_SETPOINT_F, HYSTERESIS_F)
    show_temp = True

    # --- Telemetry (DB + UART) ---
    telem = Telemetry(MONGO_URI, MONGO_DB, MONGO_COLL)

    # --- Timers ---
    last_sensor = last_lcd = last_uart = last_db = 0.0
    temp_f = tstat.last_temp_f or DEFAULT_SETPOINT_F

    try:
        while True:
            now = time.monotonic()

            # Buttons (debounced)
            if btn_mode.pressed():
                tstat.cycle_mode()
            if btn_up.pressed():
                tstat.set_setpoint(tstat.setpoint_f + 1.0)
            if btn_down.pressed():
                tstat.set_setpoint(tstat.setpoint_f - 1.0)

            # Sensor read
            if now - last_sensor >= SENSOR_PERIOD_S:
                try:
                    temp_f = sensor.read_f()
                except Exception as e:
                    # If sensor temporarily fails, keep last reading
                    print(f"[SENSOR WARN] {e}")
                last_sensor = now

            # Control logic (hysteresis)
            heat_on, cool_on = tstat.apply(temp_f)

            # LEDs (visual feedback)
            if tstat.mode == Mode.HEAT:
                leds.set_heat(fade=heat_on)
                if not heat_on:
                    leds.off()
            elif tstat.mode == Mode.COOL:
                leds.set_cool(fade=cool_on)
                if not cool_on:
                    leds.off()
            else:
                leds.off()

            # LCD toggle between time and status
            if now - last_lcd >= LCD_TOGGLE_PERIOD_S:
                line1 = fmt_clock(datetime.now())
                line2 = fmt_status_temp(temp_f) if show_temp else fmt_status_mode(tstat.mode, tstat.setpoint_f)
                lcd.write_lines(line1, line2)
                show_temp = not show_temp
                last_lcd = now

            # UART logging
            if now - last_uart >= UART_PERIOD_S:
                uart_log(STATE_NAMES[int(tstat.mode)], temp_f, tstat.setpoint_f)
                last_uart = now

            # Database logging
            if now - last_db >= DB_PERIOD_S:
                telem.log(STATE_NAMES[int(tstat.mode)], temp_f, tstat.setpoint_f)
                last_db = now

            time.sleep(0.01)  # Cooperative yield

    except KeyboardInterrupt:
        pass
    finally:
        try:
            leds.off()
        except Exception:
            pass
        try:
            lcd.goodbye()
            time.sleep(1)
            lcd.clear()
        except Exception:
            pass

if __name__ == "__main__":
    main()

