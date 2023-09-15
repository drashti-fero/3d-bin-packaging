from rest_framework.routers import DefaultRouter

from . import views

app_name = "capacity_quotation"
router = DefaultRouter()

router.register("packaging_spaces", views.PackagingSpacesViewSet, basename="packaging_spaces")
router.register("items", views.ItemsViewSet, basename="items")

urlpatterns = []

urlpatterns += router.urls
