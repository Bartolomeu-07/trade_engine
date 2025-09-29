from django.urls import path

from app.views import AssetTypeListView, AssetListView, InvestorListView

urlpatterns = [
    path("assettypes/", AssetTypeListView.as_view(), name="asset-type-list"),
    path("assets/", AssetListView.as_view(), name="asset-list"),
    path("investors/", InvestorListView.as_view(), name="investor-list"),
]

app_name = "app"