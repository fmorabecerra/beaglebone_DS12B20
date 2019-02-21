#!/usr/bin/env python

w1="/sys/bus/w1/devices/28-0315a1d2e6ff/w1_slave"

raw = open(w1, "r").read()
temp_C = float(raw.split("t=")[-1])/1000
print "Temperature is "+str(temp_C)+"C degrees"
temp_F = temp_C*9/5+32
print "Temperature is "+str(temp_F)+"F degrees"
