"""thelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from profile import Profile

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from thelp.add_views.views import export_excel, get_client_ip
from thelp.views import TaskView, TaskPanelView, TaskToDoView, ReportView, ReportUserView, MonthlyReportView, \
    AnnualReportView, CommonReportView
from thelp.views_ext.accounts import LogoutView, ProfileView, RegisterView

urlpatterns = [
    path('', TaskView.as_view(), name="homepage"),
    path('tasks/', TaskPanelView.as_view(), name="tasks"),
    path('report/', ReportView.as_view(), name="report"),
    path('report_user/', ReportUserView.as_view(), name="report_user"),
    path('report/monthly_report', MonthlyReportView.as_view(), name="monthly_report"),
    path('report/annual_report', AnnualReportView.as_view(), name="annual_report"),
    path('report/common_report', CommonReportView.as_view(), name="common_report"),
    path('tasks/<int:task_id>/', TaskToDoView.as_view(), name="task"),
    path('export_excel/', export_excel, name="export-excel"),
    path('get_client_ip/', get_client_ip, name="get-client-ip"),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', ProfileView.as_view()),
    path('admin/', admin.site.urls),
]
