import machine
import utime

led = machine.Pin(2, machine.Pin.OUT)
input1 = machine.ADC(0)

while True:
    value = input1.read()
    print("value: {}".format(value))
    utime.sleep(10)