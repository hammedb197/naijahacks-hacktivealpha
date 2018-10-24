from django.shortcuts import render
from .apps import load_model
# Create your views here.

def index(request):

    # context = {'home_page': home_page}
    return render(request, 'phish_checker/index.html')

def model_predict(request):

	model = load_model.loaded_model

	return render(request, 'WE are moving on')