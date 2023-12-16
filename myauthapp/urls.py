from django.urls import path
from . import views
urlpatterns=[
    path('sign/',views.signup),
    path('login/',views.login),
    path('',views.ListView.as_view())
]