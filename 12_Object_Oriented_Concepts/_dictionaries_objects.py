class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def attack(self, pts):
        self.health -= pts


p1 = Player(1, 2)
p2 = Player(3, 4)
p3 = Player(5, 6)

# Internally all the instance attributes are stored in a Instance Dictionary.
# All the methods in the class are stored in Class Dictionary

print(p1.__dict__)
print(p1.__class__.__dict__)
print(Player.__dict__)
