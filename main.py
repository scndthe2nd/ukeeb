import matrix


matrix.Keeb(matrix.MATRIX, matrix.KEYPAD, matrix.KEY_COUNT, matrix.COLS, matrix.ROWS).run()



'''
## Output assignments on the SPAM LIKELY Rev 0 keyboard
Shift Controller pins
d2 - LC > 12 + 13
d3 - CLK > 11
d4 - Out > 9

Thumbstick
A0 - X axis
A1 - Y axis

5 way 
d5 - Up
d8 - Left
d9 - Down
d0 - Center
d1 - Right

I2C 0
SDA
SCL

I2C 1
SDA1 - D6
SCL1 - D7

SD Card
D10
MOSI
SCK
MISO

Extra Pins
A2
A3
SCK
MISO
MOSI
D10

'''
