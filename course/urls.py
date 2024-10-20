from django.urls import path
from . import views
from django.shortcuts import render
from .models import Course, Certificate

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('courses/', views.courses, name='courses'),

    # Home pages for different user groups
    path('admin-home/', views.admin_home, name='admin_home'),
    path('trainer-home/', views.trainer_home, name='trainer_home'),
    path('learner-home/', views.learner_home, name='learner_home'),

    # Pages for specific functionalities
    path('users/', views.users_list, name='users_list'),
    path('branches/', views.branches, name='branches'),  # Bu satırı ekleyin
    path('course-list/', views.course_list, name='course_list'),  # Bu satırı ekleyin
    path('groups/', views.groups, name='groups'),
    path('grading-hub/', views.grading_hub, name='grading_hub'),
    path('calendar/', views.calendar, name='calendar'),
    path('trainer-courses/', views.trainer_courses, name='trainer_courses'),

    # Reports for Admin
    path('reports/users/', views.report_users, name='report_users'),
    path('reports/courses/', views.report_courses, name='report_courses'),
    path('reports/branches/', views.report_branches, name='report_branches'),
    path('reports/groups/', views.report_groups, name='report_groups'),
    path('reports/learning-activities/', views.learning_activities, name='learning_activities'),
    path('reports/training-matrix/', views.training_matrix, name='training_matrix'),
    path('reports/timeline/', views.timeline, name='timeline'),

    # Additional reports and functionalities
    path('account-settings/', views.account_settings, name='account_settings'),
    path('course-report/<int:course_id>/', views.course_report, name='course_report'),
]

def course_report(request, course_id):
    course = Course.objects.get(id=course_id)
    students = course.students.all()
    certificates = Certificate.objects.filter(course=course)

    context = {
        'course': course,
        'students': students,
        'certificates': certificates,
    }
    return render(request, 'reports/course_report.html', context)

from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # diğer URL'ler...
]
