from django.shortcuts import render

# Create your views here.

def index(request):

    # context = {'home_page': home_page}
    return render(request, 'phish_checker/index.html')
