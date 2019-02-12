from django.views.generic.base import TemplateView
from django.conf import settings


class HomePageView(TemplateView):

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branding'] = settings.GEO_BRANDING
        return context

class AboutPageView(TemplateView):

    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branding'] = settings.GEO_BRANDING
        return context
