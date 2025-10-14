from decimal import Decimal
from typing import assert_type

from django import forms
from django.contrib.auth import get_user_model
from django.test import TestCase

from app.forms import AssetForm, TradeForm, InvestorForm
from app.models import AssetType, Asset


User = get_user_model()


class TestForms(TestCase):
    # --AssetForm--
    def test_asset_form_type_field(self):
        form = AssetForm()
        self.assertIn("type", form.fields)
        field = form.fields["type"]
        self.assertIsInstance(field, forms.ModelChoiceField)
        self.assertEqual(field.empty_label, "--Select the type of an asset--")

    def test_asset_form_with_valid_data(self):
        self.asset_type = AssetType.objects.create(name="Forex")
        data = {
            "name": "USD/PLN",
            "price": "4.34",
            "type": self.asset_type.pk,
        }
        form = AssetForm(data=data)

        self.assertTrue(form.is_valid(), form.errors)
        obj = form.save()
        self.assertIsInstance(obj, Asset)
        self.assertEqual(obj.name, "USD/PLN")
        self.assertEqual(obj.price, Decimal("4.34"))
        self.assertEqual(obj.type, self.asset_type)

    def test_asset_form_with_type_string_price(self):
        self.asset_type = AssetType.objects.create(name="Forex")
        data = {
            "name": "USD/PLN",
            "price": "abc",
            "type": self.asset_type.pk,
        }
        form = AssetForm(data=data)

        self.assertFalse(form.is_valid())

    def test_asset_form_with_no_existing_asset_type(self):
        data = {
            "name": "USD/PLN",
            "price": "4.34",
            "type": 1,
        }
        form = AssetForm(data=data)

        self.assertFalse(form.is_valid())

    # --TradeForm--
    def test_trade_form_with_valid_quantity(self):
        data = {"quantity": 5}
        form = TradeForm(data)

        self.assertTrue(form.is_valid())

    def test_trade_form_with_invalid_quantity(self):
        data = {"quantity": -1}
        form = TradeForm(data)

        self.assertFalse(form.is_valid())

    # --InvestorForm--
    def test_investor_form_with_valid_data(self):
        self.investor = User.objects.create_user(
            username="test_investor",
            password="ZAQ!2wsx1234",
            email="test@test.pl",
        )
        form = InvestorForm(
            data={
                "balance": "5000.00",
                "password1": "NewPass!234",
                "password2": "NewPass!234",
            },
            instance=self.investor,
        )
        self.assertTrue(form.is_valid())

    def test_investor_form_with_mismatching_passwords(self):
        self.investor = User.objects.create_user(
            username="test_investor",
            password="ZAQ!2wsx1234",
            email="test@test.pl",
        )
        form = InvestorForm(
            data={
                "balance": "5000.00",
                "password1": "NewPass!234",
                "password2": "NewBass!234",
            },
            instance=self.investor,
        )
        self.assertFalse(form.is_valid())