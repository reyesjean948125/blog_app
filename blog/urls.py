from django.conf.urls import url
from .views import index, view_blog, add_blog, update_blog, delete_comment

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^view_blog/(?P<blog_id>\d+)$', view_blog, name="view-blog"),
	url(r'^add_blog$', add_blog, name='add-blog'),
	url(r'^update_blog/(?P<blog_id>\d+)$', update_blog, name='update-blog'),
	url(r'^delete_comment/(?P<comment_id>\d+)$', delete_comment, name='delete-comment'),
]