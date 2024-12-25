from django.shortcuts import render


# Create your views here.
def home(request):
    # Additional Menu Items

    return render(request, 'home/home.html')
