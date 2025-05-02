from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10  # Number of record to shown at one page
    # page_query_param = 'p' #default page lai change garcha
    page_size_query_param = 'records'  # client can decide the page size
    max_page_size = 15  # To limit the page size
    
    def paginate_queryset(self, queryset, request, view=None):         
        pagination_string = request.query_params.get("pagination")
        pagination = False if pagination_string == "false" else True
        if not pagination:
            return None
        return super().paginate_queryset(queryset, request, view)
   
    
class MyLimitOffsetPagination(LimitOffsetPagination):
    pass

    
    
