from django.shortcuts import redirect, render

from MyProjectRegularExam.account.views import get_profile
from MyProjectRegularExam.car.forms import CreateCarForm
from MyProjectRegularExam.car.models import Car


# Create your views here.
def create_car(request):
    form = CreateCarForm(request.POST or None)
    profile = get_profile()
    if form.is_valid():
        form.instance.owned_id = profile.pk
        form.save()

        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'car/car-create.html', context)



