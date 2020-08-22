from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', inclu('books.urls'))
    url(r'^book_drf$', views.BooksDRF.as_view({'get': 'list', 'post': 'create'})),
    url(r'^book_drf/(?P<pk>\d+)$', views.BooksDRF.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}))
]
