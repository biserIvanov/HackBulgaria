class Product(object):
    objects = []

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price
        Product.objects.append(self)

    def profit(self):
        profit = self.final_price - self.stock_price
        #print (profit)
        return profit


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super(Laptop, self).__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price,
                 display_size, mega_pixels):
        super(Smartphone, self).__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store(object):
    products = {}
    sold = {}

    def __init__(self, name):
        self.name = name

    def load_new_products(self, product, count):
        if isinstance(product, Product):
            self.products[product] = count

    def list_products(self, product_class):
        for key in Store.products:
            if isinstance(key, product_class):
                print(key.name + " " + str(Store.products[key]))

    def sell_product(self, product):
        if self.products[product] > 0:
            self.products[product] -= 1
            if product in self.sold:
                self.sold[product] += 1
            else:
                self.sold[product] = 1
            return True
        else:
            return False

    def total_income(self):
        total = 0
        for key in self.sold:
            total += key.profit()*self.sold[key]
        print(total)


laptop = Laptop("HP Note Book", 1000, 1300, 1000, 4)
smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)

Emag = Store('Laptop.bg')
Emag.load_new_products(smarthphone, 2)
Emag.load_new_products(laptop, 10)
Emag.list_products(Laptop)
print(Emag.sell_product(smarthphone))
print(Emag.sell_product(smarthphone))
print(Emag.sell_product(smarthphone))
Emag.total_income()
