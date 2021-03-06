from spike import Motor, MotorPair, ColorSensor

# Initialize motors and sensors
motor_pair = MotorPair('A', 'E')
motor_pair.set_motor_rotation(27.63)
right_wheel = Motor('E')
color_sensor = ColorSensor('F')

# Homework assignment #1
# You need to raise the light sensors on your robot. They are too low to the ground.
# Follow the instructions on https://primelessons.org/RobotDesigns/instructions/ADBModifications.pdf
# Picture of what it will look like on the robot - https://photos.app.goo.gl/VapzimdMYeoP7CkB7


# Homework assignment #2
# Write a function to rotate the robot by exact degrees
# The current function will cause the robot to turn either right (postive), or left (negative), but not the correct amount
# Example:
#   rotate(90) should make the robot rotate 90 degrees to the right
#   rotate(-90) should make the robot rotate 90 degrees to the left
def rotate(degrees):
  motor_pair.move(degrees * 1, 'degrees', 100, 20)

  
# Homework assignment #3
# Write a line follower function that stops when the wheel rotation reaches the "amount" parameter
# The current logic is from the example and never stops. Change it so that it does
# Hint #1: right_wheel.set_degrees_counted(0) resets the right wheel rotation counter to zero
# Hint #2: right_wheel.get_degrees_counted() returns the number of degrees counted
# Hint #3: There are 360 degrees in a wheel rotation.
# Hint #4: Change the True to a condition
# Example:
#  follow_line_rotation(10) should make to robot follow the line for 10 rotations of the wheel
def follow_line_rotation(amount):
  while True:
    steering = color_sensor.get_reflected_light() - 50
    motor_pair.start_at_power(35, int(steering))
  motor_pair.stop()
  

# Homework assignment #4 Optional
# Change follow_line from assignment #3 to stop at amount in cm
# Hint #1: There are 360 degrees in a wheel rotation. The circumference of the wheel is 27.63 cm.
# Example:
#   follow_line_cm(100) should make the robot follow the line for 100 cm
def follow_line_cm(amount):
  
# Homework assignment #5 Super Optional
# Change follow_line from assignment #4 to stop at the 
#   next perpendicular black line after the amount in cm has been reached
# Example:
#   follow_line(100) should make the robot follow the line for 100 cm,
#     and then keep going until the left light sensor senses a black line
def follow_line(amount):

