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
def rotate(angle, speed=20):
    robot.move(angle * 1.67, 'degrees', 100, speed)

# Moves robot forward or backward by inches.
# Example:
#move(15)        # Moves robot forward 15 inches at DEFAULT_SPEED
#move(-7, 25)    # Moves robot backward 7 inches at 25% speed
def move(inches, speed=None, steering=0):
    robot.move(inches, 'in', steering, speed)

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

# Step Counter, 25 seconds, 20 pts
def m02():
    reset_arms()
    rotate(-12)
    move(7)
    follow_line(right, 21)
    rotate(-90)
    move(-6.5)
    rotate(-89)
    arm(back, -65)
    move(-10, 5)
    rotate(5)
    move(35, 50)
    reset_arms()

# Step Counter & Threadmill, 45 seconds, 50 pts
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
    reset_arms()


# Pull-up and Weight Machine-magenta, back attachment. 30 seconds. 30 pts.
def m06_13():
    reset_arms()
    arm(front, -45)
    rotate(-12)
    move(7)
    follow_line(right, 29.5)
    rotate(-90)
    arm(back, -45)
    follow_line(right, 12)
    move(6)
    reset_arms()
    rotate(80)
    follow_line(right, 22.5)
    rotate(90)
    move(-1.5)
    arm(back, -90, 100)
    move(2.5)
    reset_arms()
    rotate(90)
    move(40)
    rotate(-45)
    move(28)


# Pull-up and Boccia. T attachment on front, 25 seconds, 25 points
def m06_08():
    reset_arms()
    arm(front, -45)
    rotate(-12)
    move(7)
    follow_line(right, 29.5)
    rotate(-90)
    follow_line(right, 12)
    arm(front, -45)
    rotate(22)
    move(6)
    rotate(15, 20)
    move(-.5)
    rotate(-10)
    arm(front, 45)
    arm(front, -25)
    rotate(65)
    move(-18)
    rotate(-45)
    move(-30)
    reset_arms()


# Basketball & Boccia. 25 seconds. No ball. 40 points.
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
    reset_arms()

# Row Machine. Pin in front. Bring back blue wheel. 25 seconds. 30pts plus 10pts if you push flipped blue wheel out 
def m12_09():
    reset_arms()
    rotate(-12)
    move(7)
    follow_line(right, 51.5)
    rotate(-53)
    move(2.4)
    arm(front, -90)
    rotate(-30)
    reset_arms()
    rotate(-70)
    move(4.5)
    arm(front, -90)
    rotate(-40)
    move(55)
    reset_arms()

# Threadmill & Row Machine. Pin in front. 30 seconds. 60 pts.
def m11_m12():
    reset_arms()
    rotate(-12)
    move(7)
    follow_line(right, 51.5)
    rotate(-51)
    move(2.1)
    arm(front, -90)
    rotate(-38)
    reset_arms()
    move(-.75)
    arm(back, -55)
    rotate(-93)
    move(-15, 25)
    left_wheel.start()
    time.sleep(1.5)
    left_wheel.stop()
    move(15)
    rotate(-15)
    move(50, 50)
    reset_arms()

# Boccia, carrier attachment, 15 seconds, 65 points
def m08():
    reset_arms()
    rotate(-45)
    move(6.5)
    follow_line(right, 9)
    move(3)
    rotate(-50)
    follow_line(right, 8)
    rotate(55)
    move(19)
    arm(front, -45, 15)
    time.sleep(1)
    reset_arms()
    move(-40)

# Slide
def m03():
    reset_arms()
    rotate(-45)
    move(6.5)
    follow_line(right, 9)
    move(3)
    rotate(-50)
    follow_line(right, 13)
    rotate(90)
    move(6)
    follow_line(right, 16)
    rotate(-30)
    arm(back, -50)
    move(-4.5)
    arm(back, 5)
    back.start(15)
    robot.start(0, -10)
    time.sleep(2)
    robot.stop()
    back.stop()
    move(1)
    arm(back, -20)
    move(-1)

m03()

#reset_arms()
#m08()

#m12()
#m02_m11()
#m06_13()
#m05_08()
#m11_m12()


# Exit code
raise SystemExit()
