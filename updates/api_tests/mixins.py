from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class HttpResponseMixin:
    is_json = False

    def render_response(self, data, status=200):
        content_type = "text/html"
        if self.is_json:
            content_type = "application/json"
        return HttpResponse(data, content_type=content_type, status=status)
