from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('cbv/', views.HomeView.as_view(), name='cbv_home'),
    path('cbv/gtv/', views.MyTemplateView.as_view(), name='generic_template_view'),

    # without defining a view just use this url to render a static template without passing any coontext data
    path('gtv/', TemplateView.as_view(template_name='articles/cvb_home.html'), name='gtv'),

    # url for the FormHandleView
    path('cbv/formview/', views.FormHandleView.as_view(), name='form_view'),

    # Create Article
    path('article/create/', views.ArticleCreateView.as_view(), name='create_article'),

    # Article list
    path('article/list/', views.ArticleList.as_view(), name='article_list'),

    # Article detial
    path('article/<int:pk>/<str:slug>/detail/', views.ArticleDetailView.as_view(), name='article_detail'),

    # Article update
    path('article/<int:pk>/<str:slug>/update/', views.ArticleUpdateView.as_view(), name='article_update'),

    # Article delete
    path('article/<int:pk>/<str:slug>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),

]
