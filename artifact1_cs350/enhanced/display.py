import board, digitalio
import adafruit_character_lcd.character_lcd as character_lcd

class Lcd16x2:
    def __init__(self, rs, en, d4, d5, d6, d7, cols, rows):
        rs_pin = digitalio.DigitalInOut(getattr(board, rs))
        en_pin = digitalio.DigitalInOut(getattr(board, en))
        d4_pin = digitalio.DigitalInOut(getattr(board, d4))
        d5_pin = digitalio.DigitalInOut(getattr(board, d5))
        d6_pin = digitalio.DigitalInOut(getattr(board, d6))
        d7_pin = digitalio.DigitalInOut(getattr(board, d7))
        self.lcd = character_lcd.Character_LCD_Mono(
            rs_pin, en_pin, d4_pin, d5_pin, d6_pin, d7_pin, cols, rows
        )
        self.cols = cols
        self.rows = rows
        self.clear()

    def clear(self):
        self.lcd.clear()

    def write_lines(self, line1: str, line2: str):
        self.lcd.cursor_position(0, 0)
        self.lcd.message = (line1[:self.cols]).ljust(self.cols)
        self.lcd.cursor_position(0, 1)
        self.lcd.message = (line2[:self.cols]).ljust(self.cols)

    def goodbye(self):
        self.clear()
        self.lcd.message = "Goodbye!"

