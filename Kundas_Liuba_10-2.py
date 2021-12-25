from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def expense_tissues(self):
        pass

    @property
    def mean(self):
        return f"{self.volume}"

class Coat(Clothes):
    def __init__(self, v):
        self.volume = v

    def expense_tissues(self):
        result = int(self.volume)/6.5 + 0.5
        print(round(float(result), 2))

class Suit(Clothes):

    def __init__(self, h):
        self.height = h

    def expense_tissues(self):
        result = int(self.height) * 2 + 0.3
        print(round(float(result), 2))

coat_1 = Coat(42)
coat_1.expense_tissues()
suit_1 = Suit(170)
suit_1.expense_tissues()
print(coat_1.mean)
