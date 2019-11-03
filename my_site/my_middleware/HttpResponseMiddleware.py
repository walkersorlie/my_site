from django.shortcuts import render


class HttpResponseNotAllowed:
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response


    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called.

        if response.status_code == 405:
            return render(request, '405.html', status=405)

        return response
