from django.shortcuts import render ,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    return HttpResponse("THIS IS CONTACT PAGE")

def about(request):
    return HttpResponse("THIS IS ABOUT PAGE")