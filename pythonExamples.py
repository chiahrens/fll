from spike import Motor, MotorPair, ColorSensor, PrimeHub
import time

# Define all motor ports
left_motor, right_motor, front_motor, back_motor, left_light, right_light = 'A', 'E', 'D', 'C', 'B', 'F'

# wheel circumference, number of inches traveled for single rotation of the wheel
wheel_distance=11

# Define everything that we're going to use
engine = MotorPair(left_motor, right_motor)
left_motor = Motor(left_motor)
right_motor = Motor(right_motor)
front_motor = Motor(front_motor)
back_motor = Motor(back_motor)
hub = PrimeHub()
gyro = hub.motion_sensor
gyro.reset_yaw_angle()
left_light = ColorSensor(left_light)
right_light = ColorSensor(right_light)
default_speed = 25

# Resets the odometer to 0
def reset_odometer():
    left_motor.set_degrees_counted(0)
    right_motor.set_degrees_counted(0)

# Read the current odometer. Returns the value in inches.
# We get the average degrees rotated for both wheels. 
# One of the wheel rotations is negative because it is facing the opposite direction.
# We then multiply the average degrees traveled by wheel circumfrace, divide by 360 to get the number of inches traveled
def read_odometer():
    average_degrees = (right_motor.get_degrees_counted() - left_motor.get_degrees_counted())/2
    return abs(wheel_distance * average_degrees / 360)

# Returns the left or right light sensor depending on the value of sensor
def get_light_sensor(sensor):
    if sensor == 'left':
        return left_light
    else:
        return right_light

# Returns the front or back motor depending on the value of motor
def get_motor(motor):
    if motor == 'front':
        return front_motor
    else:
        return back_motor

# Gets the yaw angle, but also adds support for -359 to 359 degrees
def get_angle(turn):
    angle = gyro.get_yaw_angle()
    if turn > 0 and angle < 0:
        angle = 360 + angle
    elif turn < 0 and angle > 0:
        angle = angle - 360
    return angle * 1.03

# Rotates the robot to specified degrees
# If current angle is equal to desired angle, it does nothing
def rotate(degrees, rotation=None, stop=True):
    current = get_angle(degrees)
    if(degrees == current):
        return
    if(rotation == 'right'):
        steering = 100
    elif rotation == 'left':
        steering = -100
    else:
        if(degrees > current):
            steering = 100
        else:
            steering = -100
    print(str(degrees) + ',' + str(current) + ',' + str(steering))
    while degrees != int(current):
        engine.start_at_power(20, steering)
        current = get_angle(degrees)
    if stop == True:
        engine.stop()

def follow_line(distance, sensor='left', edge='left', speed=default_speed, stop=True, turn_factor=1):
    if(edge != 'left'):
        turn_factor = -turn_factor
    light_sensor = get_light_sensor(sensor)
    reset_odometer()
    while read_odometer() < distance:
        steering = int((light_sensor.get_reflected_light() - 50) * turn_factor)
        engine.start_at_power(speed, steering)
    if stop == True:
        engine.stop()

def gyro_move(distance, turn=0, speed=default_speed, rotation=None, stop=True, turn_factor=1, direction='forward'):
    if abs(get_angle(turn) - turn) > 5:
        rotate(turn, rotation)
    reset_odometer()
    if(direction == 'backward'):
        speed = -speed
    while read_odometer() < distance:
        if(direction == 'forward'):
            steering = int((turn - get_angle(turn)) * turn_factor)
        else:
            steering = int((get_angle(turn) - turn) * turn_factor)
        engine.start(steering, speed)
    if stop == True:
        engine.stop()

def forward(distance, turn=0, speed=default_speed, rotation=None, stop=True, turn_factor=1):
    gyro_move(distance, turn, speed, rotation, stop, turn_factor, direction='forward')

def backwards(distance, turn=0, speed=default_speed, rotation=None, stop=True, turn_factor=1):
    gyro_move(distance, turn, speed, rotation, stop, turn_factor, direction='backward')


def lift_arm(degrees, motor='front', power=default_speed):
    motor = get_motor(motor)
    motor.run_for_degrees(degrees, power)

def lower_arm(degrees, motor='front', power=default_speed):
    lift_arm(-degrees, motor, power)

# -------------------- Code Starts Here -------------------------


# follow left edge of black line using right light sensor for 80 inches
follow_line(80, sensor='right')

# follow right edge of black line using right light sensor for 80 inches, tighter turns
follow_line(80, sensor='right', edge='right', turn_factor=1.7)

# follow left edge of black line using left light sensor for 80 inches
follow_line(80)

# follow right edge of black line using left light sensor for 80 inches, tighter turns
follow_line(80, edge='right', turn_factor=2)

# rotate 90 degrees to the right
rotate(90)

# rotate 180 degress to the left
rotate(-180)

# rotate 90 degrees to the right and drive forward 25 inches
forward(25, 90)

# rotate 180 degrees to the left and drive forward 25 inches
forward(25, -180)

# rotate 180 degrees to the right and drive backwards 25 inches
# it is driving backwards while the robot is facing back
backwards(25, 180)

# Exit program
raise SystemExit()
