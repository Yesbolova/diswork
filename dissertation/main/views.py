from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic





class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    class SignUpView(generic.CreateView):
        form_class = UserCreationForm
        success_url = reverse_lazy('login')
        template_name = 'signup.html'





def index(request):
    return render (request, 'main/index.html')



def about(request):
    return render (request, 'main/about.html')


def  praktika (request):
    return  render (request, 'main/praktika.html')

def  syntax (request):
    return  render (request, 'main/syntax.html')

def  datatype (request):
    return  render (request, 'main/datatype.html')

def  arithmeticoperation (request):
    return  render (request, 'main/arithmeticoperation.html')

def  linearalgortm(request):
    return  render (request, 'main/linearalgortm.html')

def  inputandoutput (request):
    return  render (request, 'main/inputandoutput.html')

def  workingwithfiles (request):
    return  render (request, 'main/workingwithfiles.html')

def  programmingalgorithms01 (request):
    return  render (request, 'main/programmingalgorithms01.html')

def  programmingalgorithms02 (request):
    return  render (request, 'main/programmingalgorithms02.html')

def  programmingalgorithms03 (request):
    return  render (request, 'main/programmingalgorithms03.html')


def  programmingalgorithms04 (request):
    return  render (request, 'main/programmingalgorithms04.html')

def  operator01 (request):
    return  render (request, 'main/operator01.html')

def  operator02 (request):
    return  render (request, 'main/operator02.html')

def  operator03 (request):
    return  render (request, 'main/operator03.html')

def  operator04 (request):
    return  render (request, 'main/operator04.html')

def  operator05 (request):
    return  render (request, 'main/operator05.html')

def  operator06 (request):
    return  render (request, 'main/operator06.html')
def task (request):
    return  render (request, 'main/task.html')
def informatiki (request):
    return  render (request, 'main/informatiki.html')
def olimpiada_esepteri (request):
    return  render (request, 'main/olimpiada_esepteri.html')









