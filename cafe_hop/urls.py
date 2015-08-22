from django.conf.urls import patterns, url

from cafe_hop import views

urlpatterns = patterns('',

	#home page
	url(r'^$', views.home, name = 'home'),
	url(r'^rate/(?P<cafe_id>\d+)/$', views.rate, name = 'rate'),
	url(r'^cafes/(?P<cafe_id>\d+)/$', views.cafe, name = 'cafe'),
	url(r'^comment/(?P<cafe_id>\d+)/$', views.comment, name = 'cafe'),
	url(r'^music/', views.music, name = 'music'),
	url(r'^about/', views.about, name = 'about'),
)