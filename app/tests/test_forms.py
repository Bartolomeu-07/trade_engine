from django import forms
from django.test import TestCase

from app.forms import AssetForm


class TestForms(TestCase):
    # --AssetForm--
    def test_asset_form_type_field(self):
        form = AssetForm()
        self.assertIn("type", form.fields)
        field = form.fields["type"]
        self.assertIsInstance(field, forms.ModelChoiceField)
        self.assertEqual(field.empty_label, "--Select the type of an asset--")