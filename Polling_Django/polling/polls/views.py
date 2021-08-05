from django.shortcuts import render

from .models import Question, Choice

# Get Questions and Display them
def index(request):
	return render(request, 'polls/index.html')