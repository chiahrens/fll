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
#rotate(90)        # Rotates the robot 90 degrees to the right
#rotate(-180)    # Rotates the robot 180 degrees to the left
def rotate(angle):
    robot.move(angle * 1.67, 'degrees', 100, 30)

# Moves robot forward or backward by inches.
# Example:
#move(15)        # Moves robot forward 15 inches at DEFAULT_SPEED
#move(-7, 25)    # Moves robot backward 7 inches at 25% speed
def move(inches, speed=None, steering=0):
    robot.move(inches, 'in', steering, speed=speed)

# Follow line for specified number of inches
# Example:
#follow_line(right, 15)        # Follow line for 15 inches using the right light sensor
#follow_line(left, 8)        # Follow line for 8 inches using the left light sensor
def follow_line(side, inches, speed=DEFAULT_SPEED):
    reset_odometer()
    while read_odometer() < inches:
        steering = int(side.get_reflected_light() - 50)
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

################################ Missions Start Here ################################

def m02_m11():
    reset_arms()
    move(9)
    rotate(-40)
    follow_line(right, 18.5)
    rotate(-90)
    move(-6.5)
    rotate(-91)
    arm(back, -65)
    move(-10, 5)
    move(5)
    reset_arms()
    rotate(90)
    move(6.5)
    rotate(88)
    follow_line(right, 26)
    arm(back, -55)
    rotate(170)
    move(-15, 25)
    left_wheel.start()
    time.sleep(1.5)
    left_wheel.stop()
    move(15)
    rotate(-15)
    move(50)

def m06_13():
    reset_arms()
    arm(front, -45)
    move(9)
    rotate(-40)
    follow_line(right, 27)
    rotate(-90)
    arm(back, -45)
    follow_line(right, 12)
    move(6)
    reset_arms()
    rotate(80)
    follow_line(right, 22)
    rotate(90)
    move(-1.5)
    arm(back, -90, 100)
    move(2.5)
    reset_arms()
    rotate(90)
    move(40)
    rotate(-45)
    move(28)

def m05_08():
    reset_arms()
    rotate(-45)
    move(6.5)
    follow_line(right, 9)
    move(3)
    rotate(-50)
    arm(front, -40)
    follow_line(right, 17.8)
    rotate(-5)
    arm(front, 10)
    time.sleep(.5)
    move(-1)
    arm(front, -65)
    rotate(-45)
    move(3)
    arm(front, 55)
    time.sleep(.5)
    arm(front, -55)
    rotate(-125)
    move(25)
    rotate(80)
    move(12)

def m12():
    reset_arms()
    move(9)
    rotate(-40)
    follow_line(right, 49)
    rotate(-56)
    move(2.4)
    arm(front, -90)
    rotate(-30)
    reset_arms()
    rotate(-70)
    move(4.5)
    arm(front, -90)
    rotate(-40)
    move(55)

m12()
#m02_m11()
#m06_13()
#m05_08()



# Exit code
raise SystemExit()
