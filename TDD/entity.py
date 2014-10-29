from weaphon import Weaphon


class Entity(object):

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weaphon = Weaphon("none", 0, 0)

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def take_dmg(self, amount):
        if amount > self.health:
            self.health = 0
        else:
            self.health -= amount

    def take_healing(self, healing_points):
        if self.is_alive():
            if self.health + healing_points > self.maxHealth:
                self.health = self.maxHealth
            else:
                self.health += healing_points
            return True
        else:
            return False

    def equip_weapon(self, weapon):
        if isinstance(weapon, Weaphon):
            self.weaphon.type = weapon.type
            self.weaphon.damage = weapon.damage
            self.weaphon.critical_strike_percent = weapon.critical_strike_percent

    def has_weaphon(self):
        if self.weaphon.type != "none":
            return True
        else:
            return False

    def attack(self):
        return self.weaphon.damage
