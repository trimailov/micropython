import pyb

switch = pyb.Switch()
accel = pyb.Accel()

while True:
    if switch():
        tpl = (1, 0, 0, 0)
    else:
        tpl = (0, accel.x(), -accel.y(), 0)
    pyb.hid(tpl)
    pyb.delay(20)
    print(tpl)
