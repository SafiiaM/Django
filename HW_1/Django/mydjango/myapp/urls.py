from django.urls import path
# from . import views
from .views import MainPageView, AboutView

urlpatterns = [
# path('', views.index, name='index'),
# path('about/', views.about, name='about'),

    path('', MainPageView.as_view(), name='main_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    ]