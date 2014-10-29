from entity import Entity


class Orc(Entity):

    def __init__(self, name, health, berserk_factor):
        super(Orc, self).__init__(name, health)
        self.maxHealth = health
        if berserk_factor > 2:
            self.berserk_factor = 2
        elif berserk_factor < 1:
            self.berserk_factor = 1
        else:
            self.berserk_factor = berserk_factor

    def attack(self):
        return self.weaphon.damage*self.berserk_factor
