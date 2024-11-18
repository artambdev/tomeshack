from django.shortcuts import get_object_or_404
from products.models import Book

def cart_contents(requests):

    cart_items = []
    total = 0
    num_items = 0
    cart = request.session.get('cart', {})

    for item, quantity in cart.items():
        book = get_object_or_404(Book, pk=item_id)
        total += book.price * quantity
        num_items += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'subtotal': book.price * quantity,
            'book': book,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'num_items': num_items,
    }

    return context