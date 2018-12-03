from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name= 'index.html'


class AboutPageView(TemplateView):
	template_name = 'about.html'


class ContactusPageView(TemplateView):
	template_name = 'contactus.html'


