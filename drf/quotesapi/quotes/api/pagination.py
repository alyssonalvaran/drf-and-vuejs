from rest_framework.pagination import PageNumberPagination


class QuotePagination(PageNumberPagination):
    page_size = 30