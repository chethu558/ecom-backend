from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from .serializers import OrderSerializer
from .models import Order

# Create your views here.

def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
           return True
        return False

    except UserModel.DoesNotExist:
        return False

@csrf_exempt
def add_to_cart(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'Msg':"Please login to continue"})

    if request.method == "POST":
        user_id = id
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        products = request.POST['products']

        total_products = len(products.split(',')[:-1])

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'Msg':"User doesn't exist"})

        order = Order(user = user, product_names = products, total_products=total_products, transaction_id=transaction_id, total_amount=amount)
        order.save()
        return JsonResponse({'Msg':"Success"})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer

