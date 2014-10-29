from hero import Hero
from orc import Orc
import random


class Fight(object):

    def __init__(self, hero, orc):
        if isinstance(hero, Hero) and isinstance(orc, Orc):
            self.hero = hero
            self.orc = orc

    def simulate_fight(self):
        flag1 = False
        temp = random.uniform(0, 100)
        if temp > 50:
            flag1 = True
        while self.hero.is_alive() and self.orc.is_alive():
            if not flag1:
                self.orc.health -= self.hero.attack()
                flag1 = True
                print("the hero attacked the orc and coused him " +
                      str(self.hero.attack()) + " damage")
            else:
                self.hero.health -= self.orc.attack()
                flag1 = False
                print("the orc attacked the hero and coused him " +
                      str(self.orc.attack()) + " damage")
        if flag1:
            print("the human KILLED the orc at " +
                  str(self.hero.health) + " health")
            return 1
        else:
            print("the orc KILLED the hero at " +
                  str(self.orc.health) + " health")
            return 2
