# My first class

import math  # need this for .distanceFrom method


# Every class should have a detailed comment.

# Every method should have a detailed comment.

# There should also be other comments.

# Suppose we didn't have a GraphWin package that defined a Point for us.
# In that case, we'd need to write our own classes!  Here is a start for
# a Point class. (Note that we are NOT importing GraphWin for this!)
class Point:

    # Constructor method
    # Create a point like this:
    # p = Point(3.14159, 10.0) where x and y are float type
    # They are stored internally as p.__x and p.__y (private!)
    def __init__(self, x, y):
        self.__x = x  # assigns object passed to x to object
        self.__y = y  # do same for y

    # The p.__str__() method is called automatically by print:
    # print(p)
    # Returns the state of the object as ONE string (concat!)
    def __str__(self):
        message = 'Point at: ('
        message += str(self.__x)  # MUST convert numbers to str!
        message += ', '
        message += str(self.__y)
        message += ') '
        return message

    # This is a called a copy constructor
    # Not discussed in the book
    # We need p.copy() since user-defined objects are mutable
    def copy(self):
        newPoint = Point(self.__x, self.__y)
        return newPoint  # this is the usual pattern

    # Accessor method ("getter") returns x coord.
    def getX(self):
        return self.__x

    # Accessor method ("getter") returns y coord.
    def getY(self):
        return self.__y

    # Mutator method ("setter") modifies both x and y
    # Note: we could have separate setX and setY too
    def move(self, dx, dy):
        self.__x = self.__x + dx
        self.__y += dy

    # Computes and returns Euclidean (crows-fly) distance
    # Uses Pythagorean theorem from high school math
    # Takes self and returns the distance as a float
    # This is not a mutator or accessor--just another method
    # p1 = Point(0, 0)
    # p2 = Point(3, 4)
    # d = distanceFrom(p2) # evaluates to 5.0
    def distanceFrom(self, otherPoint):
        dx = self.__x - otherPoint.__x  # X distance
        dy = self.__y - otherPoint.__y  # Y dist (sign doesn't matter)
        d = math.sqrt(dx ** 2 + dy ** 2)  # take square root of sum
        return d

        # This is the end of our class defition


# You still need a main() function
# You may also need other functions
def main():
    p1 = Point(0, 0)  # Create a point at the origin
    # p2 = Point(3, 4)
    p2 = p1.copy()  # Make a copy of the point: NOT p2 = p1 (why?)
    p2.move(3, 4)  # move the second point 3 units right and 4 up
    print(p1, p2)  # This implicitly calls the __str__() method
    d = p1.distanceFrom(p2)  # returns Euclidean distance
    print('Distance:', d)

    # Earlier code we wrote:
    # print(p1, p2)


##    print('You created a point!')
##    print('X coord at', p.getX())
##    print('Y coord at', p.getY())
##    p.move(-10, 0)
##    print('You moved a point!')
##    print('X coord at', p.getX())
##    print('Y coord at', p.getY())

main()
