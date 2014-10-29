from entity import Entity


class Hero(Entity):

    def __init__(self, name, health, nickName):
        super(Hero, self).__init__(name, health)
        self.nickName = nickName
        self.maxHealth = health

    def known_as(self):
        return self.name + " the " + self.nickName
