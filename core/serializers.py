from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from .models import Post, Upvote


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        required = ("id", "username", "password", "email")
        fields = ("id", "username", "password", "email")

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            is_active=True,
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class PostSerializer(ModelSerializer):
    upvotes_count = SerializerMethodField()

    class Meta:
        model = Post
        fields = "id", "title", "text", "upvotes_count", "author", "created"

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        post.author = self.context.get("request").user.username
        post.created = timezone.now()

        post.save()
        return post

    def get_upvotes_count(self, obj):
        return Upvote.objects.filter(post_id=obj.id).count()


# todo check if works without it


class UpvoteSerializer(ModelSerializer):
    class Meta:
        model = Upvote
        fields = "__all__"
