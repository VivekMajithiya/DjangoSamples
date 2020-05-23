from django.urls import path
from AppTwo import views

app_name = 'AppTwo'

urlpatterns = [
    path('',views.index,name='index'),
    path('userinfo/',views.userinfo,name='userinfo'),
    path('formpage/',views.formpage,name='formpage'),
    path('usersignup/',views.usersignup,name='usersignup')
]
