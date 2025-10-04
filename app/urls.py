from django.urls import path

from app.views import AssetTypeListView, AssetListView, InvestorListView, OrderListView, AssetDetailView, \
    AssetCreateView, AssetUpdateView, AssetDeleteView, IndexView, AssetBuyView, AssetSellView, AssetTypeUpdateView, \
    AssetTypeCreateView, AssetTypeDeleteView, InvestorDetailView, InvestorUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    # ASSET TYPE
    path("assettypes/", AssetTypeListView.as_view(), name="asset-type-list"),
    path("assettypes/create", AssetTypeCreateView.as_view(), name="asset-type-create"),
    path("assettypes/<int:pk>/update", AssetTypeUpdateView.as_view(), name="asset-type-update"),
    path("assettypes/<int:pk>/delete", AssetTypeDeleteView.as_view(), name="asset-type-delete"),

    # ASSET
    path("assets/", AssetListView.as_view(), name="asset-list"),
    path("assets/<int:pk>/", AssetDetailView.as_view(), name="asset-detail"),
    path("assets/create/", AssetCreateView.as_view(), name="asset-create"),
    path("assets/<int:pk>/update", AssetUpdateView.as_view(), name="asset-update"),
    path("assets/<int:pk>/delete", AssetDeleteView.as_view(), name="asset-delete"),
    path("assets/<int:pk>/buy", AssetBuyView.as_view(), name="asset-buy"),
    path("assets/<int:pk>/sell", AssetSellView.as_view(), name="asset-sell"),

    # INVESTOR
    path("investors/", InvestorListView.as_view(), name="investor-list"),
    path("investors/<int:pk>/detail", InvestorDetailView.as_view(), name="investor-detail"),
    path("investors/<int:pk>/update", InvestorUpdateView.as_view(), name="investor-update")

    # ORDER
    path("orders/", OrderListView.as_view(), name="order-list"),
]

app_name = "app"