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

def back_arm(degrees, speed=25):
    back.run_for_degrees(degrees * 2, speed)

def m02():
    move(-27)
    back_arm(-45)
    move(-10, speed=5)
    move(35)

def m11():
    rotate(-25)
    move(3)
    follow_line_right(50)
    back_arm(-45)
    rotate(175)
    move(-15)
    left_motor.run_for_seconds(2)
    move(10)
    back_arm(45)
    move(55)

def m13():
    reset_arms()
    front_arm(-90)
    rotate(-25)
    move(3)
    follow_line_right(29)
    rotate(-90)
    follow_line_right(12)
    move(6)
    rotate(80)
    follow_line_right(22.5)
    front_arm(90)
    rotate(-90)
    move(2)
    back_arm(-90)
    front_arm(-90)
    reset_arms()
    move(-5)
    rotate(-90)
    move(40)
    rotate(-45)
    move(28)

#m02()
#m11()
#m13()

# Exit code
raise SystemExit()
