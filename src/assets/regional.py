#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop
from pybricks.parameters import Color
import time
lever_max = 105
# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
elev_motor = Motor(Port.B)
sonic_sensor = UltrasonicSensor(Port.S4)
gripper_motor = Motor(Port.C)
left_color = ColorSensor(Port.S1)
#right_color = ColorSensor(Port.S4)
#gyro = GyroSensor(Port.S2)
#right_color = Sensor(Port.3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=88, axle_track=104)

def dist_track(x):
    while True: #distance tracking
        dist = sonic_sensor.distance(silent=False)
        print(dist) 
        if dist < x:
            robot.stop()
            break
        else:
            robot.straight(-10)

#while True: #reflection based tracking
#    left = left_color.reflection()
#    right = right_color.reflection()
#    print("left",left)
#    print("right",right)
#    #time.sleep(1)
#    if left <= 60:
#        print("not white")
#        robot.turn(10)
#    if left > 60:
#        print("white")
#        robot.drive(-100,0) 
def wait(): #wait
    time.sleep(1)
    print("Waiting: 1")
    time.sleep(1)
    print("Waiting: 2")
    time.sleep(1)
    print("Waiting: 3")
    time.sleep(1)
    print("Waiting: 4")
    time.sleep(1)
    print("Waiting: 5")
    print(20*"_")


def grip_test(): #grabs smth   
    #elev_motor.run_angle(100,lever_max,Stop.HOLD)
    #wait()
    #robot.straight(-70)
    #wait()
    print("Grip open")
    gripper_motor.run_angle(-100,40)
    wait()
    print("going down")
    elev_motor.run_time(-100,1300,Stop.HOLD)
    gripper_motor.run_time(100,1000)
    print("up..")
    wait()
    elev_motor.run_time(100,1000)
    #wait()
    #robot.straight(-100)




def ref_track(x): #1cm!!
    d = 0
    while d != x: #reflection based tracking
            left = left_color.color()
            #right = right_color.color()
            print("left",left)
            #print("right",right)
            #time.sleep(1)
            if left == Color.BLUE:
                robot.turn(-10)
            elif left == Color.WHITE:
                robot.straight(-10)
                d += 1
            else:
                #robot.drive(-100,0)
                robot.turn(10)


def start_go():
    robot.straight(-460)
    robot.turn(110)
    robot.straight(-400)

def cont():
    grip_test()

# Go forward and backwards for one meter.
#robot.straight(1000)

# Turn clockwise by 360 degrees and back again.
#robot.turn(360)

#print(left_color.reflection())
#right_motor.run(100)
#under_motor.run_time(1000,1000)
#robot.straight(10)
black = 60
def fueling():
    #elev_motor.run_time(100,600,Stop.HOLD)
    time.sleep(2)
    robot.straight(470)
    time.sleep(2)
    robot.straight(-150)
    #left_motor.run_time(-20,600)
    robot.turn(120)
    print("elfordult")

def tank_b():
    robot.straight(470)
    robot.straight(-520)
    robot.turn(-95)
    robot.straight(470)
    robot.turn(30)
    robot.straight(1200)
    robot.straight(-1200)
    robot.turn(-30)
    robot.straight(-470)

def spin():
    while True:
        left = left_color.color()
        robot.turn(2)
        print(left)
        if left == Color.BLUE:
            break

def contain_two():
    robot.straight(350)
    gripper_motor.run_angle(-100,40)
    robot.turn(-60)
    robot.straight(-50)
    robot.turn(-5)
    robot.straight(-15)
    elev_motor.run_time(-100,1300)
    time.sleep(2)
    gripper_motor.run_time(100,1000)
    time.sleep(2)
    elev_motor.run_time(100,1300)
    time.sleep(2)
    robot.turn(100)
    robot.straight(-320)
    elev_motor.run_time(-100,900)
    gripper_motor.run_time(-100,700)

def contain_three():
    robot.turn(-20)
    robot.straight(850)
    gripper_motor.run_angle(-100,40)
    robot.turn(-90)
    ref_track(10)
    dist_track(120)
    robot.turn(10)
    elev_motor.run_time(-100,1300)
    time.sleep(2)
    gripper_motor.run_time(100,1000)
    time.sleep(2)
    elev_motor.run_time(100,1600)
    time.sleep(2)
    robot.straight(400)
    robot.turn(95)
    ref_track(70)
    dist_track(280)
    elev_motor.run_time(-100,900)
    gripper_motor.run_time(-100,700)

def ship_deploy():
    robot.straight(300)
    robot.turn(90)
    robot.straight(400)
    robot.turn(90)
    robot.straight(300)
    robot.turn(90)
    robot.straight(50)
    time.sleep(3)
    robot.turn(-45)
    robot.straight(500)


def final_solution():
    robot.straight(470)
    robot.straight(-250)


def long_way():
    robot.straight(470)
    robot.straight(-250)
    robot.turn(90)
    robot.straight(-1800)
    robot.turn(90)
    robot.straight(-300)


def contain_out():
    fueling()
    ref_track(68) #x = 45.5 y = 39.3
    dist_track(118)
    robot.turn(10)
    grip_test()
    robot.straight(50)
    spin()
    robot.turn(55)
    #robot.turn(115)
    robot.straight(-380)
    #robot.turn(15)
    elev_motor.run_time(-100,900)
    gripper_motor.run_time(-100,700)
    robot.turn(90)
    robot.straight(-500)
    robot.straight(-1800)
    robot.turn(90)
    robot.straight(-300)




    

def start():
    fueling()
    ref_track(68) #x = 45.5 y = 39.3
    dist_track(120)
    robot.turn(10)
    grip_test()
    robot.straight(50)
    spin()
    robot.turn(55)
    #robot.turn(115)
    robot.straight(-380)
    #robot.turn(15)
    elev_motor.run_time(-100,900)
    gripper_motor.run_time(-100,700)
    elev_motor.run_time(100,1100)
    gripper_motor.run_time(100,700)
    contain_two()
    elev_motor.run_time(100,1100)
    gripper_motor.run_time(100,700)
    contain_three()
    ship_deploy()

def plan_b():
    tank_b()


def start_debug():
    try:
        start()
    except:
        ev3.speaker.beep(500,100)

def color_test():
    while True:
        print(left_color.color())



#+ bal
#- jobb fokoknál
long_way()
