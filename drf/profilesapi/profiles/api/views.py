from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins
from profiles.models import Profile, ProfileStatus
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer


class ProfileViewSet(mixins.UpdateModelMixin,
					mixins.ListModelMixin,
					mixins.RetrieveModelMixin,
					viewsets.GenericViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]


class ProfileStatusViewSet(ModelViewSet):
	queryset = ProfileStatus.objects.all()
	serializer_class = ProfileStatusSerializer
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

	def perform_create(self, serializer):
		user_profile = self.request.user.profile
		serializer.save(user_profile=user_profile)
