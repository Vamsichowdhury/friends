
from django.urls import path,include
from myapp import views

app_name='myapp'

urlpatterns = [
  	path('',views.home,name='home'),
    path('index/',views.index,name='index'),
	path('forms/',views.forms,name='forms'),
    path("remove/<int:pk>/",views.remove_name,name='remove_name'),
    path("removeall/",views.remove_all,name='remove_all'),
    path("login/",views.login_user,name='login_user'),
    path("logout/",views.logout_user,name='logout_user'),
    
]
