from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Define all motor ports
left_motor, right_motor, front_motor, back_motor, left_light, right_light = 'A', 'E', 'D', 'C', 'B', 'F'

front = Motor(front_motor)
back = Motor(back_motor)

def reset_arms(position='up'):
    if position == 'up':
        direction = 1
    else:
        direction = -1
    front.start_at_power(35 * direction)
    back.start_at_power(35 * direction)
    time.sleep(1.5)
    front.start_at_power(-35 * direction)
    back.start_at_power(-35 * direction)
    time.sleep(.16)
    front.stop()
    back.stop()

def arm(motor, degrees, speed=25):
    motor.run_for_degrees(int(degrees*3.5), speed)

reset_arms()
arm(front, -45)
arm(back, -45)
reset_arms('down')
arm(front, 45)
arm(back, 45)

reset_arms()
arm(front, -90)
arm(back, -90)
reset_arms('down')
arm(front, 90)
arm(back, 90)

raise SystemExit()
