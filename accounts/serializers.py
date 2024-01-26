from rest_framework import serializers
from rest_framework.authtoken.models import Token
from posts.serializers import PostSerializer

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "Email is already in use."}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user


class CurrentUserPostsSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(
        # view_name="post_detail",
        # many=True,
        # name="post_detail",
        # queryset=User.objects.all(),
    )

    class Meta:
        model = User
        fields = ["id", "email", "username", "posts"]

    def get_posts(self, user):
        posts = user.posts.all()
        serializer = PostSerializer(posts, many=True)
        return serializer.data
