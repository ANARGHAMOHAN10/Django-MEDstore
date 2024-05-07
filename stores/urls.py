from django.urls import path
from stores import views
urlpatterns=[
    path('',views.home,name=''),
    path('register',views.register,name='register'),
    path('my-login',views.my_login,name='my-login'),
    path('user-logout',views.user_logout,name='user-logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create-record',views.create_record,name='create-record'),
    path('update-record/<int:pk>/',views.update_record,name='update-record'),
    path('delete/<int:pk>/',views.delete_record,name='delete'),
    path('searchlist',views.search,name='searchlist')


]