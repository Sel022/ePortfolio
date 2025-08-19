from enum import IntEnum

class Mode(IntEnum):
    OFF  = 0
    HEAT = 1
    COOL = 2

STATE_NAMES = ["OFF", "HEAT", "COOL"]

class ThermostatState:
    def __init__(self, setpoint_f: float, hysteresis_f: float):
        self.setpoint_f = setpoint_f
        self.hysteresis_f = hysteresis_f
        self.mode = Mode.OFF
        self.last_temp_f = None

    def cycle_mode(self):
        self.mode = Mode((int(self.mode) + 1) % 3)

    def set_setpoint(self, val_f: float):
        self.setpoint_f = val_f

    def apply(self, temp_f: float):
        """Return tuple: (heat_on, cool_on) based on hysteresis + mode."""
        self.last_temp_f = temp_f
        if self.mode == Mode.HEAT:
            if temp_f < (self.setpoint_f - self.hysteresis_f):
                return True, False   # heating needed
            if temp_f >= self.setpoint_f:
                return False, False  # stop heating
            return False, False
        elif self.mode == Mode.COOL:
            if temp_f > (self.setpoint_f + self.hysteresis_f):
                return False, True   # cooling needed
            if temp_f <= self.setpoint_f:
                return False, False  # stop cooling
            return False, False
        else:
            return False, False

