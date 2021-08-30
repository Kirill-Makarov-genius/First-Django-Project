from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('show_post/<slug:post_slug>', ShowPost.as_view(), name="show_post"),
    path('category/<slug:cat_slug>', Categories.as_view(), name="categories"),
    path('about', about, name='about'),
    path('add_post', AddPost.as_view(), name='add_post'),
    path('work', work, name='work'),
    path("accounts/register", RegisterUser.as_view(), name="register")
]
