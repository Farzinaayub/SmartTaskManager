from django.urls import path
from . import views
urlpatterns = [path('', views.dashboard, name="dashboard"),
               path('call_function/', views.call_function, name='call_function'),
               path('tab1/', views.tab1, name="Organize"),
               path('taskpage/<str:pk>/', views.taskpage, name="update"),
               path('tab3/', views.tab3, name="Help"),
               ]
