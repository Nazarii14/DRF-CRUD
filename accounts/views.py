from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from .tokens import create_jwt_pair_for_user


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = ()

    def post(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "User created successfully"}
            return Response(response,
                            status=status.HTTP_201_CREATED,
                            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = ()

    def post(self, request: Request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login successful", "token": tokens}
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

    def get(self, request: Request, *args, **kwargs):
        content = {
            "user": str(request.user),
            "auth": str(request.auth),
        }
        return Response(content, status=status.HTTP_200_OK)
