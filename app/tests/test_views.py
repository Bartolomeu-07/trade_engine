from tkinter.font import names

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from app.forms import AssetTypeForm
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

