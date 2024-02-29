from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from MyProjectRegularExam.account.forms import CreateProfileForm
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

