import datetime
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone

from .models import Question


def index(request):
    latest_question_list = get_list_or_404(Question, pub_date__date__gt=timezone.now() - datetime.timedelta(month=1))
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {
        # 'latest_question_list': latest_question_list
    # }
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
