from django.urls import path

from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('course/one/example', views.course_one_example, name='course_one_example'),
    path('course/one/main', views.course_one_main, name='course_one_main'),
    path('course/two/example', views.course_two_example, name='course_two_example'),
    path('course/two/main', views.course_two_main, name='course_two_main'),
    path('course/three/example', views.course_three_example, name='course_three_example'),
    path('course/three/main', views.course_three_main, name='course_three_main'),
]