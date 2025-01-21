from django.shortcuts import render,HttpResponse
from datetime import datetime
from book.models import Contact
from django.contrib import messages

# Create your views here.
def home(request):
    contacts=Contact.objects.all()
    context={
        'contact':contacts
    }
    print(context)
    return render(request,'home.html',context)
    

def about(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        text=request.POST.get('comment')
        contact=Contact(title=title,text=text,date=datetime.today())
        contact.save()
        messages.success(request,"your entry was published,visit story site! ")

        

    return render(request,'about.html')
