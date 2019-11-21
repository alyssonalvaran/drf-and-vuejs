from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer


class ProfileViewSet(ReadOnlyModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated]
