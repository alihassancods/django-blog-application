from django.urls import path
from .views import testView,post_list,post_detail
app_name = 'blog'
# You can see all the path converters provided by 
# Django at https://docs.djangoproject.com/en/5.0/topics/http/urls/#path-converters.
urlpatterns = [
    path('testview',testView,name='testview'),
    path('posts',post_list,name = 'post_list'),
    path('post/<int:id>',post_detail,name='post_detail'),
]
# If using path() and converters isn’t sufficient for you, you can use re_path() instead to define complex 
# URL patterns with Python regular expressions. You can learn more about defining URL patterns with 
# regular expressions at https://docs.djangoproject.com/en/5.0/ref/urls/#django.urls.re_path. 