# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import *
from .forms import CreateWorksheetForm, UserLoginForm
from django.contrib.auth import login, logout
from django.http import JsonResponse


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'worksheet_app/login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'worksheet_app/home.html')

class WorkSheetList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = WorkSheet
    context_object_name = 'worksheets'
    template_name = 'worksheet_app/workSheetList.html'
    paginate_by = 10

    def get_queryset(self):
        return WorkSheet.objects.filter(creating_user_id=self.kwargs['pk'])


@login_required(login_url='/login/')
def create_worksheet_method(request):
    if request.method == 'POST':
        form = CreateWorksheetForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.creating_user = request.user
            listing.save()
            return redirect('create_success')
    else:
        form = CreateWorksheetForm()
    return render(request, 'worksheet_app/createWorksheet.html', context={'form': form})


@login_required(login_url='/login/')
def create_success(request):
    return render(request, template_name='worksheet_app/createSuccess.html')


class DetailWorksheet(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = WorkSheet
    template_name = 'worksheet_app/worksheetDetail.html'
    context_object_name = 'worksheet'


class EditWorksheet(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = WorkSheet
    template_name = 'worksheet_app/worksheetEdit.html'
    form_class = CreateWorksheetForm
    success_url = reverse_lazy('create_success')


class DeleteWorksheet(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = WorkSheet
    template_name = 'worksheet_app/worksheetDelete.html'
    success_url = reverse_lazy('home')


def get_districts(request, *args, **kwargs):
    region_soato = request.GET.get('regionSOATO')
    region = Region.objects.get(soato=region_soato)
    try:
        districts = District.objects.filter(region_id=region.id).order_by('name')
        ls = list(districts.values())
    except Exeption:
        ls = []
    return JsonResponse(ls, safe=False)