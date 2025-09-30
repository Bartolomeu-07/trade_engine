# services.py
from decimal import Decimal
from django.core.exceptions import ValidationError
from .models import Investor, Asset, Holding, Order

def execute_order_simple(*, investor: Investor, asset: Asset, side: str, quantity: int) -> Order:
    if quantity <= 0:
        raise ValidationError("Quantity must be positive.")

    price = Decimal(str(asset.price))
    total = price * Decimal(quantity)

    # Pobierz lub stwórz holding
    holding, _ = Holding.objects.get_or_create(investor=investor, asset=asset, defaults={"quantity": 0})

    if side == Order.BUY:
        if investor.balance < total:
            raise ValidationError("Insufficient balance.")
        investor.balance -= total
        holding.quantity += quantity

    elif side == Order.SELL:
        if holding.quantity < quantity:
            raise ValidationError("Insufficient quantity to sell.")
        investor.balance += total
        holding.quantity -= quantity

    else:
        raise ValidationError("Invalid side.")

    # Zapisz zmiany
    investor.save()
    holding.save()

    # Utwórz order
    order = Order.objects.create(
        asset=asset,
        investor=investor,
        side=side,
        quantity=quantity,
    )
    return order