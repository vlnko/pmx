from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "projects/home.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"