from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    contact_info ={
        'Name' : 'Samudro Sinha',
        'Contact' : '12345678'
    }
    return JsonResponse(contact_info)
