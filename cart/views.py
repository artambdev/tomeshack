from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """
    Simply renders the cart view
    """
    return render(request, 'cart/cart.html')


def modify_cart(request, item_id):
    """
    Handles requests to modify item quantity via cart view
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def add_to_cart(request, item_id):
    """
    Handles requests to add items to the cart
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += new_quantity
        new_quantity = cart[item_id] + quantity
        if new_quantity > 4:
            new_quantity = 4
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    Handles requests to remove items from the cart
    """
    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)
        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
