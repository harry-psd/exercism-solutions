def equilateral(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b >= c and b + c >= a and c + a >= b:
        return a == b and b == c and c == a
    return False
        
    


def isosceles(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b >= c and b + c >= a and c + a >= b:
        return a == b or b == c or c == a
    return False


def scalene(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b >= c and b + c >= a and c + a >= b:
        return a != b and b != c and c != a
    return False
