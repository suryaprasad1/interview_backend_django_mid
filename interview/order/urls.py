from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, DeactivateOrderView, OrderEmbargoFilterView, TagOrdersView, OrderTagsView


urlpatterns = [
    path("tags/", OrderTagListCreateView.as_view(), name="order-detail"),
    path("", OrderListCreateView.as_view(), name="order-list"),
    path("orders/<int:pk>/deactivate/", DeactivateOrderView.as_view(),name="order-deactivate"),
    path("orders/embargo-filter/", OrderEmbargoFilterView.as_view(),name= "order-embargo-filter"),
    path("orders/<int:pk>/tags/", OrderTagsView.as_view(),name = "order-tags"),
    path("tags/<int:pk>/orders/", TagOrdersView.as_view(),name = "tags-orders"),
]
