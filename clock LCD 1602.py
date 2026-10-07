from machine import I2C, Pin, RTC
import time
# ===== پەیوەستکردنی I2C =====
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
# ===== دیاریکردنی ناونیشانی LCD =====
LCD_ADDR = 0x27
# ===== دروستکردنی LCD =====
from i2c_lcd import I2cLcd
lcd = I2cLcd(i2c, LCD_ADDR, 2, 16)   # 2 ڕیز، 16 ستوون
# ===== دیاریکردنی RTC =====
rtc = RTC()

print(" LCD 1602")
while True:
    # وەرگرتنی کات و بەروار
    now = rtc.datetime()
    # ===== ڕیزی یەکەم: کات =====
    # (ساڵ, مانگ, ڕۆژ, ڕۆژی هەفتە, کاتژمێر, خولەک, چرکە, ژێرچرکە)
    time_str = "{:02d}:{:02d}:{:02d}".format(now[4], now[5], now[6])
    lcd.move_to(0, 0)
    lcd.putstr("Time: " + time_str)
    # ===== ڕیزی دووەم: بەروار =====
    date_str = "{:04d}-{:02d}-{:02d}".format(now[0], now[1], now[2])
    lcd.move_to(0, 1)
    lcd.putstr("Date: " + date_str)
    # ===== پیشاندان لە Shell (بۆ دڵنیایی) =====
    print("📅 {}   {}".format(date_str, time_str))
    
    time.sleep(1)
    