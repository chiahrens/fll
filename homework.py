from spike import Motor, MotorPair, ColorSensor

# Initialize motors and sensors
motor_pair = MotorPair('A', 'E')
motor_pair.set_motor_rotation(11, 'in')
right_wheel = Motor('E')
color_sensor = ColorSensor('F')

# Homework assignment #1
# Write a line follower function that stops when the wheel rotation reaches the "rotations" parameter
# The current logic is from the example and never stops. Change it so that it does
# Hint #1: right_wheel.set_degrees_counted(0) resets the right wheel rotation counter to zero
# Hint #2: right_wheel.get_degrees_counted() returns the number of degrees counted
# Hint #3: There are 360 degrees in a wheel rotation.
# Example:
#  follow_line(10) should make to robot follow the line for 10 rotations of the wheel
def follow_line(rotations):
  while True:
    steering = color_sensor.get_reflected_light() - 50
    motor_pair.start_at_power(35, int(steering))
  motor_pair.stop()
  
# Homework assignment #2
# Write a function to rotate the robot by exact degrees
# The current function will cause the robot to turn either right (postive), or left (negative), but the math is off.
# Example:
#   rotate(90) should make the robot rotate 90 degrees to the right
#   rotate(-90) should make the robot rotate 90 degrees to the left
def rotate(degrees):
  motor_pair.move(degrees * 1, 'degrees', 100, 20)
  
# Homework assignment #3
# Change follow_line from assignment #1 to stop at inches
# Hint #1: There are 360 degrees in a wheel rotation. The circumference of the wheel is 11 inches.
# Example:
#   follow_line(24) should make the robot follow the line for 24 inches
def follow_line_inches(inches):

