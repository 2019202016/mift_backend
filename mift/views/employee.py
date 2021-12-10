from mift.permissions import IsVolunteer
from mift.serializers import VolunteerSerializer, PostSerializer
from mift.models import Volunteer, POST
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ApplyPostApiView(CreateAPIView):
    serializer_class = VolunteerSerializer
    http_method_names = [u'post']
    permission_classes = [IsAuthenticated, IsVolunteer]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AppliedPostsAPIView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsVolunteer]

    def get_queryset(self):
        applied_posts_id = list(Volunteer.objects.filter(user=self.request.user).values_list('post_id', flat=True))
        return POST.objects.filter(id__in=applied_posts_id)


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsVolunteer])
def already_applied_api_view(request, post_id):
    is_applied = Volunteer.objects.filter(user=request.user, post_id=post_id).exists()
    content = {
        'is_applied': is_applied
    }
    return Response(content)
