from gpiozero import Motor
from time import sleep

# Motor via två pinnar (framåt, bakåt)
left = Motor(forward=17, backward=18, pwm=True)
right = Motor(forward=27, backward=22, pwm=True)

print("🚗 Framåt...")
left.forward(0.5)
right.forward(0.5)
sleep(2)

print("↩️ Backåt...")
left.backward(0.5)
right.backward(0.5)
sleep(2)

print("↪️ Vänster...")
left.backward(0.5)
right.forward(0.5)
sleep(2)

print("↩️ Höger...")
left.forward(0.5)
right.backward(0.5)
sleep(2)

print("⏹️ Stopp")
left.stop()
right.stop()
