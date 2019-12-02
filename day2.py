#!/usr/bin/python
import os
import re
import sys
#import urllib
#import requests
import math

IN1 = 1
IN2 = 2
OUT = 3
NEXT = 4

def intcode_computer(intcode_list):
    cursor = 0
    
    while cursor <  len(intcode_list):
        opcode = intcode_list[cursor]

        cursor_in1 = cursor + IN1
        cursor_in2 = cursor + IN2
        cursor_out = cursor + OUT
        
        if(opcode == 1):
            print str(cursor) + ': processing addition'
            pos_in1 = intcode_list[cursor_in1]
            pos_in2 = intcode_list[cursor_in2]
            pos_out = intcode_list[cursor_out]
            opcode_result = intcode_list[pos_in1] + intcode_list[pos_in2]

            print str(cursor) + ': replacing position ' + str(pos_out) + ' with ' + str(opcode_result)
            intcode_list[pos_out] = opcode_result

            cursor = cursor + NEXT

        elif(opcode == 2):
            print str(cursor) + ': processing multiplication'
            pos_in1 = intcode_list[cursor_in1]
            pos_in2 = intcode_list[cursor_in2]
            pos_out = intcode_list[cursor_out]
            opcode_result = intcode_list[pos_in1] * intcode_list[pos_in2]

            print str(cursor) + ': replacing position ' + str(pos_out) + ' with ' + str(opcode_result)
            intcode_list[pos_out] = opcode_result

            cursor = cursor + NEXT


        elif(opcode == 99):
            print str(cursor) + ': halt'
            break
        else:
            print str(cursor) + ': invalid opcode'
            sys.exit(0)


def main():
    f = open('day2.txt','r')
    # get input from file
    intcode_raw = f.read()
    #break into list of strings
    intcode_slist = intcode_raw.rstrip().split(',')
    #convert into list of ints
    intcode_list = map(int, intcode_slist)
    
    print 'ORIGINAL STATE'
    print intcode_list
    
    # reproduce "1202 program alarm"
    intcode_list[1] = 12
    intcode_list[2] = 2

    print '1202 PROGRAM ALARM STATE'
    print intcode_list
    
    intcode_computer(intcode_list)

    print 'OUTPUT'
    print intcode_list

    print 'Position 0 value'
    print intcode_list[0]
        

    


if __name__ == '__main__':
  main()



