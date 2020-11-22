from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^Hello-view/',views.HelloApiView.as_view()),
]
