from django.urls import path, re_path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from .views import get_files, create_file, file_detail
from .views import *
urlpatterns = [
    path('', homepage),
    re_path('login', login),
    re_path('signup', signup),
    re_path('test_token', test_token),
    path('test_ai', test_ai),
    path('files', files),
    path('files/<int:pk>', file_detail, name='file_detail'),
    path('files/create/', create_file, name='create_file'),
]

urlpatterns += staticfiles_urlpatterns()
