from django.urls import path
from profiles.api.views import ProfileViewSet

urlpatterns = [
	path(
		"profiles/",
		ProfileViewSet.as_view({"get": "list"}),
		name="profile-list"
	),
	path(
		"profiles/<int:pk>/",
		ProfileViewSet.as_view({"get": "retrieve"}),
		name="profile-detail"
	),
]
