from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.views.generic import TemplateView, FormView, ListView
from django.urls import reverse
from .forms import ArticleForm
from .models import Article

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



    # To handle form the generic FormView will work
class FormHandleView(FormView):
    form_class = ArticleForm
    template_name = 'articles/create_article.html'
    # success_url = '/cbv/gtv/' #hard coded url


    # we can also define the get_success_url() methd
    def get_success_url(self):
        return reverse('generic_template_view')


    # To get the valid data as cleaned_data
    def form_valid(self, form):
        # valid data will be process here
        data = form.cleaned_data
        print(data)
        return super().form_valid(form)


    # in the same way we can use the form_invalid() method for process invalid data



# Aticle list view in simple class base view
# class ArticleList(View):
#
#     def get(self, request):
#         context = {}
#         articles = Article.objects.all()
#         context['articles'] = articles
#         return render(request, 'articles/article_list.html', context)



# Article list view using TemplateView
# class ArticleList(TemplateView):
#     template_name = 'articles/article_list.html'
#
#     def get_context_data(self, **kwargs):
#         articles = Article.objects.all()
#         context = super().get_context_data(**kwargs)
#         context['articles'] = articles
#         return context


# Article list in Generic ListView
class ArticleList(ListView):
    template_name = 'articles/article_list.html'
    model = Article

    # if we need to render extra context variable then we have to override the
    # get_context_data() method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['articles'] = context.get('object_list')
        context['notice'] = 'This message from admin panel.'
        return context
