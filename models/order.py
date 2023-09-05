####### commented out bits were part of a failed attempt to generate order numbers
####### I thought that might help with trying to get the order list to link to individual order pages
####### ran some tests in my scrap_paper.py but run into issues whenever I add orders.index(self) into the function...

class Order():

    def __init__(self, customer_name, order_date, product_name, quantity):
        # self.order_number = 1
        self.customer_name = customer_name
        self.order_date = order_date
        self.product_name = product_name
        self.quantity = quantity
    
    # def assign_order_number(self):
    #     self.order_number = orders.index(self)
    #     return self.order_number
    # def assign_order_number(self, random_number):
    #     self.order_number += random_number
    #     return self.order_number

    # def return_index_position(self):
    #     index_position = orders.index(self)
    #     return index_position
    