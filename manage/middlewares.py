from django.core.cache import cache

import threading

THREAD_LOCAL = threading.local()

class TenantMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        print("IN Call")
        cache.set("DB", "normal", nx=True)
        setattr(THREAD_LOCAL, "DB", cache.get("DB"))
        response = self.get_response(request)
        print(request.META['USER'])
        return response

    def process_view(self,request, view_func, *view_args, **view_kwargs):
        print(request)
        if(request.META['USER'] == 'root'):
            cache.set("DB", "root")
        setattr(THREAD_LOCAL, "DB", cache.get("DB"))

def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB")

def set_db_for_router(db):
    setattr(THREAD_LOCAL,"DB", db)
