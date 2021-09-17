from typing_extensions import ParamSpec
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect

from django.contrib.auth.decorators import login_required


from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, get_user_model,logout

# Create your views here.

User = get_user_model()

def home(request):
	return render(request, 'index.html')

@login_required(login_url='login')
def admin_panel(request):
	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		bank_acno = request.POST['bank_acno']
		email = request.POST['email']
		passwor = '0ok9ij8uh'

		uname = firstname+" "+lastname

		user = User.objects.create_user(uname,email,passwor)
		user.bank_ac = bank_acno
		user.save()
	

		return HttpResponse(firstname+" : "+lastname+'\n'+'****'+email)
	return render(request, 'adminpanel.html')

def login(request):
	user = request.user
	
    # print(users)
	if user.is_authenticated:
		print('usrr is_authenticated ____________________________')
		if user.is_admin:
			User = get_user_model()
			users = list(User.objects.filter(is_admin=False))
			print(users)
			return render(request, 'adminpanel.html', {'us': users,'nbar':'adminpanel'})
		return render(request, 'customerview.html',{'us':user,'nbar':'dashboard'})


	print('usrr not authenticated ____________________________')

		
	if request.method == 'POST':
		emailid = request.POST['email']
		password = request.POST['password']

		user = authenticate(request, email=emailid,password=password)

		if user is not None:
			if user.is_admin:
				auth.login(request,user)
				User = get_user_model()
				users = list(User.objects.all())
				return render(request, 'adminpanel.html', {'us': users,'nbar':'adminpanel'})
			auth.login(request,user)
			return render(request, 'customerview.html',{'us':user,'nbar':'dashboard'})
				
		return HttpResponse("no user found")
	return render(request,'login.html',{'nbar':'login'})


def logout_view(request):
    logout(request)
    return redirect('/')
	