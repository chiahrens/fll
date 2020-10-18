from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Define MotorPair with right motor on port A and left motor on port B. Set wheel size to 11 inches and default speed to 45%.
DEFAULT_SPEED=35
motor_pair = MotorPair('A', 'E')
motor_pair.set_motor_rotation(11, 'in')
motor_pair.set_default_speed(DEFAULT_SPEED)
left_motor= Motor('A')
right_motor = Motor('E')
front = Motor('D')
back = Motor('C')
left_light = ColorSensor('B')
right_light = ColorSensor('F')

# Rotates the robot by specified angle. Positive to rotate right. Negative to rotate left.
def rotate(angle):
    motor_pair.move(angle * 1.67, 'degrees', 100, 30)

# Moves robot forward or backward by inches. If angle is set, it rotates the robot by specified angle first.
def move(inches, angle=0, speed=None):
    if angle != 0:
        rotate(angle)
    motor_pair.move(inches, 'in', speed=speed)

def follow_line_left(inches, speed=DEFAULT_SPEED):
    right_motor.set_degrees_counted(0)
    while right_motor.get_degrees_counted() * 11 / 360 < inches:
        steering = int(left_light.get_reflected_light() - 50)
        motor_pair.start_at_power(speed, steering)
    motor_pair.stop()

def follow_line_right(inches, speed=DEFAULT_SPEED):
    right_motor.set_degrees_counted(0)
    while right_motor.get_degrees_counted() * 11 / 360 < inches:
        steering = int(right_light.get_reflected_light() - 50)
        motor_pair.start_at_power(speed, steering)
    motor_pair.stop()

def front_arm(seconds, speed):
    front.start(speed)
    time.sleep(seconds)
    front.stop()


def back_arm(seconds, speed):
    back.start(speed)
    time.sleep(seconds)
    back.stop()

def m02():
    move(-27)
    back_arm(1, -20)
    move(-10, speed=5)
    move(35)
    back_arm(1, 25)

def m11():
    move(3, -25)
    follow_line_right(50)
    back_arm(1, -22)
    move(-15, 175)
    left_motor.run_for_seconds(2)
    move(10)
    back_arm(1, 25)
    move(55, 0)

def m13():
    front_arm(2, -20)
    move(3, -25)
    follow_line_right(29)
    rotate(-90)
    follow_line_right(12)
    move(6)
    rotate(80)
    follow_line_right(22.5)
    front_arm(2, 20)
    move(2, -90)
    back_arm(1, -20)
    front_arm(2, -20)
    front_arm(2, 20)
    back_arm(1, 20)
    move(-5)
    move(40, -90)
    move(28, -45)

#m02()
m11()
#m13()

#front_arm(2, -20)
#front_arm(2, 20)
#back_arm(1, 20)

# Exit code
raise SystemExit()
