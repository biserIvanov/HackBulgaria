import unittest

from hero import Hero
from orc import Orc
from entity import Entity
from weaphon import Weaphon
from fight import Fight
from dungeon import Dungeon


class Hero_tests(unittest.TestCase):

    def setUp(self):
        self.entity = Entity("Gosho", 100)
        self.bron_hero = Hero("Ivan", 100, "Magician")
        self.bron_orc = Orc("Pesho", 100, 1.40)

    def test_initialisation(self):
        self.assertEqual(self.bron_hero.name, "Ivan")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickName, "Magician")

    def test_known_as(self):
        self.assertEqual("Ivan the Magician", self.bron_hero.known_as())

    def test_get_health(self):
        self.assertEqual(100, self.bron_hero.get_health())

    def test_is_alive_with_max_health(self):
        self.bron_hero.health -= 100
        self.assertFalse(self.bron_hero.is_alive())

    def test_is_alive_when_hit(self):
        self.bron_hero.health += 20
        self.assertTrue(self.bron_hero.is_alive())

    def test_take_dmg(self):
        self.bron_hero.take_dmg(80)
        self.assertEqual(20, self.bron_hero.health)

    def test_take_more_dmg_than_health(self):
        self.bron_hero.take_dmg(120)
        self.assertEqual(0, self.bron_hero.health)

    def test_take_healing_on_dead_hero(self):
        self.bron_hero.take_dmg(120)
        self.assertFalse(self.bron_hero.take_healing(20))

    def test_take_more_healing_than_the_max_health(self):
        self.bron_hero.take_dmg(50)
        self.bron_hero.take_healing(100)
        self.assertEqual(100, self.bron_hero.health)

    def test_take_successful_heal(self):
        self.bron_hero.take_dmg(20)
        self.assertTrue(self.bron_hero.take_healing(40))

    def test_Orc_initialization(self):
        self.assertEqual(self.bron_orc.name, "Pesho")
        self.assertEqual(self.bron_orc.health, 100)
        self.assertEqual(self.bron_orc.berserk_factor, 1.40)

    def test_Orc_initialization2(self):
        self.bron_orc_big = Orc("Pesho", 100, 2.40)
        self.assertEqual(self.bron_orc_big.berserk_factor, 2)

    def test_Orc_initialization3(self):
        self.bron_orc_small = Orc("Pesho", 100, 0.40)
        self.assertEqual(self.bron_orc_small.berserk_factor, 1)

    def test_Orc_get_healt(self):
        self.assertEqual(self.bron_orc.get_health(), 100)

    def test_if_orc_is_alive_when_created(self):
        self.assertTrue(self.bron_orc.is_alive())

    def test_if_orc_is_alive_when_hit(self):
        self.bron_orc.health -= 30
        self.assertTrue(self.bron_orc.is_alive())

    def test_orc_take_dmg(self):
        self.bron_orc.take_dmg(30)
        self.assertEqual(70, self.bron_orc.get_health())

    def test_orc_take_more_dmg(self):
        self.bron_orc.take_dmg(110)
        self.assertEqual(0, self.bron_orc.get_health())

    def test_take_normal_heal(self):
        self.bron_orc.take_dmg(50)
        self.bron_orc.take_healing(40)
        self.assertEqual(90, self.bron_orc.health)

    def test_take_overload_heal(self):
        self.bron_orc.take_dmg(50)
        self.bron_orc.take_healing(100)
        self.assertEqual(100, self.bron_orc.health)


class WeaphonTest(unittest.TestCase):

    def setUp(self):
        self.sniper = Weaphon("Gun", 85, 0.10)
        self.hammer = Weaphon("One-Hand", 30, 0)
        self.bron_orc = Orc("Pesho", 100, 1.50)
        self.bron_hero = Hero("Ivan", 100, "Magician")

    def test_weaphon_initialization(self):
        self.assertEquals("Gun", self.sniper.type)
        self.assertEquals(85, self.sniper.damage)
        self.assertEquals(0.10, self.sniper.critical_strike_percent)

    def test_crit_hit_sniper(self):
        temp = False
        for i in range(100):
            if temp:
                break
            else:
                temp = self.sniper.critical_hit()
        self.assertTrue(temp)

    def test_crit_hit_hammer(self):
        temp = False
        for i in range(100):
            if temp:
                break
            else:
                temp = self.hammer.critical_hit()
        self.assertFalse(temp)

    def test_entity_has_weaphon(self):
        self.bron_orc.equip_weapon(self.hammer)
        self.assertTrue(self.bron_orc.has_weaphon())

    def test_entity_do_not_has_wep(self):
        self.assertFalse(self.bron_orc.has_weaphon())

    def test_entity_equip_weaphon_first_time(self):
        self.bron_orc.equip_weapon(self.hammer)
        self.assertEqual("One-Hand", self.bron_orc.weaphon.type)

    def test_equip_weaphon_when_the_entity_allready_has_one(self):
        self.bron_orc.equip_weapon(self.hammer)
        self.bron_orc.equip_weapon(self.sniper)
        self.assertEqual("Gun", self.bron_orc.weaphon.type)

    def test_attack_no_weaphon(self):
        self.assertEqual(0, self.bron_orc.attack())

    def test_atack_hero(self):
        self.bron_hero.equip_weapon(self.hammer)
        self.assertEqual(30, self.bron_hero.attack())

    def test_atack_orc(self):
        self.bron_orc.equip_weapon(self.hammer)
        self.assertEqual(45, self.bron_orc.attack())


