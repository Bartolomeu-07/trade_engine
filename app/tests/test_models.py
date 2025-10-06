from django.test import TestCase

from app.models import AssetType, Holding, Investor, Asset


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