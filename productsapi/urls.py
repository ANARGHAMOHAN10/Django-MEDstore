from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signupapi'),
    path('logins',views.logins,name='loginsapi'),
     path('create',views.create_product,name='createapi'),
     path('listproduct',views.list_product,name='listproductapi'),
     path('updateproduct/<int:pk>/',views.update_product,name='updateproductapi'),
     path('deleteproduct/<int:pk>/',views.delete_product,name='deleteproductapi'),
     path('searchproduct',views.search_product,name='searchproductapi'),
     path('logout',views.logout,name='logout')

]
