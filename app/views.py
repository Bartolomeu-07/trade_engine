from django.views import generic

from app.models import AssetType


class AssetTypeListView(generic.ListView):
    model = AssetType
    fields = "__all__"
