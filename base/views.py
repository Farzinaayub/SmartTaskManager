
import secrets
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
        prompt=f"Extract the entities from the text with labels Id,Action,Task,Time,Relative time,Date,Relative Date,Stakeholders,Location\ntext: Remind me to buy some chocolates for saya and diya from Lulu Mall.\n\nId:1\nAction:Set Reminder\nTask: Buy Chocolates\nTime: Not specified\nRelative time: not specified\nDate: not specified\nRelative Date: Today\nStakeholders: me,saya,diya\nLocation: Lulu Mall\n##\ntext: assign the frontend module to rajesh's team. They can start working from tomorrow\n\nId:2\nAction: Delegation\nTask: Assign Frontend Module\nTime: Not specified\nRelative time: Tomorrow\nDate: Not specified\nRelative Date: Tomorrow\nStakeholders: Rajesh's Team\nLocation: Office\n##\ntext:{input_text}\n",
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

# print(random_token)


# print(ner(input_text))


def dashboard(request):
    context = {'tasks': tasks}
    return render(request, 'base/Dashboard.html', context)


def tab1(request):
    return render(request, 'base/tab1.html')


def taskpage(request, pk):
    # task = None
    # for key, value in tasks.items():
    #     if value['Id'] == pk:

    #         task = value
    #         break
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
