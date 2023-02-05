from django.http import HttpResponse
class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    #if view function raises error
    def process_exception(self, request, exception):
        return HttpResponse(f'<h1>Currently we are facing some technical problem <br> The raised exception is:{exception.__class__.__name__}<br> The exception Messgae is:{exception}</h1>')
