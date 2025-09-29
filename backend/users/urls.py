from django.urls import path
from .views import RegisterView, CustomLoginView, GetUsersView

app_name = 'users'

urlpatterns =[   
     path('register/', RegisterView.as_view(), name='register'),
     path('login/', CustomLoginView.as_view(), name='login'),
     path('list/', GetUsersView.as_view(), name= 'users-list'),
]
