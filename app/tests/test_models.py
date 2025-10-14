from django.test import TestCase

from app.models import AssetType, Holding, Investor, Asset, Order


class TestModels(TestCase):
    def setUp(self):
        self.investor = Investor.objects.create(
            username="TestInvestor",
            email="testemail@kj.com",
            password="TestPass123#",
            balance=10000,
        )
        self.asset_type = AssetType.objects.create(name="Stocks")
        self.asset = Asset.objects.create(
            name="Tesla",
            price=3118.20,
            type=self.asset_type,
        )
        self.holding = Holding.objects.create(
            investor=self.investor,
            asset=self.asset,
            quantity=3,
        )

    def test_asset_type_str_method(self):
        self.assertEqual(str(self.asset_type), self.asset_type.name)

    def test_holding_str_method(self):
        self.assertEqual(
            str(self.holding),
            f"{self.investor.username} holds {self.holding.quantity} × {self.asset.name}"
        )

    def test_holding_should_be_deleted_if_quantity_equal_to_zero(self):
        self.assertEqual(Holding.objects.all().count(), 1)
        self.holding.quantity = 0
        self.holding.save()
        self.assertEqual(Holding.objects.all().count(), 0)

    def test_order_value_is_calculate_correct(self):
        order_1 = Order.objects.create(
            id=1,
            asset = self.asset,
            quantity = 5,
            investor = self.investor,
            side = "Buy",
        )
        self.assertEqual(order_1.value, self.asset.price * order_1.quantity)

        order_2 = Order.objects.create(
            id=2,
            asset=self.asset,
            quantity=3,
            investor=self.investor,
            side="Sell",
        )
        self.assertEqual(order_2.value, self.asset.price * order_2.quantity)