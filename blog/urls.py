from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$','blog.views.home', name='home'),
                       url(r'^Curriculum/$', 'blog.views.cv', name='cv'),
                       url(r'^Cronometro/$', 'blog.views.crono', name='crono'),
                       url(r'^Calculadora/$', 'blog.views.calc', name='cal'),
                       url(r'^Imagen/$', 'blog.views.img', name='img'),
                       url(r'^Premio/$', 'blog.views.price', name='price'),
                       url(r'^Conversor/$', 'blog.views.conv', name='conv'),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'blog.views.ver_post', name='vermipost'),
                       url(r'^contactame/$', 'blog.views.contact', name='contactame'),
                       url(r'^save_message/$', 'blog.views.save_message', name='save_message'),
                       url(r'^Principal/$', 'blog.views.principal', name='principal'),
                      )