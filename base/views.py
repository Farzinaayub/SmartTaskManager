from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
tasks = [
    {'taskid': '1', 'taskaction': 'Transfer',
        'taskname': 'Move Roy to Design team', 'taskdate': '14/4/23'},
    {'taskid': '2', 'taskaction': 'Shopping',
        'taskname': 'Buy Groceries for home', 'taskdate': '15/4/23'},
    {'taskid': '3', 'taskaction': 'Transfer',
        'taskname': 'Move Praveen to Development team', 'taskdate': '14/4/23'},
    {'taskid': '4', 'taskaction': 'Visit',
        'taskname': 'Visit Mr. Roy', 'taskdate': '14/4/23'},
    {'taskid': '5', 'taskaction': 'Conference',
        'taskname': 'Attend the tech conference', 'taskdate': '17/4/23'}
]


def dashboard(request):
    context = {'tasks': tasks}
    return render(request, 'base/Dashboard.html', context)


def tab1(request):
    return render(request, 'base/tab1.html')


def taskpage(request, pk):
    task = None
    for i in tasks:
        if i['taskname'] == pk:
            task = i
    context = {'task': task}
    return render(request, 'base/tab2.html', context)


def tab3(request):
    return render(request, 'base/tab3.html')
