from django.conf.urls import url
from .  import views

urlpatterns = [
	url('', views.post_list, name='post_list'),
	url('^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]