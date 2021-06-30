from django.urls import path
from common import views


urlpatterns = [
    path('', views.showIndex, name='common_page'),
    path('student/',views.studentPage, name='student'),
    path('student_registration/', views.studenRegistration, name='student_registration')
]