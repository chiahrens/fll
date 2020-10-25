from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Initialize motors and sensors
WHEEL_CIRCUMFERENCE_CM = 27.63
DEFAULT_SPEED = 35
robot = MotorPair('A', 'E')
robot.set_motor_rotation(WHEEL_CIRCUMFERENCE_CM)
robot.set_default_speed(DEFAULT_SPEED)
#robot.set_stop_action('hold')
left_wheel= Motor('A')
right_wheel = Motor('E')
front = Motor('D')
back = Motor('C')
left = ColorSensor('B')
right = ColorSensor('F')

# Move front or back attachment
# Example:
#  arm(front, 45)        # Move the front attachment up by 45 degrees
#  arm(back, -90)        # Move the back attachment down by 90 degrees
def arm(motor, degrees, speed=25):
    # motor.run_for_rotation(rotations, speed)
    motor.set_degrees_counted(0)
    if(degrees > 0):
        motor.start(speed)
    elif(degrees < 0):
        motor.start(-speed)
    while abs(motor.get_degrees_counted()) < abs(degrees * 2):
        continue
    motor.stop()

# Set front and back arms in up postions
def reset_arms(front_degrees=0, back_degrees=0):
    front.start(50)
    back.start(50)
    time.sleep(.5)
    front.stop()
    back.stop()
    arm(front, front_degrees)
    arm(back, back_degrees)

# Reset odometer to 0
def reset_odometer():
    right_wheel.set_degrees_counted(0)

# Read odometer. Return distance traveled in cm
def read_odometer():
    return (right_wheel.get_degrees_counted() / 360) * WHEEL_CIRCUMFERENCE_CM

# Rotates the robot by specified angle - positive to rotate right, negative to rotate left.
# Example:
#   rotate(90)        # Rotates the robot 90 degrees to the right
#   rotate(-180)    # Rotates the robot 180 degrees to the left
def rotate(angle, speed=20):
    robot.move(angle * 1.67, 'degrees', 100, speed)

def pivot(angle, speed=20):
    if angle > 0:
        turn = 99
    elif angle < 0:
        turn = -99
    robot.move(abs(angle) * 1.67, 'degrees', turn, speed)

# Follow line for specified number of cm
# Example:
#   follow_line(15)        # Follow line for 15 cm using the right light sensor
#   follow_line(8, left)        # Follow line for 8 cm using the left light sensor
def follow_line(cm, line_stop=False, steer_x=1, speed=DEFAULT_SPEED):
    reset_odometer()
    while read_odometer() < cm:
        steering = int(right.get_reflected_light() - 50) * steer_x
        robot.start_at_power(speed, steering)
    if line_stop == True:
        while left.get_reflected_light() > 25:
            steering = int(right.get_reflected_light() - 50) * steer_x
            robot.start_at_power(speed, steering)
    robot.stop()

################################ Helper functions Start Here ################################

def start_bottom_line(cm):
    robot.move(23, 'cm', -3)
    follow_line(cm, True)

def start_top_line(cm):
    robot.move(19, 'cm', -46)
    follow_line(20)
    follow_line(15, False, 2, 15)
    follow_line(cm, True)

def start_line3(cm):
    robot.move(19, 'cm', -46)
    follow_line(20)
    follow_line(15, False, 2, 15)
    robot.move(8, 'cm', 30)
    follow_line(cm, True)

#start_bottom_line(64)
#start_bottom_line(90)
#start_bottom_line(121)

#start_top_line(18)
#start_top_line(42)

#start_line3(29)
#start_line3(45)
#start_line3(70)
#start_line3(103)

#start_bottom_line(64)
#robot.move(6)
#rotate(-90)
#follow_line(30)
#robot.move(7)
#follow_line(10)
#robot.move(8)

start_line3(103)
robot.move(13)
pivot(90, -20)
follow_line(7)
