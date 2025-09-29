from django.urls import path

from app.views import AssetTypeListView, AssetListView

urlpatterns = [
    path("assettypes/", AssetTypeListView.as_view(), name="asset-type-list"),
    path("assets/", AssetListView.as_view(), name="asset-list"),
]

app_name = "app"