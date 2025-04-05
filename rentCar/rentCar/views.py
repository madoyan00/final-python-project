from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Car
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CarForm

def index(request):
    template = loader.get_template('rentcar/index.html')
    context = {'username': 'arman', 'password': '1234'}


    return HttpResponse(template.render(context, request))

def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_car")
    else:
        form = CarForm()

    return render(request, "rentCar/add-car.html",{"form": form})
    
    

class CustomLoginView(LoginView):
    template_name = 'rentCar/auth.html'
    
    def get_success_url(self):
        return reverse_lazy('cars')
    

class RegisterPage(FormView):
    template_name = 'rentCar/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('auth')
    
    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('cars')
        
        return super().get(*args, **kwargs)
    
def filter(request):
    return render(request, 'rentCar/filter.html')

def nothification(request):
    return render(request, 'rentCar/nothification.html')

def settings(request):
    return render(request, 'rentCar/settings.html')

def register(request):
    return render(request, 'rentCar/register.html')

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car
    }
    

        

    return render(request, 'rentCar/car_detail.html', context)
   

def rent_car(request):
    cars = Car.objects.all()
    
    brand = request.GET.get('brand')
    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    search_query = request.GET.get('search')

    if search_query:
        cars = cars.filter(brand__icontains=search_query)
    if min_year:
        cars = cars.filter(year__gte=min_year)
    if max_year:
        cars = cars.filter(year__lte=max_year)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if search_query:
        cars = cars.filter(brand__icontains=search_query) | cars.filter(model__icontains=search_query)
        

    return render(request, 'rentCar/rent-car.html', {'cars': cars})

def user(request):
    return render(request, 'rentCar/user.html')

