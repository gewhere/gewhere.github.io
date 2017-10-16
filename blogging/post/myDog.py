"""This is a class definition example document"""

# imports
import sys
from argparse import ArgumentParser

# constants

# exception classes

# interface functions

# classes

class Dog(object):

    kind = 'canine'           # class variable shared by all instances

    def __init__(self, name):
        self.name = name      # instance variable unique to each instance
        self.tricks = []      # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

    def print_dog(self, name, tricks):
        print("Name: {}".format(self.name))
        print("Tricks: {}".format(self.tricks))

# internal functions & classes

def main():
    parser = ArgumentParser(description="A class for dogs")
    parser.add_argument("-n", "--name",
                        type=str,
                        default="Rocky",
                        help="Name of the dog")
    parser.add_argument("-t", "--tricks",
                        type=str,
                        help="Dog's learned tricks")

    args = parser.parse_args()

    name = args.name
    tricks = args.tricks

    puppy = Dog(name)
    puppy.add_trick(tricks)
    puppy.print_dog(name, tricks)

    return 0

# run standalone
if __name__ == '__main__':
    status = main()
    sys.exit(status)