class fightTest(unittest.TestCase):

    def setUp(self):
        self.sniper = Weaphon("Gun", 85, 0.10)
        self.hammer = Weaphon("One-Hand", 30, 0)

        self.bron_orc = Orc("Pesho", 100, 1.50)
        self.bron_hero = Hero("Ivan", 100, "Magician")

    def test_fight(self):
        self.bron_orc.equip_weapon(self.hammer)
        self.bron_hero.equip_weapon(self.sniper)
        self.fight1 = Fight(self.bron_hero, self.bron_orc)
        print
        self.assertEqual(1, self.fight1.simulate_fight())
        print("__________________________________________________________")

    def test_fight2(self):
        self.bron_orc.equip_weapon(self.sniper)
        self.bron_hero.equip_weapon(self.hammer)
        self.fight1 = Fight(self.bron_hero, self.bron_orc)
        self.assertEqual(2, self.fight1.simulate_fight())


class Dungeon_Test(unittest.TestCase):

    def setUp(self):
        self.sniper = Weaphon("Gun", 85, 0.10)
        self.hammer = Weaphon("One-Hand", 30, 0)

        self.bron_orc = Orc("Pesho", 100, 1.50)
        self.bron_hero = Hero("Ivan", 100, "Magician")

        self.bron_orc.equip_weapon(self.hammer)
        self.bron_hero.equip_weapon(self.sniper)
        self.magura = Dungeon("/home/biser/TDD/simple_dungeon.txt")

    def tearDown(self):
        f1 = open("/home/biser/TDD/simple_dungeon.txt", 'w+')
        a = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S\n"
        self.magura.lst = []
        f1.write(a)

    def test_constructor(self):
        self.assertEqual(
            "/home/biser/TDD/simple_dungeon.txt", self.magura.path)

    def test_print_map(self):
        a = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S\n"
        self.assertEqual(a, self.magura.print_map())

    def test_spawn_first_entity(self):
        self.magura.spown("Ivan", self.bron_hero)
        f1 = open("/home/biser/TDD/simple_dungeon.txt", 'r')
        first_spowning_point = f1.readline()[0]
        f1.close()
        self.assertEqual(first_spowning_point, "H")

    def test_spawn_wrong_object_as_argument(self):
        self.magura.spown("Ivan", self.sniper)
        self.assertEqual(
            "wrong instance given", self.magura.spown("Ivan", self.sniper))

    def test_spawn_second_entity(self):
        temp = ""
        self.magura.spown("Ivan", self.bron_hero)
        self.magura.spown("Ivan", self.bron_orc)
        f1 = open("/home/biser/TDD/simple_dungeon.txt", 'r')
        print
        for line in f1:
            temp = line
        temp = temp[len(temp)-2:]
        self.assertEqual("O\n", temp)

    def test_spawn_one_more_than_the_map_can_handle(self):
        self.magura.spown("Ivan", self.bron_hero)
        self.magura.spown("Gosho", self.bron_orc)
        self.assertEqual("currently there is no free spowning point", self.magura.spown("Pesho", self.bron_orc))

    def test_entity_move(self):
        self.magura.spown("Ivan", self.bron_hero)
        self.magura.move("Ivan", "right")
        f1 = open("/home/biser/TDD/simple_dungeon.txt", 'r')
        first_spowning_point = f1.readline()[1]
        f1.close()
        self.assertEqual(first_spowning_point, "H")

    def test_entity_move_through_wall(self):
        pass
        self.magura.spown("Ivan", self.bron_hero)
        self.magura.move("Ivan", "right")
        self.assertFalse(self.magura.move("Ivan", "right"))

    def test_move_outside_the_map(self):
        pass
        self.magura.spown("Ivan", self.bron_hero)
        self.assertFalse(self.magura.move("Ivan", "left"))

if __name__ == '__main__':
    unittest.main()
