from django.urls import path
from exam import views
urlpatterns = [
    path('',views.index,name='index')
]