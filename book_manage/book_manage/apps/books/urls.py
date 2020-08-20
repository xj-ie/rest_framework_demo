from django.conf.urls import url, include
# from django.contrib import admin
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', inclu('books.urls'))
    url(r'^book_drf$', views.Books.as_view()),
    url(r'^book_drf/(?P<pk>\d+)$', views.Books_update.as_view())
]
