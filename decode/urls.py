from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from decode import views

urlpatterns = [
    url(r'^decode/$', views.DecodeList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)