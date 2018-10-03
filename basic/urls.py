from django.conf.urls import url
from django.urls import path
from basic import views

app_name = 'basic'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'member/', views.Member.as_view()),
]