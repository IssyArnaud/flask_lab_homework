from flask import Blueprint
from flask import render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def order_list():
    return render_template('order_list.jinja', title="Order List", orders=orders)

@orders_blueprint.route("/orders/<index>")
def show_single_order(index):
    order = orders[int(index)]
    return render_template('single_order.jinja', title="Order Details", order=order)