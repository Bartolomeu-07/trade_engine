from django.test import TestCase

from app.models import AssetType


class TestModels(TestCase):
    def test_asset_type_str_method(self):
        asset_type = AssetType.objects.create(name="Stocks")

        self.assertEqual(str(asset_type), asset_type.name)