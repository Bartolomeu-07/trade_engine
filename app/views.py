from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView, FormView

from app.forms import AssetForm, TradeForm
from app.models import AssetType, Asset, Investor, Order
from app.services import execute_order


class IndexView(TemplateView):
    template_name = "app/index.html"


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


class AssetDeleteView(generic.DeleteView):
    model = Asset
    template_name = "app/asset_delete.html"
    success_url = reverse_lazy("app:asset-list")


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


class AssetBuyView(FormView):
    template_name = "app/asset_trade.html"
    form_class = TradeForm

    def dispatch(self, request, *args, **kwargs):
        self.asset = get_object_or_404(Asset, pk=kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["asset"] = self.asset
        ctx["side"] = Order.BUY
        return ctx

    def form_valid(self, form):
        try:
            order = execute_order(
                investor=self.request.user,
                asset=self.asset,
                side=Order.BUY,
                quantity=form.cleaned_data["quantity"],
            )
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("app:asset-detail", kwargs={"pk": self.asset.pk})


class AssetSellView(AssetBuyView):
    template_name = "app/asset_trade.html"
    form_class = TradeForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["side"] = Order.SELL
        return ctx

    def form_valid(self, form):
        try:
            order = execute_order(
                investor=self.request.user,
                asset=self.asset,
                side=Order.SELL,
                quantity=form.cleaned_data["quantity"],
            )
            return super(FormView, self).form_valid(form)
        except ValidationError as e:
            form.add_error(None, e.message)
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse("app:asset-detail", kwargs={"pk": self.asset.pk})
