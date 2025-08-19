
CS_350_Module_07_Final_Project_Thermosat 


import board
import digitalio
import pwmio
import time
import sys
from datetime import datetime
import adafruit_character_lcd.character_lcd as character_lcd
import busio
import adafruit_ahtx0

# --- LCD Setup ---
lcd_columns = 16
lcd_rows = 2
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D5)
lcd_d7 = digitalio.DigitalInOut(board.D11)

lcd = character_lcd.Character_LCD_Mono(
    lcd_rs, lcd_en,
    lcd_d4, lcd_d5, lcd_d6, lcd_d7,
    lcd_columns, lcd_rows
)

# --- AHT20 Sensor Setup ---
i2c = busio.I2C(board.SCL, board.SDA)
aht20 = adafruit_ahtx0.AHTx0(i2c)

# Read room temperature once and treat it as hardcoded
room_temp = aht20.temperature * 9 / 5 + 32  # Convert °C to °F

# --- Button Setup ---
btn_state = digitalio.DigitalInOut(board.D21)
btn_up = digitalio.DigitalInOut(board.D22)
btn_down = digitalio.DigitalInOut(board.D27)

for btn in [btn_state, btn_up, btn_down]:
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

# --- LED Setup ---
red_led = pwmio.PWMOut(board.D18, frequency=5000, duty_cycle=0)
blue_led = pwmio.PWMOut(board.D24, frequency=5000, duty_cycle=0)

# --- Constants and Variables ---
set_point = 72.0  # Default set point
system_state = 0  # 0: OFF, 1: HEAT, 2: COOL
state_names = ["OFF", "HEAT", "COOL"]

prev_btn_state = True
prev_btn_up = True
prev_btn_down = True

lcd.clear()
lcd_show_temp = True
last_uart_time = time.monotonic()

# --- LED Control ---
def set_leds(heat, fade):
    if heat:
        if fade:
            for duty in list(range(0, 65535, 4096)) + list(range(65535, 0, -4096)):
                red_led.duty_cycle = duty
                blue_led.duty_cycle = 0
                time.sleep(0.005)
        else:
            red_led.duty_cycle = 65535
            blue_led.duty_cycle = 0
    else:
        if fade:
            for duty in list(range(0, 65535, 4096)) + list(range(65535, 0, -4096)):
                blue_led.duty_cycle = duty
                red_led.duty_cycle = 0
                time.sleep(0.005)
        else:
            blue_led.duty_cycle = 65535
            red_led.duty_cycle = 0

# --- Main Loop ---
try:
    while True:
        now = datetime.now()
        line1 = now.strftime("%b %d %H:%M:%S")[:16]

        # --- Button Logic ---
        if prev_btn_state and not btn_state.value:
            system_state = (system_state + 1) % 3  # Toggle state
        if prev_btn_up and not btn_up.value:
            room_temp += 1  # Simulate room temp increasing
        if prev_btn_down and not btn_down.value:
            room_temp -= 1  # Simulate room temp decreasing

        prev_btn_state = btn_state.value
        prev_btn_up = btn_up.value
        prev_btn_down = btn_down.value

        # --- LED Behavior ---
        if system_state == 1:  # HEAT
            if room_temp < set_point:
                set_leds(True, True)
            else:
                set_leds(True, False)
        elif system_state == 2:  # COOL
            if room_temp > set_point:
                set_leds(False, True)
            else:
                set_leds(False, False)
        else:  # OFF
            red_led.duty_cycle = 0
            blue_led.duty_cycle = 0

        # --- LCD Output ---
        if lcd_show_temp:
            line2 = f"T:{room_temp:.1f}F"
        else:
            line2 = f"{state_names[system_state]} {int(set_point)}F"
        lcd_show_temp = not lcd_show_temp

        lcd.cursor_position(0, 0)
        lcd.message = line1.ljust(16)
        lcd.cursor_position(0, 1)
        lcd.message = line2.ljust(16)

        # --- UART Logging ---
        if time.monotonic() - last_uart_time > 30:
            print(f"{state_names[system_state].lower()},{room_temp:.1f},{int(set_point)}")
            last_uart_time = time.monotonic()

        time.sleep(1)

except KeyboardInterrupt:
    red_led.duty_cycle = 0
    blue_led.duty_cycle = 0
    lcd.clear()
    lcd.message = "Goodbye!"
    time.sleep(1)
    lcd.clear()
