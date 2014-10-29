import random


class Weaphon(object):

    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        rand = random.uniform(0.01, 0.99)
        if rand <= self.critical_strike_percent:
            return True
        else:
            return False
