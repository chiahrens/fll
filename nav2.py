from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Initialize motors and sensors
WHEEL_CIRCUMFERENCE_CM = 27.63
DEFAULT_SPEED = 35
robot = MotorPair('A', 'E')
robot.set_motor_rotation(WHEEL_CIRCUMFERENCE_CM)
robot.set_default_speed(DEFAULT_SPEED)
right_wheel = Motor('E')
left = ColorSensor('B')
right = ColorSensor('F')


# Reset odometer to 0
def reset_odometer():
    right_wheel.set_degrees_counted(0)


# Read odometer. Return distance traveled in cm
def read_odometer():
    return (right_wheel.get_degrees_counted() / 360) * WHEEL_CIRCUMFERENCE_CM


# Rotates the robot by specified angle - positive to rotate right, negative to rotate left.
# Parameters:
#angle - Required. Degrees to rotate. Positive to rotate right. Negative to rotate left.
#speed - Default 20. Rotation speed.
# Example:
#rotate(90)        # Rotates the robot 90 degrees to the right
#rotate(-180)    # Rotates the robot 180 degrees to the left
def rotate(angle, speed=20):
    robot.move(angle * 1.67, 'degrees', 100, speed)


# Follow line for specified number of cm.
# Parameters:
#cm - Required. Number of cm the robot should follow the line
#line_stop - Default False. If set to True, it will continue until next stop line.
#steer_x - Default 1. Setting this higher will cause sharper turns.
#speed - Default DEFAULT_SPEED. Speed of the robot.
# Example:
#follow_line(15)                # Follow line for 15 cm and stop
#follow_line(15, True)        # Follow line for 15 cm, but stop at next stop line
#follow_line(15, False, 2, 10)# Follow line for 15 cm, at 10% speed with sharper turns
def follow_line(cm, line_stop=False, steer_x=1, speed=DEFAULT_SPEED):
    reset_odometer()
    while read_odometer() < cm or (line_stop == True and left.get_reflected_light() > 25):
        steering = int(right.get_reflected_light() - 50) * steer_x
        robot.start_at_power(speed, steering)
    if line_stop == True:
        robot.stop()

def move(cm, steering=0, speed=None)
    reset_odometer()
    robot.start(steering, speed)
    while read_odometer() < cm:
        continue

################################ Helper functions Start Here ################################

def bottom_horizontal(cm):
    move(23, -3)
    follow_line(cm, True)

def left_vertical(cm):
    move(19, -46)
    follow_line(20)
    follow_line(15, False, 2, 15)
    follow_line(cm, True)

def top_horizontal(cm):
    move(19, -46)
    follow_line(20)
    follow_line(15, False, 2, 15)
    move(8, 30)
    follow_line(cm, True)

################################ Mission functions Start Here ################################

def m06:
    bottom_horizontal(64)

def m09:
    bottom_horizontal(90)

def m11:
    bottom_horizontal(121)

def m04:
    left_vertical(18)

def m08:
    left_vertical(42)

def m07:
    top_horizontal(29)

def m08:
    top_horizontal(45)

def m10:
    top_horizontal(70)

def m13:
    top_horizontal(103)

def m06_08:
    bottom_horizontal(64)
    robot.move(6)
    rotate(-90)
    follow_line(30)
    robot.move(7)
    follow_line(10)
    robot.move(8)

