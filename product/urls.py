from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"product", views.ProductViews, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "filter-product/",
        views.ProductTypeViews.as_view(),
    ),
    path(
        "product-me/",
        views.ProductMeViews.as_view(),
    ),
    path(
        "search-product/",
        views.ProductSearchViews.as_view(),
    ),
]
