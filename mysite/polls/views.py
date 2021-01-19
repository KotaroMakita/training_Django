from django.shortcuts import render

# Create your views here.
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# from django.template import loader

from .models import Choice,Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    # return render(request,'polls/detail.html',{'question'}:question})

    # return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{'question':question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExitst):
        return render(request,'polls/detail.html',{'question':question,'error_message':"You didn't select a choice. ",})
    else:
        selected_choice.vote += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))