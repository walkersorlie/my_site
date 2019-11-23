from homepage.models import AboutContent


class AboutContentBlock:
    def __init__(self, get_response):
        # One-time configuration and initialization.
        self.get_response = get_response


    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        """
        Add to session? Cache?
        """
        request.about_content_block = AboutContent.objects.last()

        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called.

        return response
