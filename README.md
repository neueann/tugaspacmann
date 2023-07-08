This is my phyton project for phyton class @ pacmann. I basically made a self-service cashier app for Andi, so customers can check out Andi's product even if they are
not in the same city as Andi. 
To start off, as a programmer we have to make the customers create an unique "User ID". 
Then they have to add their desired products by typing in the product's name, qty, and price. I added "Tango" (6000), "Ultra Milk" (22000), "Ayam Goreng" (20000), "Pasta Gigi" (15000), ("Mainan Mobil", 0, 200000), "Mi Instan" (3000).
If the customer want to add a new product, they have to type add_item(self, name, qty, price). If the input is correct, then the app will print the name, quantity, and price of the chosen product. 
It is not rare that a customer will want to add another products already in the cart. They can do this by typing "update_item_qty(self, name, new qty)". If the name is correct, the app will print "Updated (product name) to (new quantity)" along with the updated price. But if the app cannot find the product in the cart, it will print "Item is not in the cart".  
The customer can also update the price of the product by typing "update_item_price(self, name, price)". But if the app cannot find the product in the cart, it will print "Item is not in the cart".  
While working on the project, I realized that a lot of people often mistyped, so I decided that the app will self-update - meaning the customers can easily update their cart by typing update_item_name("faulty_name", "correct_name"). For example, a customer want to add another "3 ultra milk" in their cart, with 4 ultra milk already existing in the cart. But they typed add_item("utra milk", 3, 22000) instead of "ultra milk". Instead of deleting the entry, the customer only have to type update_item_name("utra", "ultra"). The total of ultra milk in their cart will be updated from 4 to 7. The app will print "Updated product utra milk name to ultra milk".
If the customer want to check that their order is correct, they can search the product by typing "check_order(self)". If the app found that the customer has mistyped their order, "Invalid name found" will pop up. If the name, price, and qty of order is corret, the app will print "Order is valid". If it is not, the app will print "Invalid data in input found".  
If a customer wishes that they want to delete an entry to their order, they can type "delete_item(self, name)". If the input is correct, the app will print "deleted product (name)". 
Even so, if a customer wishes to reset their transaction, they can type "reset_transaction(self)." The app will print "Transaction has been reset".
Andi made a special request by deducting certain percentage if a customer reached certain spending. 
  The specification being: 
  if total >= 200: disc = 5%
  if total >= 300: disc = 8
  if total >= 500: disc = 10 
To check the total price and see if they are eligible for the discount, customer can type "total_price(self)". If the total has reached the minimum thresold of 200000, the app will automatically deduct the discount. The app will also print "Subtotal is (total before discount) with a discount of (empty if the total has not reached 200000, number if the total has reached 200000). Total price will be deducted from the original price. 
