class CashDesk(object):
    money = []

    def __init__(self):
        self.money = [[100, 0], [50, 0], [20, 0], [10, 0],
                      [5, 0], [2, 0], [1, 0]]

    def take_money(self, amount):
        for key in amount:
            for i in range(len(self.money)):
                if self.money[i][0] == key:
                    self.money[i][1] += amount[key]
        print (self.money)

    def total(self):
        result = 0
        for i in range(len(self.money)):
            if self.money[i][1] > 0:
                result += self.money[i][0]*self.money[i][1]
        print (result)

    def can_withdraw_money(self, amount):
        a = self.money
        for i in range(len(self.money)):
            while True:
                if self.money[i][0] <= amount and self.money[i][1] > 0:
                    amount -= self.money[i][0]
                    self.money[i][1] -= 1
                    if amount == 0:
                        return True
                elif self.money[i][0] == 1:
                    return False
                else:
                    break
        self.money = a


my_cash_desk = CashDesk()
my_cash_desk.take_money({1: 2, 50: 1, 20: 1})
my_cash_desk.total()
print (my_cash_desk.can_withdraw_money(53))
