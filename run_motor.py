import lgpio
import time

# Motorpins (BCM)
LEFT_IN1 = 17
LEFT_IN2 = 18
RIGHT_IN1 = 27
RIGHT_IN2 = 22

# Öppna GPIO-chip
h = lgpio.gpiochip_open(0)

# Sätt pins som utgång
for pin in [LEFT_IN1, LEFT_IN2, RIGHT_IN1, RIGHT_IN2]:
    lgpio.gpio_claim_output(h, pin)

def set_motor(left_speed, right_speed):
    """
    left_speed, right_speed: -1.0 till 1.0
    """
    # vänster
    if left_speed > 0:
        lgpio.tx_pwm(h, LEFT_IN1, 1000, int(left_speed*100))
        lgpio.tx_pwm(h, LEFT_IN2, 1000, 0)
    elif left_speed < 0:
        lgpio.tx_pwm(h, LEFT_IN1, 1000, 0)
        lgpio.tx_pwm(h, LEFT_IN2, 1000, int(-left_speed*100))
    else:
        lgpio.tx_pwm(h, LEFT_IN1, 1000, 0)
        lgpio.tx_pwm(h, LEFT_IN2, 1000, 0)

    # höger
    if right_speed > 0:
        lgpio.tx_pwm(h, RIGHT_IN1, 1000, int(right_speed*100))
        lgpio.tx_pwm(h, RIGHT_IN2, 1000, 0)
    elif right_speed < 0:
        lgpio.tx_pwm(h, RIGHT_IN1, 1000, 0)
        lgpio.tx_pwm(h, RIGHT_IN2, 1000, int(-right_speed*100))
    else:
        lgpio.tx_pwm(h, RIGHT_IN1, 1000, 0)
        lgpio.tx_pwm(h, RIGHT_IN2, 1000, 0)

try:
    print("🚗 Framåt...")
    set_motor(0.5, 0.5)
    time.sleep(2)

    print("↩️ Backåt...")
    set_motor(-0.5, -0.5)
    time.sleep(2)

    print("↪️ Vänster...")
    set_motor(-0.5, 0.5)
    time.sleep(2)

    print("↩️ Höger...")
    set_motor(0.5, -0.5)
    time.sleep(2)

    print("⏹️ Stopp")
    set_motor(0, 0)

finally:
    lgpio.gpiochip_close(h)
