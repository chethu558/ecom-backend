from rest_framework import routers
from django.urls import path,include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.OrderViewSet)

urlpatterns = [
    path('add/<int:id>/<str:token>/', views.add_to_cart, name="add-to-cart"),
    path('', include(router.urls))
]