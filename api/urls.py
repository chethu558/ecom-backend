from django.urls import path,include
from .views import home

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home, name='home'),
    path('categories/', include('api.category.urls')),
    path('products/', include('api.product.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
