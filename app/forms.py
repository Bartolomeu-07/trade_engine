from django import forms

from .models import Asset, AssetType, Investor


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


class InvestorForm(forms.ModelForm):
    balance = forms.DecimalField(
        max_digits=14, decimal_places=2, min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    password1 = forms.CharField(
        label="New password", required=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm new password", required=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = Investor
        fields = ["balance"]

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")

        if p1 or p2:
            if not p1 or not p2:
                raise forms.ValidationError("Fill in both password fields.")
            if p1 != p2:
                raise forms.ValidationError("Passwords do not match.")
        return cleaned

    def save(self, commit=True):
        instance = super().save(commit=False)
        p1 = self.cleaned_data.get("password1")
        if p1:
            instance.set_password(p1)
        if commit:
            instance.save()
        return instance
