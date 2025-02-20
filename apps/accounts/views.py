from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.accounts.models import *
from apps.accounts.serializers import *
# Create your views here.


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()


    def post(self, request):
        try:

            user_exists = User.objects.filter(email=request.data['email']).exists()

            if user_exists:
                return Response({ "message": "exists", "status_code": status.HTTP_409_CONFLICT })
            else:

                serializer = RegistrationSerializer(data=request.data)
                if serializer.is_valid():
                    print(request.data)
                    serializer.save()
                    print('Saved ...')
                    return Response(status.HTTP_201_CREATED)
                    # if user:
                    #     print("Created ....")
                    # else:
                    #     print("Failed ....")
                else:
                    return Response({ "message": 'invalid', "status_code": status.HTTP_412_PRECONDITION_FAILED })

        except:
            return Response({ "message": "failed", "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR })





class LoginView(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        


        try: 
            data["message"] = "success"
            data["email"] = self.user.email
            data["name"] = self.user.fullname
            data["role"] = self.user.role
            data["id"] = self.user.uid

            return data
        except:
            data["message"] = "failed"
            return data




class UserProfileView(viewsets.ViewSet):
    permission_classes = [ IsAuthenticated ]
    
    def create(self, request):
        pass

    def list(self, request):
        try:
            # print("Testing ....")
            queryset = User.objects.all()
            user = get_object_or_404(queryset, uid=self.request.user.uid)
            if user:
                serializer = UserSerializer(user)
                return Response(serializer.data)
            else:
                return Response(status.HTTP_404_NOT_FOUND)
        except:
            return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None):
        pass


    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
