#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py

def triangle(a, b, c):	
	
	# Basic rule of any triange: The sum of the lengths of any two 
	# sides of a triangle always exceeds the length of the third side.
	ab = a + b
	ac = a + c
	bc = b + c
	try:
		if (ab > c) & (ac > b) & (bc > a):		
			if(a == b) & (a == c): 
				result = 'equilateral'
			elif (a == b) | (a == c) | (b == c):
				result = 'isosceles'
			else:
				result = 'scalene'
		else:
			raise Exception()
	except:
		raise TriangleError()
	else:
		return result

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
