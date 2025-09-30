from django import forms

from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["type"].empty_label = "--Select the type of an asset--"


class TradeForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label="Quantity")