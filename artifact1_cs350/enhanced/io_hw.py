import time
import board
import digitalio
import pwmio
from typing import Tuple

def _pin(name: str):
    # name like "D21" -> getattr(board, "D21")
    return getattr(board, name)

class DebouncedButton:
    def __init__(self, pin_name: str, pull_up=True, debounce_ms=50):
        self._pin = digitalio.DigitalInOut(_pin(pin_name))
        self._pin.direction = digitalio.Direction.INPUT
        self._pin.pull = digitalio.Pull.UP if pull_up else digitalio.Pull.DOWN
        self._last = self._pin.value
        self._last_change = time.monotonic()
        self._debounce = debounce_ms / 1000.0

    def pressed(self) -> bool:
        """Edge-detect press (high->low for pull-up)."""
        now = time.monotonic()
        val = self._pin.value
        if val != self._last and (now - self._last_change) >= self._debounce:
            self._last_change = now
            prev = self._last
            self._last = val
            # For pull-up buttons: falling edge means pressed
            if prev and not val:
                return True
        return False

class LedPairPWM:
    def __init__(self, red_pin: str, blue_pin: str):
        self.red = pwmio.PWMOut(_pin(red_pin), frequency=5000, duty_cycle=0)
        self.blue = pwmio.PWMOut(_pin(blue_pin), frequency=5000, duty_cycle=0)

    def set_heat(self, fade: bool):
        if fade:
            for duty in list(range(0, 65535, 4096)) + list(range(65535, 0, -4096)):
                self.red.duty_cycle = duty
                self.blue.duty_cycle = 0
                time.sleep(0.003)
        else:
            self.red.duty_cycle = 65535
            self.blue.duty_cycle = 0

    def set_cool(self, fade: bool):
        if fade:
            for duty in list(range(0, 65535, 4096)) + list(range(65535, 0, -4096)):
                self.blue.duty_cycle = duty
                self.red.duty_cycle = 0
                time.sleep(0.003)
        else:
            self.blue.duty_cycle = 65535
            self.red.duty_cycle = 0

    def off(self):
        self.red.duty_cycle = 0
        self.blue.duty_cycle = 0

    def cleanup(self):
        try:
            self.off()
        except Exception:
            pass

