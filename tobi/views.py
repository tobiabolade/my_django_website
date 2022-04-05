from django.shortcuts import get_object_or_404, render
from .models import Person, Code, Language


# Create your views here.

def index(request):
   
    person = Person.objects.get(pk=1)
    return render(request, 'tobi/index.html', {'person': person})
    
        
def about(request):
    person = Person.objects.all()
    return render(request, 'tobi/about.html', {'person': person})
    
    
def code(request):
    code = Code.objects.all()
    return render(request, 'tobi/code.html', {'code': code})
        

def codeType(request, code_type):
    lang = Language.objects.all()
    codes = get_object_or_404(Code, code_type=code_type)
    return render(request, 'tobi/codeType.html', {'codes': codes}, {'lang': lang})















    
    