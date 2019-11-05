from rest_framework import generics
# from rest_framework import permissions
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404

from quotes.models import Quote
# from ebooks.api.pagination import SmallSetPagination
# from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from quotes.api.serializers import QuoteSerializer


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by("id")
    serializer_class = QuoteSerializer
    # permission_classes = [IsAdminUserOrReadOnly]
    # pagination_class = SmallSetPagination
