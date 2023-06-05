# import api_key
import transcribe
import openai
import os
# import cognitive
from django.http import JsonResponse
from .models import Task
from django.shortcuts import render
import sys
import requests
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import logging
import traceback

sys.path.append('..')


def commandfn():
    if True:
        openai.api_key = os.environ.get('api')
        input_text = transcribe.from_mic()
        tasks = ner(input_text)
        print(tasks)
        return tasks


# def call_function(request):
#     # Call your desired Python function or perform any other actions
#     result = commandfn()

#     # Return the result as a JSON response
#     response = {'result': result}
#     # print(response)
#     task = Task(name=result['name'], desc=result['desc'],
#                 category=result['category'])
#     task.save()
#     return JsonResponse(response)
def call_function(request):
    try:
        result = commandfn()

        response = {'result': result}
        task = Task(name=result['name'], desc=result['desc'], category=result['category'])
        task.save()

        return JsonResponse(response)

    except Exception as e:
        logging.error(str(e))
        logging.error(traceback.format_exc())
        return HttpResponse(status=500)


def ner(input_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract the entities from the text with labels Id,name,desc,date,category\ntext: Remind me to buy some chocolates for saya and diya from Lulu Mall on today.\n\nId:1\nname:Set Reminder\ndesc: Buy Chocolates for kids\ndate:\ncategory:family\n##\ntext: assign the frontend module to rajesh's team. They can start working from tomorrow\n\nId:2\nname: Delegate\ndesc: Assign Frontend Module to rajesh's team\ndate:\ncategory:work\n##\ntext:{input_text}\n",
        temperature=0.02,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    extracted_text = response['choices'][0]['text']

    # Extract the entities from the extracted text and create a dictionary
    entities = {}
    for line in extracted_text.split('\n'):
        if ':' in line:
            key, value = line.split(':')
            entities[key.strip()] = value.strip()

    return entities


def dashboard(request):

    # task = Task(name=tasks['name'], desc=tasks['desc'],
    #             category=tasks['category'])
    # task.save()

    # context = {'tasks': tasks}
    return render(request, 'base/dashboard.html')


def tab1(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    print(tasks)
    return render(request, 'base/tab1.html', context)


def taskpage(request, tasks, pk):
    tasks['Id'] == pk
    context = {'task': tasks}
    return render(request, 'base/tab2.html', context)


def tab3(request):
    return render(request, 'base/tab3.html')
