import pyb

"""Mouse which uses accelerometer for movement
USR button acts as left mouse button

To use this program copy `main.py` and `boot.py`
into your MicroPython microcontroller, unmount it
and pres RST button. Microcontroller will boot into
USB-HID mode.

To get back into editing, perform soft reset.
While holding USR button, click RST button.
Release USR button, while orange LED is on"""

switch = pyb.Switch()
accel = pyb.Accel()

while True:
    if switch():
        # I decided that mouse shouldn't move while pushing a button
        tpl = (1, 0, 0, 0)
    else:
        # Y axis is inverted
        tpl = (0, accel.x(), -accel.y(), 0)
    pyb.hid(tpl)
    pyb.delay(20)
    # print hid tuple into REPL
    print(tpl)
