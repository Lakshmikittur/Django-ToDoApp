from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import TaskForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

@login_required
def home_view(request):

    search_input = request.GET.get('search') or ''
    if search_input:
        all_tasks = Task.objects.filter(user=request.user, title__icontains = search_input) 
        # context = {
        # "tasks": all_tasks
        # } 
        # return render(request, 'tasks/home.html', context)

    else:
        all_tasks = Task.objects.filter(user=request.user)

    
    # context = {
    #     "tasks": all_tasks
    # } 

    paginator = Paginator(all_tasks, 1) 
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'tasks/home.html', context)

@login_required
def task_detail_view(request, id):
    obj = get_object_or_404(Task, id=id)

    if obj.user == request.user:
        context = {
        "task":obj
        }
        return render(request, 'tasks/task_detail.html', context)
    else:
        #raise PermissionDenied("You do not have permission to view this task")
        return HttpResponseForbidden()


@login_required
def create_task_view(request):

    form = TaskForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            #form.save()
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("../")
    
    context = {
        "form":form
    }

    return render(request, "tasks/create_task.html", context)

@login_required  
def update_task_view(request, id):
    obj = get_object_or_404(Task, id=id)
    if obj.user!= request.user:
        #raise PermissionDenied("You do not have permission to update this task")
        return HttpResponseForbidden()

    else:
        form = TaskForm(request.POST or None, instance=obj)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("../")
        
        context = {
            "form":form
        }

        return render(request, "tasks/create_task.html", context)

@login_required
def delete_task_view(request, id):
    obj = get_object_or_404(Task, id=id)

    if obj.user!= request.user:
        #raise PermissionDenied("You do not have permission to update this task")
        return HttpResponseForbidden()

    else:
        if request.method == "POST":
            obj.delete()
            return redirect("../")

        context = {
            "task":obj
        }

        return render(request, "tasks/delete_task.html", context)

def mainview(request):
    return render(request, "tasks/main_view.html", {})