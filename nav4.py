from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Initialize motors and sensors
robot = MotorPair('A', 'E')
robot.set_motor_rotation(27.63)
robot.set_default_speed(35)
left_wheel = Motor('A')
right_wheel = Motor('E')
left = ColorSensor('B')
right = ColorSensor('F')
front = Motor('D')
back = Motor('C')

def reset_odometer():
    right_wheel.set_degrees_counted(0)

def distance_traveled():
    return (right_wheel.get_degrees_counted() / 360) * 27.63

def rotate(angle):
    robot.move(angle * 1.67, 'degrees', 100, 20)

def follow_line(distance):
    reset_odometer()
    while distance_traveled() < distance:
        steer = int(right.get_reflected_light() - 50)
        robot.start_at_power(35, steer)
    robot.stop()

def follow_line_stop():
    while left.get_reflected_light() > 25:
        steer = int(right.get_reflected_light() - 50)
        robot.start_at_power(20, steer)
    robot.stop()

def move(distance, angle=0, speed=None):
    rotate(angle)
    robot.move(distance, 'cm', 0, speed)

################################ Helper functions Start Here ################################

def bottom_horizontal(distance):
    move(23, -5)
    follow_line(distance)
    follow_line_stop()

def left_vertical(distance):
    move(19, -30)
    follow_line(20)
    rotate(-60)
    follow_line(distance)
    follow_line_stop()

def top_horizontal(distance):
    move(19, -30)
    follow_line(20)
    rotate(-60)
    move(8, 10)
    follow_line(distance)
    follow_line_stop()

################################ Mission functions Start Here ################################

def m06():
    bottom_horizontal(64)

def m09():
    bottom_horizontal(90)

def m11():
    bottom_horizontal(121)

def m04():
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
    move(7)
    rotate(-90)
    follow_line(28)
    move(28)
    rotate(-70)
    move(28)
