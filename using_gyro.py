from spike import Motor, MotorPair, ColorSensor, PrimeHub

# Define all motor ports
left_motor, right_motor, front_motor, back_motor, left_light, right_light = 'A', 'E', 'D', 'C', 'B', 'F'

# wheel circumference, number of inches traveled for single rotation of the wheel
wheel_distance=11

# Define everything that we're going to use
motor_pair = MotorPair(left_motor, right_motor)
motor_pair.set_motor_rotation(wheel_distance, 'in')
left_motor = Motor(left_motor)
right_motor = Motor(right_motor)
front_motor = Motor(front_motor)
back_motor = Motor(back_motor)
hub = PrimeHub()
gyro = hub.motion_sensor
left_light = ColorSensor(left_light)
right_light = ColorSensor(right_light)

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
    return wheel_distance * average_degrees / 360

def get_angle(angle):
    if angle > 0:
        return (360 + gyro.get_yaw_angle()) % 360
    elif angle < 0:
        return (gyro.get_yaw_angle() - 360) % -360
    else:
        return gyro.get_yaw_angle()


# Rotate the robot. If angle is positive, it rotates to right. If angel is negative, it rotates to left.
def rotate(angle, speed=30):
    # reset angle to 0
    gyro.reset_yaw_angle()
    # if desired angle is positive, rotate right
    if angle > 0:
        # Do while current angle is less than desired angle
        while get_angle(angle) < (angle * .97):
            # start rotate robot to the right at 20% power
            motor_pair.start_at_power(speed, 100)
    # if desired angle is negative, rotate left
    elif angle < 0:
        # Do while current angle is more than the desired angle
        while get_angle(angle) > (angle * .97):
            # start rotate robot to the right at 20% power
            motor_pair.start_at_power(speed, -100)
    motor_pair.stop()

# Follow the left edge of black line using light sensor
def follow_line(inches, side='left', speed=35):
    if side == 'left':
        sensor = left_light
    else:
        sensor = right_light
    reset_odometer()
    while read_odometer() < inches:
        steering = int(sensor.get_reflected_light() - 50)
        motor_pair.start_at_power(speed, steering)
    motor_pair.stop()


# Stop squarely on the black line
def stop_on_line():
    # Start motor_pair at 20% power
    motor_pair.start(0, 20)
    while True:
        left = left_light.get_reflected_light()
        right = right_light.get_reflected_light()
        motor_pair.start((left - right) * 3, 20)
        # If both sensors detect black line, stop and break out of loop
        if left < 40 and right < 40:
            motor_pair.stop()
            break

# Drive foward for designated distance and angle
def drive(inches, angle=0, speed=45):
    rotate(angle)
    reset_odometer()
    if inches > 0:
        while read_odometer() < inches:
            steering = int(angle - get_angle(angle))
            motor_pair.start(steering, speed)
    else:
        while read_odometer() > inches:
            steering = int(get_angle(angle) - angle)
            motor_pair.start(steering, -speed)
    motor_pair.stop()


#rotate(300)

#motor_pair.move(180*1.65, 'degrees', 100, 20)

drive(-40)
drive(-40, 180)

raise SystemExit()
