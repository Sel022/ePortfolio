import board, busio, adafruit_ahtx0

class AHT20Sensor:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self._dev = adafruit_ahtx0.AHTx0(i2c)

    def read_f(self) -> float:
        # AHT20 returns Celsius
        c = float(self._dev.temperature)
        return c * 9.0 / 5.0 + 32.0

