import json
import re

from django.http import HttpResponse
from django.urls import reverse


class PageNotFoundMiddleware(object):
    """
    Middleware for json response on page not found error.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        response = self.get_response(request)
        if (response.status_code == 404 and "application/json" not in response["content-type"]):
            data = {"Error": f"This url {request.path} not found."}
            response = HttpResponse(json.dumps(data), content_type="application/json", status=404)
        return response