from Adafruit_MotorHAT import Adafruit_MotorHAT
from Adafruit_MotorHAT import Adafruit_MotorHAT

# sätt i2c_bus=1 explicit
mh = Adafruit_MotorHAT(addr=0x60, i2c_bus=1)


motor = mh.getMotor(1)
motor.setSpeed(0)
motor.run(Adafruit_MotorHAT.FORWARD)
