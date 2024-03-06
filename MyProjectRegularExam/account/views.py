from django.db.models import Sum
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from MyProjectRegularExam.account.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from MyProjectRegularExam.account.models import Profile
from MyProjectRegularExam.car.models import Car

def get_profile():
    return Profile.objects.first()
# Create your views here.

def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}
    return render(request, template_name='profile/profile-create.html', context=context)

def catalogue(request):
    cars = Car.objects.all()
    context = {
        'profile': get_profile(),
        'cars': cars
    }

    return render(request, template_name='car/catalogue.html', context=context)

class IndexView(views.TemplateView):
    template_name = "web/index.html"

def profile_details_page(request):
    profile = get_profile()
    total_sum = Car.objects\
        .filter(owner=profile, owner__isnull=False)\
        .aggregate(total_price=Sum('price'))['total_price'] or 0

    context = {
        'profile': profile,
        'total_sum': total_sum
    }

    return render(request, template_name='profile/profile-details.html', context=context)

def edit_profile(request):
    profile = get_profile()
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('detail_profile')
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile/profile-edit.html', context)

def delete_profile(request):
    profile = get_profile()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('index')

    context = {
        'form':form,
        'profile': profile
    }

    return render(request, 'profile/profile-delete.html', context)


