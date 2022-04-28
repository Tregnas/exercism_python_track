"""
Determine if a triangle is equilateral, isosceles, or scalene.
"""

def is_triangle(sides):
"""
Check is inputed sizes makes triangle at all
"""
    if 0 not in sides and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False

def equilateral(sides):
"""
An equilateral triangle has all three sides the same length.
"""
    if is_triangle(sides):
        if sides[0] == sides[1]:
            if sides[1] == sides[2]:
                if sides[0] == sides[2]:
                    return True
    return False
# alt oneliner: convert list into set, cos values in set are unique, so...
#    return len(set(sides)) == 1

def isosceles(sides):
"""
An isosceles triangle has at least two sides the same length. 
(It is sometimes specified as having exactly two sides the same length, but we'll say at least two.)
"""
    if is_triangle(sides):
        if sides[0] == sides[1]:
            return True
        if sides[1] == sides[2]:
            return True
        if sides[0] == sides[2]:
            return True
    return False
# alt oneliner: return len(set(sides)) < 3

def scalene(sides):
"""
A scalene triangle has all sides of different lengths.
"""
    if is_triangle(sides):
        if equilateral(sides) == isosceles(sides) == False:
            return True
    return False
# alt oneliner for 2nd if: return len(set(sides)) == 3

def degenerate(sides):
"""
The case where the sum of the lengths of two sides equals that of the third is known as a degenerate triangle.
It has zero area and looks like a single line.
"""
    if is_triangle(sides):
        if sides[0] + sides[1] == sides[2] or sides[1] + sides[2] == sides[0] or sides[0] + sides[2] == sides[1]:
            return True
    return False
