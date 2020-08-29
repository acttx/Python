import random
from card import Card


class Deck(list):
    """
    This class represents a Deck of Cards.
    It inherits from list - it is a list
    Cards are added at the end of the list: Use append
    Cards are dealt from the end of the list: Use pop()
    """

    def __init__(self):
        """
        Constructor:
        Calls the list constructor
        """

        super().__init__()

    def initialize(self):
        """
        Initializes the Deck with 52 Cards
          Both the Suits and Ranks are integers
            Suits: 0=Clubs, 1=Diamonds, 2=Hearts, 3=Spades
            Ranks: 1=Ace, 2-10=2=10, 11=Jacks, 12=Queen, 13=King
        """

        for suit in range(4):
            for rank in range(1, 14):
                self.add_card(Card(suit, rank))

    def add_card(self, card):
        """
        Add the Card to the end of the list
        """

        self.append(card)

    def deal(self):
        """
        Removes and returns the last Card in the list
        """
        # first_card = self[0]
        #         # del self[0]
        #         # return first_card
        return self.pop()


    def shuffle(self):
        """
        The random class has a shuffle method
        that accepts a list as an argument
        Return the shuffled Deck
        """

        return random.shuffle(self)

    def __str__(self):
        """
        Returns a string containing the list of Cards
        in the Deck: 13 Cards to a line
        The newline character is added for every 13th Card
        """

        s = []
        for card in self:
            s.append(str(card))
        return "\n".join([" ".join(s[i:i+13]) for i in range(0, len(s), 13)])

