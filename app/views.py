from django.views import generic

from app.models import AssetType


class AssetTypeListView(generic.ListView):
    model = AssetType
    template_name = "app/assettype_list.html"
    context_object_name = "assettypes"
    fields = "__all__"
