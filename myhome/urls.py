from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index),
   path('mycontact/', views.mycontact, name='mycontact'),
   path('register/', views.register, name="register"),
   path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
   path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
   path('developing/', views.developing, name="developing"),
   path('afterreg/', views.afterreg, name="afterreg"),
   path('afterlogin/', views.afterlogin, name="afterlogin"),
]
