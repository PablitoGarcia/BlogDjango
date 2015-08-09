from django.contrib import admin
from django.conf.urls import include, url
urlpatterns = [
   
     url(r'^', include('blog.urls', namespace = "app_blog")),
     url(r'^admin/', include(admin.site.urls)),
]
