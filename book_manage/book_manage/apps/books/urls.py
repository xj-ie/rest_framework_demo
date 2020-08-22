from django.conf.urls import url
from . import views
from rest_framework.routers import SimpleRouter

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', inclu('books.urls'))
    # url(r'^book_drf$', views.BooksDRF.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^book_drf/(?P<pk>\d+)$', views.BooksDRF.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}))
]
router = SimpleRouter()
router.register('book_drf', views.BooksDRF, basename='books_drf')
print(router.urls)
urlpatterns += router.urls
