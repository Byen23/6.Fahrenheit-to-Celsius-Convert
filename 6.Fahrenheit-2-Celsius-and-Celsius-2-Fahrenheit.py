# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 06:17:55 2019

@author: Byen23
"""
#6th Program to be uploaded to github.
''' This program converts temperature between Fahrenheit to Celsius,
    and Converts Celsius to Fahrenheight.'''
    
'''Fahrenheit to Celsius formula:

(°F - 32) x 5/9 = °C or in plain english, First subtract 32, then multiply by 5,
then divide by 9.'''

'''Celsius to Fahrenheit formula:

(°C × 9/5) + 32 = °F or in plain English, Multiple by 9, then divide by 5, then
add 32.'''

#Converts Celsius to Fahrenheit
Fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0
print("Temperature:", Fahrenheit,"Fahrenheight =", Celsius,"C")

# Cnverts Fahrenheit to Celsius
Celsius = float(input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32
print("Temperature:", Celsius, "Celsius =", Fahrenheit, "F")
