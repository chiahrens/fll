from spike import Motor, MotorPair, ColorSensor, PrimeHub

# Define MotorPair with right motor on port A and left motor on port B. Set wheel size to 11 inches and default speed to 45%.
motor_pair = MotorPair('A', 'E')
motor_pair.set_motor_rotation(11, 'in')
motor_pair.set_default_speed(45)

# Rotates the robot by specified angle. Positive to rotate right. Negative to rotate left.
def rotate(angle):
    motor_pair.move(angle * 1.67, 'degrees', 100, 30)

# Moves robot forward by inches. If angle is set, it rotates the robot by specified angle first.
def forward(inches, angle=0):
    rotate(angle)
    motor_pair.move(inches, 'in')

# Moves robot backwards by inches. If angle is set, it rotates the robot by specified angle first.
def backward(inches, angle=0):
    rotate(angle)
    motor_pair.move(-inches, 'in')

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
