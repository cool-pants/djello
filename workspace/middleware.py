from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
    
class SimpleMiddleware:
    def __init__(self, get_response) -> None:
        print("IN init")
        self.get_response = get_response

    def __call__(self, request, *args, **kwds):
        print("IN call")
        response = self.get_response(request)
        print("processed other hooks")
        return response
