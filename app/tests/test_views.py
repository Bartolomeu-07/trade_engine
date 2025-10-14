from decimal import Decimal
from platform import processor
from tkinter.font import names
from typing import assert_type

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from app.forms import AssetTypeForm, AssetForm, InvestorForm
from app.models import AssetType, Asset, Investor

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

    def test_asset_create(self):
        type = AssetType.objects.create(name="Stocks")

        # GET method
        url = reverse("app:asset-create")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'app/asset_form.html')
        self.assertIsInstance(res.context['form'], AssetForm)

        # POST method
        success_url = reverse("app:asset-list")
        data = {"name": "Tesla", "price": 10001.01, "type": type.id}
        res = self.client.post(url, data=data)

        self.assertRedirects(res, success_url, fetch_redirect_response=False)
        self.assertTrue(Asset.objects.filter(name='Tesla').exists())

    def test_asset_update(self):
        self.asset_type = AssetType.objects.create(name="Stocks")
        self.asset = Asset.objects.create(name="Tesla", price=1001.20, type=self.asset_type)
        url = reverse("app:asset-update", args=[self.asset.id])

        # GET method
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "app/asset_form.html")
        self.assertIsInstance(res.context['form'], AssetForm)

        # POST method
        success_url = reverse("app:asset-detail", args=[self.asset.id])
        data = {"name": self.asset.name, "price": 12.003, "type": self.asset_type.id}
        res = self.client.post(url, data)

        self.assertRedirects(res, success_url, fetch_redirect_response=False)
        self.asset.refresh_from_db()
        self.assertEqual(self.asset.price, Decimal("12.003"))

    def test_asset_delete(self):
        self.asset_type = AssetType.objects.create(name="Stocks")
        self.asset = Asset.objects.create(name="Tesla", price=1001.20, type=self.asset_type)
        url = reverse("app:asset-delete", args=[self.asset.id])

        # GET method
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "app/asset_delete.html")

        # POST method
        success_url = reverse("app:asset-list")
        res = self.client.post(url)

        self.assertFalse(Asset.objects.filter(name='Tesla').exists())
        self.assertRedirects(res, success_url, fetch_redirect_response=False)

# --Investor--

    def test_investor_list(self):
        User = get_user_model()
        User.objects.create_superuser(
            username="test_one",
            email="tester@gmail.com",
            password="test1234@",
            balance=Decimal("12000.00"),
        )
        User.objects.create_superuser(
            username="test_two",
            email="testing@gmail.com",
            password="test1234%",
            balance=Decimal("135000.50"),
        )
        investors = Investor.objects.all()

        url = reverse("app:investor-list")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(investors),
            list(res.context['investors']),
        )
        self.assertTemplateUsed(res, "app/investor_list.html")

    def test_investor_detail(self):
        User = get_user_model()
        investor = User.objects.create_superuser(
            username="test_one",
            email="tester@gmail.com",
            password="test1234@",
            balance=Decimal("12000.00"),
        )

        url = reverse("app:investor-detail", args=[investor.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context['investor'], investor)
        self.assertTemplateUsed(res, "app/investor_detail.html")

    def test_investor_update(self):
        User = get_user_model()
        investor = User.objects.create_superuser(
            username="test_one",
            email="tester@gmail.com",
            password="test1234@",
            balance=Decimal("12000.00"),
        )
        url = reverse("app:investor-update", args=[investor.id])

        # GET method
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "app/investor_form.html")
        self.assertIsInstance(res.context['form'], InvestorForm)

        # POST method
        success_url = reverse("app:investor-detail", args=[investor.id])
        data = {
            "balance": Decimal("5000.00"),
            "password1": "ZAQ!2wsx1234",
            "password2": "ZAQ!2wsx1234",
        }
        res = self.client.post(url, data)

        self.assertRedirects(res, success_url, fetch_redirect_response=False)
        investor.refresh_from_db()
        self.assertEqual(investor.balance, data["balance"])
        self.assertTrue(investor.check_password(data["password1"]))