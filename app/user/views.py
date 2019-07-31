from django.core.mail import send_mail
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        name = data['name']
        email = data['email']

        send_mail(
            f'Welcome {name}',
            'Thank you for registeration',
            'test@email.com',
            [email]
        )
        
        serializer.save()
