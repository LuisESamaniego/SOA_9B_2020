from django.shortcuts import render
from services.models import Products

# Create your views here.
def showTemplate(request):
    response = Products.objects.all()
    return render(request, 'index.html', {'response' : response})
