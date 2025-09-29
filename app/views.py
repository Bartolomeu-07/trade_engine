from django.views import generic

from app.models import AssetType, Asset


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
