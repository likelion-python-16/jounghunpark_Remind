from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from collections import OrderedDict
from django.conf import settings

class CustomPageNumberPagination(PageNumberPagination):
  default_page_size = settings.REST_FRAMEWORK.get("PAGE_SIZE", 5)

  def paginate_queryset(self, queryset, request, view=None):
    page_size = request.query_params.get("PAGE_SIZE", self.default_page_size)

    if page_size == "all":
      self.page_size = queryset.count()
    else:
      try:
        self.page_size = int(page_size)
      except ValueError:
        self.page_size = self.default_page_size

    return super().paginate_queryset(queryset, request, view)
  
  def get_paginated_response(self, data):
    return Response(
      OrderedDict([
        ("data", data),
        ("page_size", len(data)),
        ("total_count", self.page.paginator.count),
        ("page_count", self.page.paginator.num_pages),
        ("current_page", self.page.number),
        ("next", self.get_next_link()),
        ("previous", self.get_previous_link()),
      ])
    )