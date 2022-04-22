def is_triangle(sides):
    if 0 not in sides and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
            return True
    return False

def equilateral(sides):
    if is_triangle(sides):
        if sides[0] == sides[1]:
            if sides[1] == sides[2]:
                if sides[0] == sides[2]:
                    return True
    return False
# alt oneliner: convert list into set, cos values in set are unique, so...
#    return len(set(sides)) == 1

def isosceles(sides):
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
    if is_triangle(sides):
        if equilateral(sides) == isosceles(sides) == False:
            return True
    return False
# alt oneliner for 2nd if: return len(set(sides)) == 3

def degenerate(sides):
    if is_triangle(sides):
        if sides[0] + sides[1] == sides[2] or sides[1] + sides[2] == sides[0] or sides[0] + sides[2] == sides[1]:
            return True
    return False
