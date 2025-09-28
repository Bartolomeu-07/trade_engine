from django.urls import path

from app.views import AssetTypeListView

urlpatterns = [
    path("assettypes/", AssetTypeListView.as_view(), name="assettypes"),
]

app_name = "app"