
from django.urls import path, include
from students import views 



urlpatterns = [
    path('create',views.create,name='create'),
    path('<int:student_id>',views.detail,name='detail'),
]
