from django.urls import path

from app.views import AssetTypeListView, AssetListView, InvestorListView, OrderListView

urlpatterns = [
    # ASSET TYPE
    path("assettypes/", AssetTypeListView.as_view(), name="asset-type-list"),

    # ASSET
    path("assets/", AssetListView.as_view(), name="asset-list"),

    # INVESTOR
    path("investors/", InvestorListView.as_view(), name="investor-list"),

    # ORDER
    path("orders", OrderListView.as_view(), name="order-list"),
]

app_name = "app"