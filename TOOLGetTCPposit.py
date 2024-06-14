# -*- coding: utf-8 -*-
import sys
import os
import time

# Add the directory containing lib64 to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib64'))

from lib64 import jkrc
PI = 3.1415926

robot = jkrc.RC("192.168.0.77")
ret = robot.login()
ret = robot.get_tcp_position()
if ret[0] == 0:
    print("the tcp position is :", ret[1])
else:
    print("some things happened, the errcode is: ", ret[0])
robot.logout()