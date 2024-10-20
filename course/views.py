from django.shortcuts import render, redirect
from .models import Course, Certificate
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from datetime import datetime
from .models import LearningActivity
from django.contrib import messages
from .forms import AccountSettingsForm
from .models import UserActivity

@login_required
def home(request):
    if request.user.groups.filter(name='Admin').exists():
        return redirect('admin_home')
    elif request.user.groups.filter(name='Trainer').exists():
        return redirect('trainer_home')
    elif request.user.groups.filter(name='Learner').exists():
        return redirect('learner_home')
    else:
        return render(request, 'course/home.html')

@login_required
def courses(request):
    courses = Course.objects.all()  # Burada Course modelinize göre verileri çekebilirsiniz
    context = {
        "courses": courses,
    }
    return render(request, 'course/course_list.html', context)

def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_home')
            elif user.groups.filter(name='Trainer').exists():
                return redirect('trainer_home')
            elif user.groups.filter(name='Learner').exists():
                return redirect('learner_home')
            else:
                return redirect('home')
        else:
            error_message = "Invalid username or password."
    return render(request, 'course/login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_home(request):
    context = get_user_context(request)
    context.update({
        'active_users': User.objects.filter(is_active=True).count(),
        'assigned_courses': 12,
        'training_time': 120,
        'completion_rate': 85,
        'total_users': User.objects.count(),
        'learners': User.objects.filter(groups__name='Learner').count(),
        'trainers': User.objects.filter(groups__name='Trainer').count(),
        'admins': User.objects.filter(groups__name='Admin').count(),
    })
    return render(request, 'course/admin_home.html', context)
@login_required
def users_list(request):
    users = User.objects.all()  # Tüm kullanıcıları çeker
    context = {
        "users": users,
    }
    return render(request, 'course/users.html', context)

@login_required
def course_list(request):
    courses = Course.objects.all()  # Burada Course modelinize göre verileri çekebilirsiniz
    context = {
        "courses": courses,
    }
    return render(request, 'course/course_list.html', context)

@login_required
def trainer_home(request):
    context = get_user_context(request)
    context.update({
        'recent_courses': [
            {"name": "Kriz Yönetimi", "status": "Completed 😊"},
            {"name": "Project Management", "status": "Completed 😊"},
            {"name": "What is TalentLibrary?", "status": "Completed 😊"},
        ],
        'calendar_events': [
            {"date": "2024-09-01", "event": "Training A"},
            {"date": "2024-09-15", "event": "Training B"},
        ],
        'completed_assessments': 5,
        'completed_trainings': 10,
        'overall_points': 1500,
        'total_assigned_trainings': 20,
        'completed_trainings_stat': 10,
        'total_training_time': 120,
        'successful_tests': 8,
    })
    return render(request, 'course/trainer_home.html', context)
@login_required
def trainer_courses(request):
    courses = Course.objects.all()  # Burada kendi Course modelinize göre verileri çekebilirsiniz.
    context = {
        "courses": courses,
    }
    return render(request, 'course/trainer_courses.html', context)


@login_required
def learner_home(request):
    context = get_user_context(request)
    context.update({
        'recent_courses': [
            {"name": "Kriz Yönetimi", "status": "Tamamlandı 😊"},
            {"name": "Project Management", "status": "Tamamlandı 😊"},
        ],
        'today': datetime.today().strftime('%d/%m/%Y, %H:%M'),
        'points': 525,
        'level': 1,
        'badges': 3,
        'trainings': 2,
        'completed_assignments': 0,
        'submitted_comments': 0,
        'total_training_time': 1,
        'successful_tests': 1,
    })
    return render(request, 'course/learner_home.html', context)

def get_user_context(request):
    return {
        'is_admin': request.user.groups.filter(name='Admin').exists(),
        'is_trainer': request.user.groups.filter(name='Trainer').exists(),
        'is_learner': request.user.groups.filter(name='Learner').exists(),
    }

@login_required
def groups(request):
    return render(request, 'course/groups.html')

@login_required
def branches(request):
    # Bu fonksiyonda branch verilerini işleyebilirsiniz.
    # Şu an için basit bir placeholder olarak aşağıdaki kodu kullanabilirsiniz.
    branches = []  # Burada Branch modelinize göre verileri çekebilirsiniz
    context = {
        "branches": branches,
    }
    return render(request, 'course/branches.html', context)

@login_required
def grading_hub(request):
    return render(request, 'course/grading_hub.html')

@login_required
def calendar(request):
    return render(request, 'course/calendar.html')

@login_required
def trainer_courses(request):
    courses = Course.objects.all()
    return render(request, 'course/trainer_courses.html', {"courses": courses})

@login_required
def training_matrix(request):
    return render(request, 'course/training_matrix.html', {"matrix_data": []})

@login_required
def timeline(request):
    return render(request, 'course/timeline.html', {"timeline_data": []})

@login_required
def report_users(request):
    users = User.objects.all()
    context = {
        "users": users,
    }
    return render(request, 'course/report_users.html', context)

# Report for Courses
@login_required
def report_courses(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, 'course/report_courses.html', context)

# Report for Branches
@login_required
def report_branches(request):
    branches = []  # Örnek veri, bu listeyi Branch modeliyle değiştirin.
    context = {
        "branches": branches,
    }
    return render(request, 'course/report_branches.html', context)

# Report for Groups
@login_required
def report_groups(request):
    groups = Group.objects.all()
    context = {
        "groups": groups,
    }
    return render(request, 'course/report_groups.html', context)

# Learning Activities Report
@login_required
def learning_activities(request):
    activities = LearningActivity.objects.all()
    context = {
        "activities": activities,
    }
    return render(request, 'course/learning_activities.html', context)

# Account & Settings
@login_required
def account_settings(request):
    if request.method == 'POST':
        form = AccountSettingsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account settings have been updated successfully.')
            return redirect('account_settings')
    else:
        form = AccountSettingsForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'course/account_settings.html', context)

# Example Course Report Detail
@login_required
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


def admin_dashboard(request):
    timeline_logs = UserActivity.objects.order_by('-timestamp')[:10]  # Son 10 eylemi alır
    context = {
        'timeline_logs': timeline_logs,
        # Diğer veriler...
    }
    return render(request, 'course/admin_dashboard.html', context)
