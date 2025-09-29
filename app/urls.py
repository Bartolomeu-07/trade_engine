from django.urls import path

from app.views import AssetTypeListView, AssetListView, InvestorListView, OrderListView, AssetDetailView, \
    AssetCreateView, AssetUpdateView

urlpatterns = [
    # ASSET TYPE
    path("assettypes/", AssetTypeListView.as_view(), name="asset-type-list"),

    # ASSET
    path("assets/", AssetListView.as_view(), name="asset-list"),
    path("assets/<int:pk>/", AssetDetailView.as_view(), name="asset-detail"),
    path("assets/create/", AssetCreateView.as_view(), name="asset-create"),
    path("assets/update", AssetUpdateView.as_view(), name="asset-update"),

    # INVESTOR
    path("investors/", InvestorListView.as_view(), name="investor-list"),

    # ORDER
    path("orders/", OrderListView.as_view(), name="order-list"),
]

app_name = "app"