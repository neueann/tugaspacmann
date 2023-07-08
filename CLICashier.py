import time
from datetime import datetime


# class constructor for a product
class Product():
    def __init__(self, name, qty, price):
        self.Name = name
        self.Qty = qty
        self.Price = price

# insert Product data here
Pdata = {
    "Tango" : Product("Tango", 0, 6000),
    "Kecap Bango" : Product("Kecap Bango", 0, 16000),
    "Ultra Milk" : Product("Ultra Milk", 0, 22000),
    "Ayam Goreng" : Product("Ayam Goreng", 0, 20000),
    "Pasta Gigi" : Product("Pasta Gigi", 0, 15000),
    "Mainan Mobil" : Product("Mainan Mobil", 0, 200000),
    "Mi Instan" : Product("Mi Instan", 0, 3000),
}

# class constructor for trx
class Transaction():
    # class constructor default
    def __init__(self):
        self.Trxid = datetime.now().strftime("%Y%m%d%H%M%S")
        self.Cart = {} #dictionary of string : product types
        
    # adds item to Transaction object, says if item is already in cart
    def add_item(self, name, qty, price):
        list = self.Cart.keys()
        if name in list:
            self.update_item_qty(name, (self.Cart[name].Qty + qty))
        else:
            self.Cart[name] = Product(name, qty, price)
        print("added item", end = " ")
        print(name, end= ", ")
        print(qty, end=", ")
        print(price)
    
    # finds key of name in cart, if exists, copies value to new key, updates to new name
    def update_item_name(self, name, name2):
        list = self.Cart.keys()
        if name in list:
            #replicates to 
            if name2 in list:
                self.update_item_qty(name2, (self.Cart[name].Qty + self.Cart[name2].Qty))
                self.Cart.pop(name)
            else:
                self.Cart[name2] = Product(name2, self.Cart[name].Qty, self.Cart[name].Price)
                self.Cart.pop(name)
            print("updated product", end=" ")
            print(name)
            print("name to", end=" ")
            print(name2)
        else:
            print("Item is not in cart")
            
    # finds key of name in cart, if exists, updates to new qty
    def update_item_qty(self, name, qty):
        list = self.Cart.keys()
        if name in list:
            self.Cart[name].Qty = qty
            print("updated product", end=" ")
            print(name)
            print("quantity to", end=" ")
            print(qty)
        else:
            print("Item is not in cart")
            
    # finds key of name in cart, if exists, updates to new price 
    def update_item_price(self, name, price):
        list = self.Cart.keys()
        if name in list:
            self.Cart[name].Price = price
            print("updated product", end=" ")
            print(name)
            print("price to", end=" ")
            print(price)
        else:
            print("Item is not in cart")
        
    # pops the name key-value pair from dictionary
    def delete_item(self, name):
        self.Cart.pop(name)
        print("deleted product", end=" ")
        print(name)
        
    # empties dictionary
    def reset_transaction(self):
        self.Cart.clear()
        print("Transaction has been reset")
        
    def check_order(self):
        for name in self.Cart.keys():
            #checks against the product data in "Pdata"
            if name not in Pdata.keys():
                print("Invalid name found:", end=" ")
                print(name)
            elif self.Cart[name].Name == Pdata[name].Name and self.Cart[name].Price == Pdata[name].Price:
                print("Order is valid")
            else:
                print("Invalid data in input found", end=" ")
                print(name)
                
        print("Transaction id =", end=" ")
        print(self.Trxid)
        print("| No |  Nama Item  | Jumlah Item | Harga/Item | Total Harga |")
        print("|----|-------------|-------------|------------|-------------|")
        i = 1
        for name in self.Cart.keys():
            pdname = self.Cart[name].Name
            pdqty = self.Cart[name].Qty
            pdprice = self.Cart[name].Price
            print("| ", end=" ")
            print(i, end=" ")
            print("| ", end="")
            print(pdname.ljust(12), end="")
            print("| ", end="")
            print(str(pdqty).ljust(12), end="")
            print("| ", end="")
            print(str(pdprice).ljust(11), end="")
            print("| ", end="")
            print(str(pdprice * pdqty).ljust(12), end="")
            print("| ")
            i += 1 #increments i for next count
    
    def total_price(self):
        total = 0
        disc = 0
        # adds prices
        for name in self.Cart:
            total += (self.Cart[name].Price * self.Cart[name].Qty)
        if total >= 200:
            disc = 5
        if total >= 300:
            disc = 8
        if total >= 500:
            disc = 10
        print("Subtotal is", end=" ") #print without newline
        print(total, end=" ")
        print("with a discount of", end=" ")
        print(disc, end= "% or ")
        print(((total/100)*disc))
        total = (total/100) * (100-disc) #count total
        print("your total is", end= " ")
        print(total)
    
trax = Transaction()
trax.add_item("Ayam Goreng", 2, 20000)
trax.add_item("Pasta Gigi", 3, 15000)
trax.check_order()
trax.delete_item("Pasta Gigi")
trax.reset_transaction

trax.add_item("Ayam Goreng", 2, 20000)
trax.add_item("Pasta Gigi", 3, 15000)
trax.add_item("Mainan Mobil", 1, 200000)
trax.add_item("Mi Instan", 5, 3000)
trax.total_price()
#trax.add_item("Tango", 3, 16000) # harusnya 16000
#trax.check_order()

#trax.update_item_name("Jango", "Tango")
#trax.check_order()

#trax.total_price()
#trax.reset_transaction()
#trax.check_order()
#

    