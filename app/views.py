from django.views import generic

from app.models import AssetType, Asset, Investor


class AssetTypeListView(generic.ListView):
    model = AssetType
    template_name = "app/assettype_list.html"
    context_object_name = "assettypes"
    fields = "__all__"


class AssetListView(generic.ListView):
    model = Asset
    template_name = "app/asset_list.html"
    context_object_name = "assets"
    fields = "__all__"


class InvestorListView(generic.ListView):
    model = Investor
    template_name = "app/investor_list.html"
    context_object_name = "investors"
    fields = ["username", "balance", "holdings"]
