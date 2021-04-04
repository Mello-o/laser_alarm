from gpiozero import LightSensor, LED
from time import sleep

led = LED(20)
ldr = LightSensor(21)

while True:
    
    l = ldr.value
    print(l)
    
    if l > 0.5:
        led.on()
    else:
        led.off()
        
    sleep(0.3)