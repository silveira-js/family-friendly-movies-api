from urllib.parse import urlencode
from urllib.parse import urlsplit
from urllib.parse import urlunsplit

from rest_framework.pagination import BasePagination
from rest_framework.response import Response


class TMDbPagination(BasePagination):
    def __init__(self):
        self.page = 1
        self.total_results = 0
        self.total_pages = 0
        super().__init__()

    def paginate_queryset(self, queryset, request, view=None):
        self.page = int(request.query_params.get("page", 1))
        self.total_results = queryset.get("total_results", 0)
        self.total_pages = queryset.get("total_pages", 0)
        self.queryset = queryset["results"]
        self.request = request
        return self.queryset

    def get_paginated_response(self, data):
        return Response(
            {
                "page": self.page,
                "results": data,
                "total_pages": self.total_pages,
                "total_results": self.total_results,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
            },
        )

    def get_next_link(self):
        if self.page < self.total_pages:
            page_number = self.page + 1
            return replace_query_param(
                self.request.build_absolute_uri(),
                "page",
                page_number,
            )
        return None

    def get_previous_link(self):
        if self.page > 1:
            page_number = self.page - 1
            return replace_query_param(
                self.request.build_absolute_uri(),
                "page",
                page_number,
            )
        return None


def replace_query_param(url, key, val):
    (scheme, netloc, path, query, fragment) = urlsplit(url)
    query_params = {}
    query_params[str(key)] = val
    new_query = urlencode(query_params, doseq=True)
    return urlunsplit((scheme, netloc, path, new_query, fragment))
