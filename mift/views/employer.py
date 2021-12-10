from mift.permissions import IsNGO
from mift.serializers import VolunteerSerializer
from mift.models import Volunteer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class VolunteersListAPIView(ListAPIView):
    serializer_class = VolunteerSerializer
    permission_classes = [IsAuthenticated, IsNGO]

    def get_queryset(self):
        user = self.request.user
        return Volunteer.objects.filter(post__user_id=user.id)
