from django.shortcuts import render, redirect
from .models import  User
from .forms import UserForm

# Create your views here.
def user_List(request):
    users = User.objects.all()
    return render(request,'listingpage.html',{'users':users})
def add_user(request):
    mydict={}
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict['form'] = form
    return render(request,'add.html')




