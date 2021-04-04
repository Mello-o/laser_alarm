from gpiozero import LightSensor, LED, Buzzer
from time import sleep

led = LED(20)
ldr = LightSensor(21)
buzzer = Buzzer(12)

while True:
    
    l = ldr.value
    print(l)
    
    if l > 0.5:
        led.on()
        buzzer.on()
    else:
        led.off()
        buzzer.off()
        
    sleep(0.3)