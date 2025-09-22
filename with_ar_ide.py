import serial
import time

# Set up the serial connection to the Arduino
ser = serial.Serial('COM5', 115200)  # Update 'COM3' to the correct port for your system
time.sleep(2)  # Wait for the connection to initialize

# Function to set the speed of a stepper motor
def set_speed(motor, speed):
    command = f"{motor}S{speed}\n"
    ser.write(command.encode())
    # time.sleep(0.1)  # Short delay to ensure command is processed

# Function to move a stepper motor a certain number of steps
def move_steps(motor, steps):
    command = f"{motor}M{steps}\n"
    ser.write(command.encode())
    # time.sleep(0.1)  # Short delay to ensure command is processed

# Example usage
a = input("do you want to proceed")
set_speed('1', 1000)  # Set speed to 200 for motor 1 (adjust as needed)
move_steps('1', 100)  # Move 1000 steps forward for motor 1
time.sleep(2)
move_steps('1', -100)  # Move 1000 steps backward for motor 1

set_speed('2', 200)  # Set speed to 200 for motor 2 (adjust as needed)
move_steps('2', 100)  # Move 1000 steps forward for motor 2
time.sleep(2)
move_steps('2', -100)  # Move 1000 steps backward for motor 2

# set_speed('3', 200)  # Set speed to 200 for motor 3 (adjust as needed)
# move_steps('3', 1000)  # Move 1000 steps forward for motor 3
# time.sleep(2)
# move_steps('3', -1000)  # Move 1000 steps backward for motor 3

ser.close()
