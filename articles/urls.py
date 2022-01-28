from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cbv/', views.HomeView.as_view(), name='cbv_home'),
    path('cbv/gtv/', views.MyTemplateView.as_view(), name='generic_template_view'),

    # without defining a view just use this url to render a static template without passing any coontext data
    path('gtv/', TemplateView.as_view(template_name='articles/cvb_home.html'), name='gtv'),
]
