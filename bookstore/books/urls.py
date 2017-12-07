from django.conf.urls import url
from books import views


urlpatterns = [
    url(r'^index',views.index,name='index'),
    url(r'books/(?P<book_id>\d+)/$', views.detail, name='detail'),
]