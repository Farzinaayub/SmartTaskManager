import api_key
import transcribe
import openai
from .models import Task
from django.shortcuts import render
import sys
sys.path.append('..')


openai.api_key = api_key.api
input_text = transcribe.from_mic()


def ner(input_text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract the entities from the text with labels Id,name,desc,date,category\ntext: Remind me to buy some chocolates for saya and diya from Lulu Mall.\n\nId:1\nname:Set Reminder\ndesc: Buy Chocolates for kids\ndate:Not specified\ncategory:family\n##\ntext: assign the frontend module to rajesh's team. They can start working from tomorrow\n\nId:2\nname: Delegate\ndesc: Assign Frontend Module to rajesh's team\ndate: Not specified\ncategory:work\n##\ntext:{input_text}\n",
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
    # return response['choices'][0]['text']


tasks = ner(input_text)
print(tasks)


def dashboard(request):
    task = Task(name=tasks['name'], desc=tasks['desc'])
    task.save()

    context = {'tasks': tasks}
    return render(request, 'base/Dashboard.html', context)


def tab1(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    print(tasks)
    return render(request, 'base/tab1.html', context)


def taskpage(request, pk):
    tasks['Id'] == pk
    context = {'task': tasks}
    return render(request, 'base/tab2.html', context)


def tab3(request):
    return render(request, 'base/tab3.html')

# from django.http import HttpResponse

# Create your views here.
# tasks = [
#     {'taskid': '1', 'taskaction': 'Transfer',
#         'taskname': 'Move Roy to Design team', 'taskdate': '14/4/23'},
#     {'taskid': '2', 'taskaction': 'Shopping',
#         'taskname': 'Buy Groceries for home', 'taskdate': '15/4/23'},
#     {'taskid': '3', 'taskaction': 'Transfer',
#         'taskname': 'Move Praveen to Development team', 'taskdate': '14/4/23'},
#     {'taskid': '4', 'taskaction': 'Visit',
#         'taskname': 'Visit Mr. Roy', 'taskdate': '14/4/23'},
#     {'taskid': '5', 'taskaction': 'Conference',
#         'taskname': 'Attend the tech conference', 'taskdate': '17/4/23'}
# ]
