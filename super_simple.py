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
def reset_arms():
    front.start(50)
    back.start(50)
    time.sleep(.5)
    front.stop()
    back.stop()

# Reset odometer to 0
def reset_odometer():
    right_wheel.set_degrees_counted(0)

# Read odometer. Return distance traveled in inches
def read_odometer():
    return (right_wheel.get_degrees_counted() / 360) * WHEEL_CIRCUMFERENCE

# Rotates the robot by specified angle - positive to rotate right, negative to rotate left.
# Example:
#   rotate(90)        # Rotates the robot 90 degrees to the right
#   rotate(-180)      # Rotates the robot 180 degrees to the left
def rotate(angle):
    robot.move(angle * 1.67, 'degrees', 100, 30)

# Moves robot forward or backward by inches.
# Example:
#   move(15)          # Moves robot forward 15 inches at DEFAULT_SPEED
#   move(-7, 25)      # Moves robot backward 7 inches at 25% speed
def move(inches, speed=None, steering=0):
    robot.move(inches, 'in', steering, speed=speed)

# Follow line for specified number of inches
# Example:
#   follow_line(right, 15)        # Follow line for 15 inches using the right light sensor
#   follow_line(left, 8)          # Follow line for 8 inches using the left light sensor
def follow_line(side, inches, speed=DEFAULT_SPEED):
    reset_odometer()
    while read_odometer() < inches:
        steering = int(side.get_reflected_light() - 50)
        robot.start_at_power(speed, steering)
    robot.stop()

# Move front or back attachment
# Example:
#   arm(front, 45)        # Move the front attachment up by 45 degrees
#   arm(back, -90)        # Move the back attachment down by 90 degrees
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

################################ Missions Start Here ################################

def m02():
    reset_arms()
    move(-26.5)
    arm(back, -55)
    move(-10, 5)
    move(35)

def m11():
    reset_arms()
    rotate(-25)
    move(3)
    follow_line(right, 50)
    arm(back, -55)
    rotate(175)
    move(-15)
    right_wheel.run_for_seconds(2)
    move(70)

def m13():
    reset_arms()
    arm(front, -90)
    rotate(-25)
    move(3)
    follow_line(right, 29)
    rotate(-90)
    follow_line(right, 12)
    move(6)
    rotate(80)
    follow_line(right, 22)
    arm(front, 90)
    rotate(-88)
    move(1)
    arm(back, -90)
    arm(front, -90, 100)
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
    follow_line(right, 9)
    move(3)
    rotate(-50)
    arm(front, 45, -25)
    follow_line(right, 18)
    rotate(-5)
    arm(front, 45, 25)

def m05():
    reset_arms()
    rotate(-45)
    move(6.5)
    follow_line(right, 9)
    move(3)
    rotate(-50)
    arm(front, 90, -25)
    follow_line(right, 17.7)
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
#m05()

#arm(front, -90)
#arm(back, -90)
reset_arms()


# Exit code
raise SystemExit()
