from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Define MotorPair with right motor on port A and left motor on port B. Set wheel size to 11 inches and default speed to 45%.
WHEEL_CIRCUMFERENCE = 11
motor_pair = MotorPair('A', 'E')
motor_pair.set_motor_rotation(WHEEL_CIRCUMFERENCE, 'in')
motor_pair.set_default_speed(35)
left_motor= Motor('A')
right_motor = Motor('E')
front = Motor('D')
back = Motor('C')
left_light = ColorSensor('B')
right_light = ColorSensor('F')

def reset_arms():
    front.start(50)
    back.start(50)
    time.sleep(.5)
    front.stop()
    back.stop()

# Reset odometer to 0
def reset_odometer():
    right_motor.set_degrees_counted(0)

# Read odometer
def read_odometer():
    return (right_motor.get_degrees_counted() / 360) * WHEEL_CIRCUMFERENCE

# Get reflected light from light sensor. If side is 'left', use left sensor. If side is 'right', use right sensor
def get_reflected_light(side='left'):
    if side == 'left':
        return left_light.get_reflected_light() - 50
    else:
        return right_light.get_reflected_light() - 50

# Rotates the robot by specified angle. Positive to rotate right. Negative to rotate left.
def rotate(angle):
    motor_pair.move(angle * 1.67, 'degrees', 100, 30)

# Moves robot forward or backward by inches. If angle is set, it rotates the robot by specified angle first.
def move(inches, steering=0, speed=None):
    motor_pair.move(inches, 'in', steering, speed=speed)

def follow_line(inches, side='left', speed=motor_pair.get_default_speed()):
    reset_odometer()
    while read_odometer() < inches:
        steering = int(get_reflected_light(side))
        motor_pair.start_at_power(speed, steering)
    motor_pair.stop()

def front_arm(degrees, speed=25):
    front.run_for_degrees(degrees * 2, speed)

def front_arm2(degrees, speed=25):
    front.set_degrees_counted(0)
    while abs(front.get_degrees_counted()) < abs(degrees * 2):
        front.start(speed)
    front.stop()

def back_arm(degrees, speed=25):
    back.run_for_degrees(degrees * 2, speed)

def m02():
    reset_arms()
    move(-26.5)
    back_arm(-55)
    move(-10, speed=5)
    move(35)

def m11():
    reset_arms()
    rotate(-25)
    move(3)
    follow_line(50, 'right')
    back_arm(-55)
    rotate(175)
    move(-15)
    left_motor.run_for_seconds(2)
    move(70)

def m13():
    reset_arms()
    front_arm(-90)
    rotate(-25)
    move(3)
    follow_line(29, 'right')
    rotate(-90)
    follow_line(12, 'right')
    move(6)
    rotate(80)
    follow_line(22, 'right')
    front_arm(90)
    rotate(-88)
    move(1)
    back_arm(-90)
    front_arm(-90, speed=100)
    reset_arms()
    move(-3)
    rotate(-90)
    move(40)
    rotate(-45)
    move(28)

def m08():
    reset_arms()
    rotate(-45)
    move(6.5)
    follow_line(9, 'right')
    move(3)
    rotate(-50)
    front_arm(45, -25)
    follow_line(18, 'right')
    rotate(-5)
    front_arm(45, 25)

def m05():
    reset_arms()
    rotate(-45)
    move(6.5)
    follow_line(9, 'right')
    move(3)
    rotate(-50)
    front_arm(90, -25)
    follow_line(17.7, 'right')
    rotate(-5)
    front.run_for_seconds(1, 50)
    rotate(-45)
    front.run_for_seconds(1, -100)
    move(2)
    front.run_for_seconds(.5, 100)
    front.run_for_seconds(.5, -100)
    rotate(-110)
    move(27)

#m02()
#m11()
#m13()
#m08()
m05()

#front_arm(45, 100)

# Exit code
raise SystemExit()
