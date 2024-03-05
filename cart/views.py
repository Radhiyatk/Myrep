from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart,Cartitems
from ecommerce_app.models import Product

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.session_create()
    return cart

def AddtoCart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = Cartitems.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except Cartitems.DoesNotExist:
        cart_item = Cartitems.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cart_items=Cartitems.objects.filter(cart=cart,active=True)
        for item in cart_items:
            total += (item.product.price*item.quantity)
            counter += item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_items=Cartitems.objects.get(product=product,cart=cart)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart:cart_detail')
def remove_all(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_items = Cartitems.objects.get(product=product, cart=cart)
    cart_items.delete()
    return redirect('cart:cart_detail')