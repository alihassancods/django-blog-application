from django.urls import path
from .views import testView
app_name = 'blog'
urlpatterns = [
    path('testview',testView,name='testview')
]