from django.conf.urls import url
from django.contrib import admin

from menu.views import page, sub1, sub2, sub2_1, sub2_2

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', page, name='page'),
    url(r'^sub1/$', sub1, name='sub1'),
    url(r'^sub2/$', sub2, name='sub2'),
    url(r'^sub2-1/$', sub2_1, name='sub2_1'),
    url(r'^sub2-2/$', sub2_2, name='sub2_2'),
]
