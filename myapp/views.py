from django.shortcuts import render,redirect
from myapp.models import FAQ
from myapp.models import SearchEngine
from myapp.models import user_register
from myapp.models import Blogs
from myapp.models import contact_us
from myapp.models import review
'''from myapp.models import UserChangePassword'''
from myapp.models import helpSupport
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.

def footer(request):
	return render(request,'footer.html')
def login(request):
	if request.method=="POST":
		e=request.POST.get('em')
		p=request.POST.get('pw')
		user=user_register.objects.filter(email=e,password=p)
		k=len(user)
		if k>0:
			request.session['email']=e
			return redirect('/userprofile')	
		else:
			return render(request,'login_form.html',{'msg':"invalid user"})
	else:
		return render(request,'login_form.html')

def navbar(request):
	return render(request,'navbar.html')

def sidebar(request):
	return render(request,'sidebar.html')


def register(request):
	return render(request,'register_form.html')

def base(request):
	return render(request,'base.html')

def allFAQs(request):
	res=FAQ.objects.all()
	return render(request,'allFAQs.html',{'data':res})

def allSearchEngines(request):
	res=SearchEngine.objects.all()
	return render(request,'allSearchEngines.html',{'data':res})

def allBlogs(request):
	res=Blogs.objects.all()
	return render(request,'allBlogs.html',{'data':res})
def register(request):
	if request.method=="POST":
		n=request.POST.get('nm')
		e=request.POST.get('em')
		p=request.POST.get('pw')

		c=request.POST.get('cpw')

		if user_register.objects.filter(email=e).exists():
			msg="email Id already exists"
			return render(request,'register_form.html',{'msg':msg})
		else:
			if p==c:
				x=user_register()
				x.name=n
				x.email=e
				x.password=p
				x.save()
				msg="user successfully registered"
				return render(request,'register_form.html',{'msg':msg})
			else:
				msg="password and confirm password doesn't match"
				return render(request,'register_form.html',{'msg':msg})
	else:
		return render(request,'register_form.html')


def contact(request):
	if request.method=="POST":
		x=contact_us()
		x.name=request.POST.get('nm')
		x.email=request.POST.get('em')
		x.phone=request.POST.get('ph')
		x.message=request.POST.get('ta')
		x.save()
		return render(request,'contact_us.html',{'msg':1})
	else:
		return render(request,'contact_us.html')

def myreview(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		x=review()
		x.title=request.POST.get('tt')
		x.message=request.POST.get('ta')
		x.save()
		return render(request,'review.html',{'msg':1})
	else:
		return render(request,'review.html')

def ChangePassword(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		o=request.POST.get('pwo')
		n=request.POST.get('pwn')
		c=request.POST.get('cp')
		if n==c:
			user=user_register.objects.get(email=request.session['email'])
			p=user.password
			if p==o:
				user.password=n
				user.save()
				msg="password successfully changed"
				return render(request,'change_password.html',{'msg':msg})
			else:
				msg="old password doesn't match"
				return render(request,'change_password.html',{'msg':msg})
		else:
			msg=" password and confirm password does not match "
			return render(request,'change_password.html',{'msg':msg})
	else:
		return render(request,'change_password.html')
		
	
def HelpAndSupport(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		x=helpSupport()
		x.heading=request.POST.get('h')
		x.content=request.POST.get('ta')
		x.save()
		msg="content added successfully"
		return render(request,'help_support.html',{'msg':msg})
	else:
		return render(request,'help_support.html')

def userprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=user_register.objects.get(email=request.session['email'])
	return render(request,'my_profile.html',{'user':user})

def detailBlog(request, id):
	res=Blogs.objects.get(id=id)
	return render(request,'detailblog.html',{'data':res})

def detailFAQ(request, id):
	res=FAQ.objects.get(id=id)
	return render(request,'detailFAQ.html',{'data':res})

		
def editProfile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=user_register.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.name=request.POST.get('nm')
		user.pincode=request.POST.get('pin')
		user.contact=request.POST.get('ph')
		user.DOB=request.POST.get('dob')
		user.address=request.POST.get('add')
		user.save()
		print("profile edited successfully")
		return redirect('/userprofile/')
	else:
		return render(request,'edit_profile.html',{'user':user})

def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	del request.session['email']
	return redirect('/login')

def forgot(request):
	if(request.method=='POST'):
		em=request.POST.get('em')
		user=user_register.objects.filter(email=em)
		if(len(user)>0):
			password=user[0].password
			subject="Password"
			message="Welcome! your password is"+password
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[em]
			send_mail(subject,message,email_from,recipient_list)
			res="your password sent to your respective email account"
			return render(request,'forget_password.html',{'res':res})
		else:
			rest='this email it is not registered'
			return render(request,'forget_password.html',{'res':rest})
	else:
		return render(request,'forget_password.html')














