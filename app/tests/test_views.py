from platform import processor
from tkinter.font import names
from typing import assert_type

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from app.forms import AssetTypeForm
from app.models import AssetType, Asset

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

# --AssetType--

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

    def test_asset_type_create(self):

        # GET method
        url = reverse("app:asset-type-create")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'app/assettype_form.html')
        self.assertIsInstance(res.context['form'], AssetTypeForm)

        # POST method
        success_url = reverse("app:asset-type-list")
        data = {"name": "Stocks"}
        res = self.client.post(url, data=data)

        self.assertRedirects(res, success_url, fetch_redirect_response=False)
        self.assertTrue(AssetType.objects.filter(name='Stocks').exists())

    def test_asset_type_update(self):
        self.asset_type = AssetType.objects.create(name="Stocks")
        url = reverse("app:asset-type-update", args=[self.asset_type.id])

        # GET method
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "app/assettype_form.html")
        self.assertIsInstance(res.context['form'], AssetTypeForm)

        # POST method
        success_url = reverse("app:asset-type-list")
        data = {"name": "ETFs"}
        res = self.client.post(url, data)

        self.assertRedirects(res, success_url, fetch_redirect_response=False)
        self.asset_type.refresh_from_db()
        self.assertEqual(self.asset_type.name, data["name"])

    def test_asset_type_delete(self):
        self.asset_type = AssetType.objects.create(name="Stocks")
        url = reverse("app:asset-type-delete", args=[self.asset_type.id])

        # GET method
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "app/assettype_delete.html")

        # POST method
        success_url = reverse("app:asset-type-list")
        res = self.client.post(url)

        self.assertFalse(AssetType.objects.filter(name='Stocks').exists())
        self.assertRedirects(res, success_url, fetch_redirect_response=False)

# --Asset--

    def test_asset_list(self):
        type = AssetType.objects.create(name="Stocks")
        Asset.objects.create(name="Tesla", price=1001.20, type=type)
        Asset.objects.create(name="Samsung", price=300.56, type=type)
        assets = Asset.objects.all()

        url = reverse("app:asset-list")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(assets),
            list(res.context['assets']),
        )
        self.assertTemplateUsed(res, 'app/asset_list.html')

    def test_asset_detail(self):
        type = AssetType.objects.create(name="Stocks")
        test_asset = Asset.objects.create(name="Tesla", price=1001.20, type=type)

        url = reverse("app:asset-detail", args=[test_asset.id])
        res = self.client.get(url)

        self.assertEqual(res.context['asset'], test_asset)
        self.assertTemplateUsed(res, "app/asset_detail.html")
