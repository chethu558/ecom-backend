from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout


from .serializers import  UserSerializer
from .models import CustomUser



import random
import re
# Create your views here.


def generate_session_token(length=25):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(65,122)]+[str(i) for i in range(10)]) for _ in range(25))

@csrf_exempt
def signin(request):
    
    if not request.method == 'POST':
        return JsonResponse({'Error':'Invalid request'})

    username = request.POST['email']
    password = request.POST['password']

    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
        return JsonResponse({'Error':'Invalid Email'})

    if len(password) < 8 :
        return JsonResponse({'Error':'Password must be atlest 8 chars'})
    
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            user_dict = UserModel.objects.filter(email=username).values().first()
            user_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'Error':'Previous session exists'})
            
            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token':token, 'user':user_dict})

        else:
            return JsonResponse({'Error':'Invalid password'})

    except UserModel.DoesNotExist:
        return JsonResponse({'Error':'User does not exist'})

@csrf_exempt
def  signout(request, id):
    logout(request)
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'Error':'Invlid user'})
    
    return JsonResponse({'Error':'Success'})



class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action ={'create': [AllowAny] }

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


