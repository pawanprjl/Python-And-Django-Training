from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


# Create your views here.
def index(request):
    question = Question.objects.get(pk=1)
    context = {
        'choice_list': question.choice_set.all(),
    }
    return render(request, 'polls/index.html', context)