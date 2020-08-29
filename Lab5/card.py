from comparable import Comparable


class Card(Comparable):
    """
    This immutable class represents a Comparable playing Card,
    inheriting from the Comparable class,  The private instance
    variables are rank and suit. The number of compares are not kept.

    Here Aces are low and Kings are high
    Only Rank is used for comparison
    Suit: Clubs = 0
          Diamonds = 1
          Hearts = 2
          Spades = 3
    Rank: Ace = 1
          2-10 = 2-10
          Jack = 11
          Queen = 12
          King = 13
    """


    def __init__(self, suit, rank):
        """
        Constructor:
        Initializes rank and suit from the parameters
        """

        super().__init__()
        self.__suit = suit
        self.__rank = rank

    def get_rank(self):
        """
        Return rank
        """

        return self.__rank

    def get_suit(self):
        """
        Return suit
        """

        return self.__suit

    def compare(self, otherCard):
        """
        Compares this card to other by Rank, Aces low
        Returns a positive number if self is greater than otherCard
        Returns a negative number if self is less than otherCard
        Otherwise returns 0, if Cards are equal
        """
        return self.__rank - otherCard.__rank

    def __str__(self):
        """
        Returns a string representation of the Card, as rank-suit
        Use a tuple with string representations of the Suit
        As "C" = Clubs, "D" = Diamonds, "H" = Heats, "S" = Spades
        Use a tuple with string representations of the Rank
        As "A" = Aces, "J" = Jacks, "Q" = Queens, "K" = Kings
        Let the first element of the tuple be None
        Use the rank and suit of the Card as indexes into the tuples
        """
        suits = ("C", "D", "H", "S")
        ranks = (None, "A", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "J", "Q", "K")

        return '{}-{}'.format(ranks[self.__rank],
                              suits[self.__suit])
