from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('doc/',views.doc,name="doc"),
    path('docview/',views.docview,name="docview"),
    path('heart/', views.heart, name="heart"),
    path('diabetes/', views.diabetes, name="diabetes"),
    path('breast/', views.breast, name="breast"),
    path('register/', views.register, name="register"),
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('log/', views.log, name="log"),
    path('log1/', views.log1, name="log1"),
    path('predict/', views.predict, name="predict"),
    path('feed/', views.feed, name="feed"),
    path('feed1/', views.feed1, name="feed1"),
    path('feed2/', views.feed2, name="feed2"),
    path('general/', views.general, name="general"),
 
    path('booking/', views.booking, name="booking"),
    path('result/', views.result, name="result"),

]
