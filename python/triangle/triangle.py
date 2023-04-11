def is_triangle_valid(sides):
    """
    Check for triangle inequality
    """
    return sides[0] + sides[1] > sides[2] and sides[1] + sides[2] > sides[0] and sides[0] + sides[2] > sides[1]


def equilateral(sides):
    if sum(sides) > 0:
        return len(set(sides)) <= 1
    return False


def isosceles(sides):
    if is_triangle_valid(sides):
        duplicates = set([x for x in sides if sides.count(x) > 1])
        if len(duplicates) >= 1:
            return True
        return False
    return False

def scalene(sides):
    if is_triangle_valid(sides):
        return len(set(sides)) == 3
    return False

# print(equilateral([2, 2, 2]))
# print(equilateral([0, 0, 0]))
# print("1")
# print(isosceles([3, 1, 1]))
# print("2")
# print(isosceles([2, 3, 4]))
# print("3")
# print(isosceles([3, 4, 4]))
# print(scalene([5, 4, 6]))
# print(scalene([4, 4, 4]))
# print(scalene([7, 3, 2]))
