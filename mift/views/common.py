from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from mift.models import POST
from mift_backend.accounts.profile.models import UserProfile

from ..serializers import *


class PostCreate(CreateAPIView):
    # queryset = POST.objects.all()
    http_method_names = [u'post']
    serializer_class = PostSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = serializer_class.Meta.model.objects.filter(filled=False)
    permission_classes = [AllowAny]


class SearchApiView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if 'location' in self.request.GET and 'position' in self.request.GET:
            return self.serializer_class.Meta.model.objects.filter(filled=False,
                                                                   location__contains=self.request.GET['location'],
                                                                   title__contains=self.request.GET['position'])
        else:
            return self.serializer_class.Meta.model.objects.filter(filled=False)
