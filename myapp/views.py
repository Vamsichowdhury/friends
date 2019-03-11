from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import FormName
from .models import FriendsCrush

def index(request):
	name=FriendsCrush.objects.all()
	return render (request,'index.html',{'names':name})

def home(request):
	return render(request,'home.html')


def forms(request):
	form=FormName()

	if request.method=='POST':
		form=FormName(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/myapp/index/')
	return render(request,'forms.html',{'myform':form})

def remove_name(request,pk):
	name=FriendsCrush.objects.get(pk=pk)
	name.delete()
	return redirect('/myapp/index/')

def remove_all(request):
	name=FriendsCrush.objects.all()
	name.delete()
	return redirect('/myapp/index/')

def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/myapp/index/')
		else:
			return redirect('/myapp/login/')
		
	return render(request,'login.html')

def logout_user(request):
	logout(request)
	return redirect('/myapp/')