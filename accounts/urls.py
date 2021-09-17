from django.urls import path

from . import views
urlpatterns = [
	path('', views.home, name="home"),
	path('login', views.login, name="login"),
	path('admin_panel', views.admin_panel, name="admin_panel"),
	path('logout', views.logout_view, name="logout"),
	
]