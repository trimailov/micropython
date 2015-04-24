import pyb


# result ~2.7M
def test():
    counter = 0
    millis = pyb.millis
    end_time = millis() + 10000
    while millis() < end_time:
        counter += 1
    return counter


# undocumented
# result ~4M
@micropython.native
def native_test():
    counter = 0
    millis = pyb.millis
    end_time = millis() + 10000
    while millis() < end_time:
        counter += 1
    return counter


# undocumented, do not know how to make it work
#@micropython.viper
#def viper_test() -> int:
#    counter:int = 0
#    millis = pyb.millis
#    end_time = millis() + 10000
#    while millis() < end_time:
#        counter += 1
#    return counter
