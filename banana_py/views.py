from django.conf import settings
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from banana_py import Bananas_OAuth


class BananasCompleteView(TemplateView):
    template_name = 'banana_py/fail.html'

    def get(self, request):
        Bananas_OAuth().on_complete(request)
        return HttpResponseRedirect(settings.MAILCHIMP_COMPLETE_URI)
