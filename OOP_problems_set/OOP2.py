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
print(my_cash_desk.can_withdraw_money(53))


class Fraction(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiply(self):
        return self.a*self.b

    def devide(self):
        return self.a/self.b


class Emplyee(object):

    def __init__(self, fname):
        self.fname = fname

    def getName(self):
        return self.fname


class HourlyEmployee(Emplyee):

    def __init__(self, fname, hourly_wage):
        super(HourlyEmployee, self).__init__(fname)
        self.hourly_wage = hourly_wage

    def weeklyPay(self, hours):
        if hours <= 40:
            return hours*self.hourly_wage
        else:
            return hours*self.hourly_wage*1.5


class SalariedEmployee(Emplyee):

    def __init__(self, fname, salary):
        super(SalariedEmployee, self).__init__(fname)
        self.salary = salary

    def weeklyPay(self, hours):
        if hours <= 40:
            return self.salary


class Manager(SalariedEmployee):

    def __init__(self, fname, salary, bonus):
        super(Manager, self).__init__(fname, salary)
        self.bonus = bonus

    def weeklyPay(self, hours):
        if hours <= 40:
            return self.salary + self.bonus


staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print("Salary: %.2f" % pay)
