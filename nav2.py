from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Initialize motors and sensors
WHEEL_CIRCUMFERENCE = 11
DEFAULT_SPEED = 30
robot = MotorPair('A', 'E')
robot.set_motor_rotation(WHEEL_CIRCUMFERENCE, 'in')
robot.set_default_speed(DEFAULT_SPEED)
left_wheel= Motor('A')
right_wheel = Motor('E')
front = Motor('D')
back = Motor('C')
left = ColorSensor('B')
right = ColorSensor('F')


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

def turn(angle, steering, turn_multiplier, speed=20):
    if angle > 0:
        start = left_wheel.get_degrees_counted()
        robot.start(steering, speed)
        while abs(left_wheel.get_degrees_counted() - start) < abs(angle * turn_multiplier) :
            continue
    elif angle < 0:
        start = right_wheel.get_degrees_counted()
        robot.start(-steering, speed)
        while abs(right_wheel.get_degrees_counted() - start) < abs(angle * turn_multiplier) :
            continue
    
def rotate(angle, speed=20):
    turn(angle, 100, 1.6, speed)

def pivot(angle, speed=20):
    turn(angle, 99, 3.2, speed)

def move(inches, steering=0, speed=DEFAULT_SPEED):
    reset_odometer()
    robot.start(steering, speed)
    while read_odometer() < inches:
        continue

def follow_line(inches, speed=DEFAULT_SPEED):
    reset_odometer()
    while read_odometer() < inches:
        steering = int(right.get_reflected_light() - 50)
        robot.start_at_power(speed, steering)

def stop_at_line(speed=DEFAULT_SPEED):
    while left.get_reflected_light() > 25:
        steering = int(right.get_reflected_light() - 50)
        robot.start_at_power(speed, steering)
    robot.stop()


################################ Helper functions Start Here ################################

def start_top_line(inches):
    #reset_arms()
    rotate(-26)
    move(6.6)
    follow_line(10)
    robot.stop()
    pivot(-45)
    follow_line(inches, True)
    stop_at_line()

def start_bottom_line(inches):
    #reset_arms()
    move(8.3)
    follow_line(inches, True)
    stop_at_line()

def start_line3(inches):
    #reset_arms()
    rotate(-26)
    move(6.6)
    line(10)
    robot.stop()
    rotate(-25)
    move(13.5)
    follow_line(inches, True)
    stop_at_line()

#start_bottom_line(35)
#start_bottom_line(45)
#start_bottom_line(58)

#start_top_line(29.5)
#start_top_line(37)

#start_line3(36)
#start_line3(42)
#start_line3(52)
#start_line3(64)
