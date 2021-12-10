from mift_backend.accounts.user.serializers import UserSerializer
from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = POST
        fields = "__all__"


class VolunteerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Volunteer
        fields = "__all__"
