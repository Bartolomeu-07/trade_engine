from django.urls import reverse_lazy, reverse
from django.views import generic

from app.forms import AssetForm
from app.models import AssetType, Asset, Investor, Order


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


class AssetDetailView(generic.DetailView):
    model = Asset
    template_name = "app/asset_detail.html"
    context_object_name = "asset"


class AssetCreateView(generic.CreateView):
    model = Asset
    form_class = AssetForm
    template_name = "app/asset_form.html"
    success_url = reverse_lazy("app:asset-list")


class AssetUpdateView(generic.UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = "app/asset_form.html"

    def get_success_url(self):
        return reverse("app:asset-detail", kwargs={"pk": self.object.pk})


class InvestorListView(generic.ListView):
    model = Investor
    template_name = "app/investor_list.html"
    context_object_name = "investors"
    fields = ["username", "balance", "holdings"]


class OrderListView(generic.ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = "orders"
    fields = "__all__"
