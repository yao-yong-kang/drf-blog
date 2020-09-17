
from django.contrib import admin
from django.urls import path,include

from . import views
app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/list/', views.article_list, name='article_list'),

]
