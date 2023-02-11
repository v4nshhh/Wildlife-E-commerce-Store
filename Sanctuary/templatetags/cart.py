from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0

@register.filter(name='totalPrice')
def totalPrice(product,cart):
    return product.productPrice * cart_quantity(product,cart)

@register.filter(name='totalPriceCart')
def totalPriceCart(product,cart):
    sum = 0
    for p in product:
        sum += totalPrice(p,cart)
    return sum