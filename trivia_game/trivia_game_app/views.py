from django.shortcuts import render, redirect, HttpResponse
from .models import Player, Question, Answer
from django.contrib import messages
import bcrypt

def start(request):

    return redirect('/playerForm')

def playerForm(request):

    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        errors = Player.objects.Registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/playerForm')
        hashedPW = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        Player.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'], password=hashedPW)
        request.session['LoggedUser'] = Player.objects.last().id
        return redirect('/gamePage')

def login(request):
    if request.method == "POST":
        errors = Player.objects.Login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/playerForm')
        request.session['LoggedUser'] = Player.objects.get(email=request.POST['logemail']).id
        return redirect('/gamePage')

    return render(request, "login.html")

def gamePage(request):
    context = {
        
    }

    return render(request, "gamePage.html", context)

def questionPage(request):

    questions_by_category = {}
    questions = Question.objects.order_by('category', 'level')

    for question in questions:
        if question.category not in questions_by_category:
            questions_by_category[question.category] = []
        questions_by_category[question.category].append(question)

    context = {
        'questions_by_category': questions_by_category
    }

    return render(request, "questionPage.html", context)

def createQuestion(request):
    if request.method == "POST":
        questionText = request.POST['text']
        questionAnswer = request.POST['answer']
        questionCategory = request.POST['category']
        questionLevel = request.POST['level']
        questionAsked = request.POST.get("asked") == "on"
        Question.objects.create(
            text=questionText, 
            answer=questionAnswer, 
            category=questionCategory, 
            level=questionLevel, 
            asked=questionAsked
            )
        return redirect('/questionPage')
    
def question_list(request):
    questions_by_category = Question.objects.order_by('category', 'level')

    return render(request, 'question_list.html', {'questions_by_category': questions_by_category})