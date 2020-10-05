%%sim_magic -x 100 -y 500 -a 0 -p -C
from ev3dev2.motor import MoveTank, SpeedPercent, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import GyroSensor

# Sequential program with gyro turn

tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

time_1s = 1

# Set the left and right motors in a forward direction
# and run for 1 second
tank_drive.on_for_seconds(SpeedPercent(50), SpeedPercent(50),
                          time_1s)


gyro = GyroSensor(INPUT_4)

target_angle = gyro.angle + 90
tank_drive.on(SpeedPercent(50), SpeedPercent(-50))
while gyro.angle < target_angle:
    pass