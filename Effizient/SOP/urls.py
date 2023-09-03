from django.urls import path
from SOP import views

urlpatterns = [
    # path('login',views.login,name='login'),
    path('sopform', views.sopform, name='sopform'),
    path('success', views.success, name='success'),
]
