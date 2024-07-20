from django.urls import path

from .views import home_page_view, about_page_view, AboutPageView

urlpatterns = [
    path("", home_page_view, name="home"),
    path("about/", about_page_view, name="about"),
]