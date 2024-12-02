from django.urls import path
from . import views

urlpatterns = [
    # Course URLs
    path('course/list/', views.course_list, name='course_list'),
    path('course/add/', views.course_create, name='course_add'),
    path('course/edit/<int:pk>/', views.course_update, name='course_edit'),
    path('course/delete/<int:pk>/', views.course_delete, name='course_delete'),

    # path('course/details/<int:pk>/', views.CourseDetail, name='course_details'),

    # Question URLs
    path('question/list/', views.question_list, name='question_list'),
    path('question/add/', views.question_create, name='question_add'),
    path('question/edit/<int:pk>/', views.question_update, name='question_edit'),
    path('question/delete/<int:pk>/', views.question_delete, name='question_delete'),

    # Student URLs
    path('student/list/', views.student_list, name='student_list'),
    path('student/add/', views.student_create, name='student_add'),
    path('student/edit/<int:pk>/', views.student_update, name='student_edit'),
    path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),
    # Tutorial URLs
    path('tutorial/list/', views.tutorial_list, name='tutorial_list'),
    path('tutorial/add/', views.tutorial_create, name='tutorial_add'),
    path('tutorial/edit/<int:pk>/', views.tutorial_update, name='tutorial_edit'),
    path('tutorial/delete/<int:pk>/', views.tutorial_delete, name='tutorial_delete'),
    # Instructor URLs
    path('instructor/list/', views.instructor_list, name='instructor_list'),
    path('instructor/add/', views.instructor_create, name='instructor_add'),
    path('instructor/edit/<int:pk>/', views.instructor_update, name='instructor_edit'),
    path('instructor/delete/<int:pk>/', views.instructor_delete, name='instructor_delete'),
    # Topic URLs
    path('topic/list/', views.topic_list, name='topic_list'),
    path('topic/add/', views.topic_create, name='topic_add'),
    path('topic/edit/<int:pk>/', views.topic_update, name='topic_edit'),
    path('topic/delete/<int:pk>/', views.topic_delete, name='topic_delete'),
    # Result URLs
    path('result/list/', views.result_list, name='result_list'),
    path('result/add/', views.result_create, name='result_add'),
    path('result/edit/<int:pk>/', views.result_update, name='result_edit'),
    path('result/delete/<int:pk>/', views.result_delete, name='result_delete'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
