from django.urls import include, path

app_name = "apis"

urlpatterns = [
    path("", include("capacity_quotation.urls", namespace="capacity_quotation")),
]
