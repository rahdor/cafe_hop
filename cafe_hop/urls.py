from django.conf.urls import patterns, url

from cafe_hop import views

urlpatterns = patterns('',

	#home page
	url(r'^$', views.home, name = 'home'),
	url(r'^rate/(?P<cafe_id>\d+)/$', views.rate, name = 'rate'),

)