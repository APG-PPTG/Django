from django.http import HttpResponse

class AppMaintennceMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # We are not passing this req to view maintenance issue
        return HttpResponse("<h1> Currently application under Maintenance please try after 2 days</h1>")
