from django.shortcuts import render,HttpResponse


def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def Reikihealing(request):
    return render(request, 'Reikihealing.html')

def tarotcardreading(request):
    return render(request, 'tarotcardreading.html')

def lamaferahealing(request):   
    return render(request, 'lamaferahealing.html')

def pendulumdowsing(request):
    return render(request, 'pendulumdowsing.html')

def certifications(request):
    return render(request, 'certifications.html')

