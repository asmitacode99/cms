from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from cms.users.api.v1.serializers import UserRegistrationSerailizer
from django.contrib.auth import get_user_model


class UserRegisterationView(CreateAPIView):
    serializer_class = UserRegistrationSerailizer
    permission_classes = [AllowAny]
    
    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data =request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 
            return Response({"message":"Registration successfull!"},status=status.HTTP_201_CREATED)
        return Response({"message":"Registration Failed!"},status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginTokenView(APIView): 
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        # Extract user credentials from request
        username = request.data.get('username')
        password = request.data.get('password')
        
        try:
            user = get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if password is correct
        if not user.check_password(password):
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({
            'access_token': access_token,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email if user.email else None,
            # Assuming the user has a group field
            'group': [group.name for group in user.groups.all()]
        }, status=status.HTTP_200_OK)