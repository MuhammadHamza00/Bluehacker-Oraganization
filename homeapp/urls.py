from django.contrib import admin
from django.urls import path
from homeapp import views
from django.urls import path  
from django.contrib import admin  
from django.urls import path
# from homeapp.views import SignUpView
from homeapp import views
from . import views


urlpatterns = [ 
    path("", views.index, name='index'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("defenders", views.defenders, name='defenders'),
    path("invader", views.invader, name='invader'),
    path("login",views.login,name="login"),
    path("logout",views.login,name="logout"),
    path('registration', views.signUp, name= 'signUp/'),
    path("pricing",views.pricing,name="pricing"),  
    path("thanks",views.thanks,name="thanks"),
        
]
#waqarbajwa200 zoo@Animal  ads123t5io
    # path("signup",views.signUp,name="signUp"),
    # # path('signup/', SignUpView.as_view(), name='signup'),  