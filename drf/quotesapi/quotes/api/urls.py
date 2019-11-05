from django.urls import path
from quotes.api.views import QuoteListCreateAPIView

urlpatterns = [
    path(
        'quotes/',
        QuoteListCreateAPIView.as_view(),
        name='quote-list'
    ),
]
