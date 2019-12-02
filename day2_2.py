#!/usr/bin/python
import os
import re
import sys
#import urllib
#import requests
import math

PARAM1 = 1
PARAM2 = 2
PARAM3 = 3
NEXT = 4

def intcode_computer(intcode_list):
    pointer = 0
    
    while pointer <  len(intcode_list):
        opcode = intcode_list[pointer]

        if(opcode == 99):
            print str(pointer) + ': halt'
            break
        
        address_p1 = pointer + PARAM1
        address_p2 = pointer + PARAM2
        address_p3 = pointer + PARAM3

        val_p1 = intcode_list[address_p1]
        val_p2 = intcode_list[address_p2]
        val_p3 = intcode_list[address_p3]

        if(opcode == 1):
            print str(pointer) + ': processing addition'
            
            opcode_result = intcode_list[val_p1] + intcode_list[val_p2]

            print str(pointer) + ': replacing position ' + str(val_p3) + ' with ' + str(opcode_result)
            intcode_list[val_p3] = opcode_result

            pointer = pointer + NEXT

        elif(opcode == 2):
            print str(pointer) + ': processing multiplication'

            opcode_result = intcode_list[val_p1] * intcode_list[val_p2]

            print str(pointer) + ': replacing position ' + str(val_p3) + ' with ' + str(opcode_result)
            intcode_list[val_p3] = opcode_result

            pointer = pointer + NEXT



        else:
            print str(pointer) + ': invalid opcode'
            sys.exit(0)


def run_program(instructions, noun, verb):
    tmp_instructions = list(instructions)
    tmp_instructions[1] = noun
    tmp_instructions[2] = verb
    intcode_computer(tmp_instructions)
    return tmp_instructions[0]
    
            
def main():
    f = open('day2.txt','r')
    # get input from file
    ins_raw = f.read()
    #break into list of strings
    ins_slist = ins_raw.rstrip().split(',')
    #convert into list of ints
    ins_list = map(int, ins_slist)
    
    print 'ORIGINAL STATE'
    print ins_list
    

#    print '1202 PROGRAM ALARM STATE'
#    print run_program(ins_list, 12, 2)
    print 'Looking for 19690720'
    print run_program(ins_list, 22, 54)
    


if __name__ == '__main__':
  main()



