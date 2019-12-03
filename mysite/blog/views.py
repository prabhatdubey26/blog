from django.shortcuts import render ,HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("This Is blogHOME PAGE we will keep all post")

def blogPost(request, slug):
    return HttpResponse(f"THIS IS BLOGPOST PAGE {slug} ")