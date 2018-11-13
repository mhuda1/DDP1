
# class untuk setiap customer

class CustomerCart():

    def __init__(self, name):
        self.name = name
        self.barang = []
    #untuk membeli barang
    def buyGoods(self, product):
        self.product = product
        self.barang.append(product)
        return '{} bought by {}'.format(product.name, self.name)

    # untuk total harga
    def totalingPrice(self):
        total = 0
        for i in self.barang:
            total += i.price
        return 'Total for {} : {} ({})'.format(self.name, total, len(self.barang))
# class untuk semua goods
class Goods():
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        
# class untuks shop
class Shop():
    def __init__(self):
        self.items = []
        self.carts = []
        self.addItems()
    # untuk menambahkan items
    def addItems(self, path="goods.txt"):
        with open(path,"r") as file:
            lines = file.readlines()
            for line in lines:
                goods = line.split()
                self.items.append(Goods(goods[0], goods[1], int(goods[2])))
    #untuk menambahkan cart
    def addCart(self, name):
        self.carts.append(CustomerCart(name))
    #untuk menemukan cart
    def findCart(self, name):
        for i in self.carts:
            if name == i.name:
                return i
    # untuk mencari barang
    def findGood(self, name):
        for i in self.items:
            if name == i.name:
                return i

myShop = Shop()

with open("commands.txt","r") as file:
    cmds = file.readlines()
    cmd = []
    for line in cmds:
        cmd.append(line.split())

for line in cmd:
    if line[0] == "CUSTOMER":
        print('Welcome {}'.format(line[1]))
        myShop.addCart(line[1])

    elif line[1] == "BUY":
        print(myShop.findCart(line[0]).buyGoods(myShop.findGood(line[2])))

    elif line[1] == "TOTAL":
        print(myShop.findCart(line[0]).totalingPrice())
    else:
        print("Sorry, your command cannot be recognized")
