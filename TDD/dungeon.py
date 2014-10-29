from hero import Hero
from orc import Orc
from entity import Entity
from weaphon import Weaphon
from fight import Fight
from dungeon import Dungeon


class Dungeon(object):

    def __init__(self, path):
        self.path = path
        self.dct = {}

    def print_map(self):
        a = ''
        f1 = open('/home/biser/TDD/simple_dungeon.txt', 'r')
        for line in f1:
            a += line
        f1.close()
        #print(a)
        return a

    def spown(self, player_name, entity):
        a = ""
        if isinstance(entity, Hero) or isinstance(entity, Orc):
            f1 = open('/home/biser/TDD/simple_dungeon.txt', 'r')
            for line in f1:
                a += line
            for i in range(len(a)):
                if a[i] == 'S' and isinstance(entity, Hero):
                    #spawn Hero
                    a = a[:i] + "H" + a[i+1:]
                    f2 = open('/home/biser/TDD/simple_dungeon.txt', 'w')
                    f2.write(a)
                    self.dct[entity] = entity.name
                    f2.close()
                    f1.close()
                    break
                elif a[i] == 'S' and isinstance(entity, Orc):
                    #spown Orc
                    a = a[:i] + "O" + a[i+1:]
                    f2 = open('/home/biser/TDD/simple_dungeon.txt', 'w')
                    f2.write(a)
                    self.dct[entity] = entity.name
                    f2.close()
                    f1.close()
                    break
                elif i == len(a)-1:
                    f1.close()
                    return ("currently there is no free spowning point")
        else:
            return ("wrong instance given")

    def move(self, player_name, direction):
        exceptFlag = False
        for player in self.dct:
            print(player.name)

            if player.name == player_name:
                if isinstance(player, Hero):
                    a = ''
                    f1 = open('/home/biser/TDD/simple_dungeon.txt', 'r+')
                    a = f1.read()
                    f1.close()
                    for i in range(len(a)):
                        if a[i] == "H":
                            if direction == "left":
                                try:
                                    if a[i-1] == ".":
                                        a = a[:i-1] + "H" + "." + a[i+1:]
                                    elif a[i-1] == "O":
                                        self.fight1 = Fight(self.dct[0], self.dct[1])
                                        if self.fight1.simulate_fight() == 1:
                                            a = a[:i-1] + "H" + "." + a[i+1:]
                                        else:
                                            a = a[:i-1] + "O" + "." + a[i+1:]
                                except:
                                    exceptFlag = True #!!! if excep....
                                f1 = open('/home/biser/TDD/simple_dungeon.txt', 'w+')
                                f1.write(a)
                                f1.close()
                                print(a)
                                break
                            elif direction == "right":
                                try:
                                    if a[i+1] == ".":
                                        a = a[:i] + "." + "H" + a[i+2:]
                                    elif a[i+1] == "O":
                                        self.fight1 = Fight(self.dct[0], self.dct[1])
                                        if self.fight1.simulate_fight() == 1:
                                            a = a[:i] + "." + "H" + a[i+2:]
                                        else:
                                            a = a[:i] + "." + "O" + a[i+2:]
                                except:
                                    pass
                                f1 = open('/home/biser/TDD/simple_dungeon.txt', 'w+')
                                f1.write(a)
                                f1.close()
                                print(a)
                                break
                            elif direction == "up":
                                try:
                                    if a[i-11] == ".":
                                        a = a[:i-11] + "H" + a[i-10:i] + "." + a[i+1:]
                                except:
                                    pass
                                f1 = open('/home/biser/TDD/simple_dungeon.txt', 'w+')
                                f1.write(a)
                                f1.close()
                                print(a)
                                break
                            elif direction == "down":
                                try:
                                    if a[i+11] == ".":
                                        a = a[:i] + "." + a[i+1:i+11] + "H" + a[i+12:]
                                    elif a[i+11] == "O":
                                        aaa = self.dct.keys()
                                        self.fight1 = Fight(aaa[0], aaa[1])
                                        if self.fight1.simulate_fight() == 1:
                                            a = a[:i] + "." + a[i+1:i+11] + "H" + a[i+12:]
                                        else:
                                            a = a[:i] + "." + a[i+1:i+11] + "" + a[i+12:]
                                except:
                                    pass
                                f1 = open('/home/biser/TDD/simple_dungeon.txt', 'w+')
                                f1.write(a)
                                f1.close()
                                print(a)
                                break

#it only works when the human moves but the rest is copy and paste
def main():
    sniper = Weaphon("Gun", 85, 0.10)
    hammer = Weaphon("One-Hand", 30, 0)

    bron_orc = Orc("Pesho", 100, 1.50)
    bron_hero = Hero("Ivan", 100, "Magician")

    bron_orc.equip_weapon(hammer)
    bron_hero.equip_weapon(sniper)
    magura = Dungeon("/home/biser/TDD/simple_dungeon.txt")

    magura.spown("Ivan", bron_hero)
    magura.spown("Pesho", bron_orc)
    magura.move("Ivan", "right")
    magura.move("Ivan", "down")
    magura.move("Ivan", "down")
    magura.move("Ivan", "down")
    magura.move("Ivan", "right")
    magura.move("Ivan", "right")
    magura.move("Ivan", "right")
    magura.move("Ivan", "right")
    magura.move("Ivan", "up")
    magura.move("Ivan", "up")
    magura.move("Ivan", "up")
    magura.move("Ivan", "right")
    magura.move("Ivan", "right")
    magura.move("Ivan", "right")
    magura.move("Ivan", "right")
    magura.move("Ivan", "down")
    magura.move("Ivan", "down")
    magura.move("Ivan", "down")
    magura.move("Ivan", "down")
    f1 = open("/home/biser/TDD/simple_dungeon.txt", 'r')
    first_spowning_point = f1.readline()[1]
    print(first_spowning_point)
    f1.close()


if __name__ == '__main__':
    main()
