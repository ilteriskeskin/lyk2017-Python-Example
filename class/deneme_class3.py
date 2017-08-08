class Nokta:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def topla(self):
        return self.x + self.y

p = Nokta(3, 4)
print(p.x, ",", p.y)
print(p.topla())
