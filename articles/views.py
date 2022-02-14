from django.shortcuts import render
from django.core.exceptions import ImproperlyConfigured
from django.views import View
from django.utils import timezone
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django.urls import reverse
from .forms import ArticleForm
from .models import Article


# Django Mixin
# Mixin is not too hard, It is a concept like "Multiple Inheritance"
# Using mixin we can inherit multiple class, we can manage "DRY" concept. DRY(Don't Repeat Yourself')
# In a mixin we can override default methods or add some extra feature
class TitleMixin:
    page_title = ''

    @property
    def get_page_title(self):
        return self.page_title

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['notice'] = 'This message from admin panel.'
        context['page_title'] = self.get_page_title
        return context


def home(request):
    return render(request, 'articles/home.html')


class HomeView(View):
    page_title = ' - Home'

    def get(self, request):
        dict = {}
        now = timezone.now()
        dict['now'] = now
        dict['page_title'] = self.page_title
        return render(request, 'articles/cvb_home.html', dict)


# Render a static template in more allegiant way
# If we need pass context data then we can use get_context_data() in more allegiant way
# instead of extending the get method
# Note : we can also render the static template only by defining the url(when we don't have to pass context data')
class MyTemplateView(TitleMixin, TemplateView):
    template_name = 'articles/cvb_home.html'
    page_title = ' - Template View'

    # Pass context data
    # First of all we have to call the super().get_context_data() to use default feature
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



    # To handle form the generic FormView will work
class FormHandleView(TitleMixin, FormView):
    form_class = ArticleForm
    template_name = 'articles/create_article.html'
    page_title = ' - FormView'
    # success_url = '/cbv/gtv/' #hard coded url


    # we can also define the get_success_url() methd
    def get_success_url(self):
        return reverse('article_list')


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
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['articles'] = Article.objects.all()
#         return context


class PublicMixin:
    is_public_field = 'is_public'

    @property
    def get_is_public(self):
        return {self.is_public_field:True}

    def get_queryset(self):
        if self.model:
            return self.model._default_manager.filter(**self.get_is_public)
        elif self.queryset:
            return self.queryset.filter(**self.get_is_public)
        else:
            raise ImproperlyConfigured(
                '%(cls)s.model not found. Define '
                'queryset' %{'cls':self.__class__.__name__}
            )

# Article list in Generic ListView
class ArticleList(TitleMixin, PublicMixin, ListView):
    """"ListView need a queryset, model.objects or override the get_queryset() method
        This ArticleList Class is inheriting mixin(TitleMixin)
        and that's why the title list page is showing the sub title ' - Articles'
     """
    template_name = 'articles/article_list.html'
    model = Article
    page_title = ' - Articles'
    # queryset = Article.objects.filter(is_public=True)

    # if we need to render extra context variable then we have to override the
    # get_context_data() method
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['articles'] = context.get('object_list')
    #     context['notice'] = 'This message from admin panel.'
    #     return context



class ArticleDetailView(TitleMixin, DetailView):
    template_name = 'articles/article_detail.html'
    model = Article
    query_pk_and_slug = True
    # page_title = ' - Article details' # hard coded page title

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        self.page_title = ' - ' + obj.title
        return obj
