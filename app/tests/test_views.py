from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from app.models import AssetType

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser')
        self.client.force_login(self.user)

    def test_home_page(self):
        url = reverse("app:index")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'app/index.html')

    def test_asset_type_list(self):
        AssetType.objects.create(name="Stocks")
        AssetType.objects.create(name="Crypto")
        asset_types = AssetType.objects.all()

        url = reverse("app:asset-type-list")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(asset_types),
            list(res.context['assettypes']),
        )
        self.assertTemplateUsed(res, 'app/assettype_list.html')

