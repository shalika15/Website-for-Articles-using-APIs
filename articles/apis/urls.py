from django.conf.urls import url
from . import views as api_views

urlpatterns = [
     url(r'^vote/$',api_views.upvote, name='upvote'),

]