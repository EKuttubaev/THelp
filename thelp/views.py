import datetime

from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from ipware import get_client_ip

from thelp.forms import TaskForm, CommentForm
from thelp.models import Task, Comment


class TaskView(TemplateView):
    template_name = "index.html"

    def dispatch(self, request, *args, **kwargs):
        form = TaskForm()
        ip = request.META["HTTP_X_REAL_IP"]

        if request.method == "POST":
            form = TaskForm(request.POST)
            print(ip)
            if form.is_valid():
                form = form.save(commit=False)
                form.ip = ip
                form.save()
                return redirect("/")

        return render(request, self.template_name, {
            "form": form,
            "ip": ip
        })


class TaskPanelView(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        tasks = Task.objects.all().filter(status_done=False)
        return render(request, "task_panel.html", context={
            "tasks": tasks
        })


class TaskToDoView(TemplateView):
    template_name = "add_comment.html"

    def dispatch(self, request, *args, **kwargs):
        form = CommentForm()
        task_id = kwargs["task_id"]
        task = Task.objects.get(id=task_id)
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.name = request.user
                if task.status_done == False:
                    task.status_done = True
                    task.save()
                    form.save()
                    return redirect("/")
        return render(request, self.template_name, {"form": form})


class ReportView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        current_year = datetime.date.today().year
        current_months = datetime.date.today().month
        current_day = datetime.date.today().day
        previos_year = current_year - 1

        active_tasks = Task.objects.all().filter(status_done=False)
        count_active_tasks = Task.objects.all().filter(status_done=False).count()
        non_active_tasks = Task.objects.all().filter(status_done=True)
        count_non_active_tasks = Task.objects.all().filter(status_done=True).count()
        tasks_for_this_year = Task.objects.all().filter(status_done=True).filter(
            time_and_date__year=current_year).count()
        tasks_for_previos_year = Task.objects.all().filter(status_done=True).filter(
            time_and_date__year=previos_year).count()
        tasks_for_this_months = Task.objects.all().filter(status_done=True).filter(
            time_and_date__month=current_months).count()
        tasks_for_today = Task.objects.all().filter(time_and_date__day=current_day).count()

        return render(request, "report.html", context={
            "active_tasks": active_tasks,
            "count_active_tasks": count_active_tasks,
            "non_active_tasks": non_active_tasks,
            "count_non_active_tasks": count_non_active_tasks,
            "tasks_for_this_year": tasks_for_this_year,
            "tasks_for_previos_year": tasks_for_previos_year,
            "tasks_for_this_months": tasks_for_this_months,
            "tasks_for_today": tasks_for_today
        })


class ReportUserView(TemplateView):
    template_name = "report_of_user.html"

    def dispatch(self, request, *args, **kwargs):
        current_day = datetime.date.today().day
        # user = User.objects.all()#.annotate(ratings=Count('comment'))
        u_for_day = Comment.objects.filter(timedate_of_comment__day=current_day).order_by("name__username").values(
            "name__username").annotate(num=Count('comment'))

        return render(request, self.template_name, context={
            # "users": users,
            "u_for_day": u_for_day
        })


class MonthlyReportView(TemplateView):
    template_name = "report/monthly_report.html"

    def dispatch(self, request, *args, **kwargs):
        current_months = datetime.date.today().month
        u_for_months = Comment.objects.filter(timedate_of_comment__month=current_months).order_by(
            "name__username").values("name__username").annotate(num=Count('comment'))
        return render(request, self.template_name, context={
            # "users": users,
            "u_for_months": u_for_months,
        })


class AnnualReportView(TemplateView):
    template_name = "report/annual_report.html"

    def dispatch(self, request, *args, **kwargs):
        current_year = datetime.date.today().year
        u_for_year = Comment.objects.filter(timedate_of_comment__year=current_year).order_by("name__username").values(
            "name__username").annotate(num=Count('comment'))
        return render(request, self.template_name, context={
            # "users": users,
            "u_for_year": u_for_year
        })


class CommonReportView(TemplateView):
    template_name = "report/common_report.html"

    def dispatch(self, request, *args, **kwargs):
        common = Comment.objects.order_by("name__username").values("name__username").annotate(num=Count('comment'))
        return render(request, self.template_name, context={
            # "users": users,
            "common": common
        })
