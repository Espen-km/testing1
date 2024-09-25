# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:36:18 2024

@author: Espen Kalvatn Morten
"""


def argmax(values):
    maxValue = values[0]
    maxValuePosition = 0
    
    for i, value in enumerate(values):
        if value > maxValue:
            maxValue = value
            maxValuePosition = i
    return maxValue, maxValuePosition

ask = int(input("How many numbers do you wish to add?:  "))
#if ask < -1:
inputValues = []

for u in range(ask):
        number = input('Enter number:  ')
        if number.isdigit():
            inputValues.append(int(number))
            # print(inputValues)
        else: 
            print('Please enter only integers')
            #print(max(inputValues))
            
#else: print('You need to enter at least 2 numbers!')


    
    #inputValues = input('Input numbers as list: ')
    #inputValues = [2, 3, -1, 7, 4]
mValue, mValuePos = argmax(inputValues) 


print(f'The highest value was: {mValue} with the index: {mValuePos}')



#if mValue == values [0]:
    #print('Cannot handle empty list')
          
#else:
   # print(mValue, mValuePos)
