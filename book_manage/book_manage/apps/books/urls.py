from django.conf.urls import url
from . import views, ViewGet
from rest_framework.routers import SimpleRouter, DefaultRouter

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^', inclu('books.urls'))
    url(r'^book_sse/$', ViewGet.Books.as_view({'get': 'list', 'post': 'create'})),
    # url(r'^book_drf/(?P<pk>\d+)$', views.BooksDRF.as_view({'put': 'update', 'get': 'retrieve', 'delete': 'destroy'}))
]
router = DefaultRouter()
# defaultrouter 生成的路由同样 他可以在主页访问到
# [<RegexURLPattern books_drf-list ^book_drf/$>,
# <RegexURLPattern books_drf-list ^book_drf\.(?P<format>[a-z0-9]+)/?$>,
# <RegexURLPattern books_drf-detail ^book_drf/(?P<pk>[^/.]+)/$>,
# <RegexURLPattern books_drf-detail ^book_drf/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$>,
# <RegexURLPattern books_drf-lastdata ^book_drf/(?P<pk>[^/.]+)/lastdata/$>,
# <RegexURLPattern books_drf-lastdata ^book_drf/(?P<pk>[^/.]+)/lastdata\.(?P<format>[a-z0-9]+)/?$>,
# <RegexURLPattern api-root ^$>, <RegexURLPattern api-root ^\.(?P<format>[a-z0-9]+)/?$>]
# router.register('book_sse', ViewGet.Books)
# print(router.urls)
# urlpatterns += router.urls

router.register('book_drf', views.BooksDRF, basename='books_drf')
print(router.urls)
urlpatterns += router.urls
