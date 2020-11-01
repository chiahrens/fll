from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Initialize motors and sensors
WHEEL_CIRCUMFERENCE_CM = 27.63
DEFAULT_SPEED = 35
robot = MotorPair('A', 'E')
robot.set_motor_rotation(WHEEL_CIRCUMFERENCE_CM)
robot.set_default_speed(DEFAULT_SPEED)
left_wheel = Motor('A')
right_wheel = Motor('E')
left = ColorSensor('B')
right = ColorSensor('F')
front = Motor('D')
back = Motor('C')
front.set_degrees_counted(0)
back.set_degrees_counted(0)


# Move front or back attachment
# Example:
#arm(front, 45)        # Move the front attachment up by 45 degrees
#arm(back, -90)        # Move the back attachment down by 90 degrees
def arm(motor, degrees, speed=25):
    motor.run_for_degrees(int(degrees * 3.5), speed)

# Set front and back arms in up postions
def reset_arms():
    front.run_to_degrees_counted(0)
    back.run_to_degrees_counted(0)

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
#distance - Required. Distance in cm the robot should follow the line
#line_stop - Default False. If set to True, it will continue until next stop line.
#steer_x - Default 1. Setting this higher will cause sharper turns.
#speed - Default DEFAULT_SPEED. Speed of the robot.
# Example:
#follow_line(15)                # Follow line for 15 cm and stop
#follow_line(15, True)        # Follow line for 15 cm, but stop at next stop line
#follow_line(15, False, 2, 10)# Follow line for 15 cm, at 10% speed with sharper turns
def follow_line(distance, line_stop=False, steer_x=1, speed=DEFAULT_SPEED):
    reset_odometer()
    while read_odometer() < distance or (line_stop == True and left.get_reflected_light() > 25):
        steering = int(right.get_reflected_light() - 50) * steer_x
        robot.start_at_power(speed, steering)
    robot.stop()

def move(distance, angle=0, speed=None):
    rotate(angle)
    robot.move(distance, speed=speed)

################################ Helper functions Start Here ################################

def bottom_horizontal(cm):
    move(20, -6)
    follow_line(cm, True)

def left_vertical(cm):
    move(16, -46)
    follow_line(23)
    follow_line(18, False, 3, 15)
    follow_line(cm, True)

def top_horizontal(cm):
    move(16, -46)
    follow_line(23)
    follow_line(18, False, 2, 15)
    move(8, 30)
    follow_line(cm, True)

################################ Mission functions Start Here ################################

def m06():
    bottom_horizontal(64)

def m09():
    bottom_horizontal(90)

def m11():
    bottom_horizontal(121)

def m04():
    left_vertical(0)

def m04b():
    left_vertical(18)

def m08():
    left_vertical(42)

def m07():
    top_horizontal(29)

def m08b():
    top_horizontal(45)

def m10():
    top_horizontal(70)

def m13():
    top_horizontal(103)

def m06_08():
    bottom_horizontal(64)
    robot.move(6)
    rotate(-90)
    follow_line(28)
    move(7)
    follow_line(11)
    move(10)

def m06_07():
    bottom_horizontal(64)
    robot.move(6)
    rotate(-90)
    follow_line(26)
    move(10)
    robot.stop()
    rotate(-35)
    robot.move(30)

def threadmill():
    m11()
    rotate(-183)
    arm(back, -90)
    robot.move(-30, speed=35)
    left_wheel.run_for_seconds(1.6)
    robot.move(30, steering=0, speed=25)
    robot.move(140, speed=100)

def row_machine():
    m11()
    rotate(-48)
    robot.move(12)
    arm(front, -90)
    rotate(-50)
    robot.move(-3)
    arm(front, 90)
    rotate(-90)
    robot.move(20)
    robot.move(140, speed=100)

threadmill()
reset_arms()


#arm(front, -90)
#arm(front, 90)
#arm(front, -45)
#reset_arms()

raise SystemExit()
