from django.urls import path,include
from . import views
urlpatterns = [
    path('gettoken/<int:id>/<str:token>/', views.generate_token, name="get-token"),
    path('process/<int:id>/<str:token>/', views.process_payment, name="get-token"),
]