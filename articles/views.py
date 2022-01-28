from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.views.generic import TemplateView

def home(request):
    return render(request, 'articles/home.html')


class HomeView(View):

    def get(self, request):
        context = {}
        now = timezone.now()
        context['now'] = now
        return render(request, 'articles/cvb_home.html', context)


# Render a static template in more allegiant way
# If we need pass context data then we can use get_context_data() in more allegiant way
# instead of extending the get method
# Note : we can also render the static template only by defining the url(when we don't have to pass context data')
class MyTemplateView(TemplateView):
    template_name = 'articles/cvb_home.html'

    # Pass context data
    # First of all we have to call the super().get_context_data() to use default feature
    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['now'] = timezone.now()
        return context
