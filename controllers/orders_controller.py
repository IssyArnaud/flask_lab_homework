####### I got stuck when it came to adding a link to the orders displayed in the /orders page to their individual pages
####### the commented out bit was part of a failed attempt to find a work-around via creating an order number variable
####### maybe I thought that would be easier to call in the orders_list.jinja for loop? 
####### but I think the main problem is that I don't understand how for loops work in jinja...
####### I don't seem to be able to have more than one step in the for loop? 



from flask import Blueprint
from flask import render_template
from models.order_list import orders
from models.order import Order

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def order_list():
    return render_template('order_list.jinja', title="Order List", orders=orders)

@orders_blueprint.route("/orders/<index>")
def show_single_order(index):
    index = orders[int(index)]
    return render_template('single_order.jinja', title="Order Details", index=index)

# @orders_blueprint.route("/orders/<order_number>")
# def show_single_order(order_number):
#     return render_template('single_order.jinja', title="Order Details", order_number=order_number)