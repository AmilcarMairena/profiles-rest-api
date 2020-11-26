from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('hello-viewset',views.HelloViewSet,base_name='hello_viewset')

urlpatterns = [
    url(r'^Hello-view/',views.HelloApiView.as_view()),
    url(r'',include(router.urls))
]
