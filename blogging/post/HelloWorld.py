"""This is a hello world example document"""

# imports
import sys
from argparse import ArgumentParser

# constants

# exception classes

# interface functions

# classes

class HelloWorld(object):
    def __init__(self, who):
        self.who = who

    def say_hello(self):
        print ("Hello %s" % self.who)

# internal functions & classes

def main():
    parser = ArgumentParser(description="Say hi")
    parser.add_argument("-w", "--who",
                        type=str,
                        default="world",
                        help="Who to say hello to")
    args = parser.parse_args()

    who = args.who

    greeter = HelloWorld(who)
    greeter.say_hello()

    return 0

# run standalone
if __name__ == '__main__':
    status = main()
    sys.exit(status)
