from spike import Motor, MotorPair, ColorSensor, PrimeHub

# Define MotorPair with right motor on port A and left motor on port B. Set wheel size to 11 inches and default speed to 45%.
motor_pair = MotorPair('A', 'E')
motor_pair.set_motor_rotation(11, 'in')
motor_pair.set_default_speed(45)
right_motor = Motor('E')
left_light = ColorSensor('B')
right_light = ColorSensor('F')

# Rotates the robot by specified angle. Positive to rotate right. Negative to rotate left.
def rotate(angle):
    motor_pair.move(angle * 1.67, 'degrees', 100, 30)

# Moves robot forward or backward by inches. If angle is set, it rotates the robot by specified angle first.
def move(inches, angle=0):
    rotate(angle)
    motor_pair.move(inches, 'in')

def follow_line_left(inches, speed=45):
    right_motor.set_degrees_counted(0)
    while right_motor.get_degrees_counted() * 11 / 360 < inches:
        steering = int(left_light.get_reflected_light() - 50)
        motor_pair.start_at_power(speed, steering)
    motor_pair.stop()

def follow_line_right(inches, speed=45):
    right_motor.set_degrees_counted(0)
    while right_motor.get_degrees_counted() * 11 / 360 < inches:
        steering = int(right_light.get_reflected_light() - 50)
        motor_pair.start_at_power(speed, steering)
    motor_pair.stop()

# Moves the robot in a 10" x 10" square
forward(10)
forward(10, 90)
forward(10, 90)
forward(10, 90)

# Moves the robot forward 10", then rotates ther robot 180 degress, and then continue to move in same direction, but backwards another 10"
forward(10)
backward(10, 180)

# Exit code
raise SystemExit()
