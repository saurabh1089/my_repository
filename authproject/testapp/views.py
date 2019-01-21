from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_exams_view(request):
    return render(request,'testapp/javaexams.html')
@login_required
def python_exams_view(request):
    return render(request,'testapp/pythonexams.html')
@login_required
def aptitude_exams_view(request):
    return render(request,'testapp/aptitudeexams.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

from testapp.forms import SignupForm
def signup_view(request):
    form=SignupForm()
    if request.method=='POST':
        form=SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
