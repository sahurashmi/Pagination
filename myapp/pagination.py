from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 10

class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE                #page no.
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size' #page size->how many records you want in a single page

    def get_paginated_response(self, data):
        #breakpoint()

        page = self.request.GET.get('page')
        if page is None:
            return Response({"message":"Hey ! your page number is not valid","data":data}) 
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },

            'total': self.page.paginator.count,
            'page': int(self.request.GET.get('page',DEFAULT_PAGE)),#, DEFAULT_PAGE)), # can not set default = self.page 
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data    
        })
