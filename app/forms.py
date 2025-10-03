from django import forms

from .models import Asset, AssetType


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["type"].empty_label = "--Select the type of an asset--"


class TradeForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Quantity")


class AssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = "__all__"