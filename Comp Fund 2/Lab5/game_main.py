import sys
from broker import Broker

"""
This game is played from the Broker class
This main method constructs a Broker object and calls its methods 
"""


def main():
    rounds = 1000
    broker = Broker(rounds)
    broker.setup()
    broker.play()
    broker.display_results()


main()
