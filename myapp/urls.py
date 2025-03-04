from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.user_List),
    path('Add/', views.add_user),

]