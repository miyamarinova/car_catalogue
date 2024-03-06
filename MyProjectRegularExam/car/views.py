from django.forms import modelform_factory
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from MyProjectRegularExam.account.views import get_profile
from MyProjectRegularExam.car.forms import CreateCarForm
from MyProjectRegularExam.car.models import Car

class ReadOnlyMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"
        return form
# Create your views here.
def create_car(request):
    form = CreateCarForm(request.POST or None)
    profile = get_profile()
    if form.is_valid():
        form.instance.owner_id = profile.pk
        form.save()
        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'car/car-create.html', context)

class DetailCarView(views.DetailView):
    queryset = Car.objects.all()
    template_name = "car/car-details.html"

class EditCarView(views.UpdateView):
    queryset = Car.objects.all()
    template_name = "car/car-edit.html"
    fields = ['type','model', 'year', 'image_url', 'price']
    success_url = reverse_lazy('catalogue')

class DeleteCarViews(ReadOnlyMixin, views.DeleteView):
    queryset = Car.objects.all()
    template_name = 'car/car-delete.html'
    fields = ['type','model', 'year', 'image_url', 'price']
    success_url = reverse_lazy('catalogue')
    form_class = modelform_factory(
        Car,
        fields=['type','model', 'year', 'image_url', 'price'],
    )
    def get_form_kwargs(self):
        kwargs=super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs
