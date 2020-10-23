from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Initialize motors and sensors
WHEEL_CIRCUMFERENCE = 11
DEFAULT_SPEED = 35
robot = MotorPair('A', 'E')
robot.set_motor_rotation(WHEEL_CIRCUMFERENCE, 'in')
robot.set_default_speed(DEFAULT_SPEED)
left_wheel= Motor('A')
right_wheel = Motor('E')
front = Motor('D')
back = Motor('C')
left = ColorSensor('B')
right = ColorSensor('F')

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

# Read odometer. Return distance traveled in inches
def read_odometer():
    return (right_wheel.get_degrees_counted() / 360) * WHEEL_CIRCUMFERENCE

# Rotates the robot by specified angle - positive to rotate right, negative to rotate left.
# Example:
#rotate(90)        # Rotates the robot 90 degrees to the right
#rotate(-180)    # Rotates the robot 180 degrees to the left
def rotate(angle, speed=20):
    robot.move(angle * 1.67, 'degrees', 100, speed)

def pivot(angle, speed=20):
    if angle == 0:
        return
    elif angle > 0:
        robot.move(angle * 1.67, 'degrees', 99, speed)
    else:
        robot.move(angle * -1.67, 'degrees', -99, speed)
    
# Moves robot forward or backward by inches.
# Example:
#move(15)        # Moves robot forward 15 inches at DEFAULT_SPEED
#move(-7, 25)    # Moves robot backward 7 inches at 25% speed
def move(inches, rotation=0, speed=None, steering=0):
    if rotation != 0:
        rotate(rotation)
    if inches != 0:
        robot.move(inches, 'in', steering, speed)

# Follow line for specified number of inches
# Example:
#follow_line(15)        # Follow line for 15 inches using the right light sensor
#follow_line(8, left)        # Follow line for 8 inches using the left light sensor
def follow_line(inches, side=right, speed=DEFAULT_SPEED):
    reset_odometer()
    while read_odometer() < inches:
        steering = int(side.get_reflected_light() - 50)
        robot.start_at_power(speed, steering)
    robot.stop()


def start_line(inches, initial_rotation=0, initial_start=0, stop_at_line=False, speed=DEFAULT_SPEED):
    if initial_rotation != 0:
        rotate(initial_rotation)
    reset_odometer()
    if initial_start != 0:
        robot.start(0, speed)
        while read_odometer() < initial_start:
            continue
    while read_odometer() < inches or (stop_at_line == True and left.get_reflected_light() > 25):
        steering = int(right.get_reflected_light() - 50)
        robot.start_at_power(speed, steering)
    robot.stop()

# Move front or back attachment
# Example:
#arm(front, 45)        # Move the front attachment up by 45 degrees
#arm(back, -90)        # Move the back attachment down by 90 degrees
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

################################ Helper functions Start Here ################################

def start_top_line(inches):
    reset_arms()
    start_line(15.5, -45, 6.5)
    move(3)
    rotate(-50)
    start_line(0, 0 , inches)

def start_bottom_line(inches):
    reset_arms()
    start_line(inches, -12, 7)

#start_line(15, 90, 5, True)
pivot(90)
pivot(-90)
pivot(90, -20)
pivot(-90, -20)
