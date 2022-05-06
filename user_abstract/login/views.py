from django.shortcuts import render

# Create your views here.


import django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


from .models import UserProfile
from .forms import ProfileForm

def user_profile(request):

      if request.method == "POST":

            username1=request.POST.get('username')
            print("---------------",username1)
            first_name=request.POST.get('first_name')
            print("---------------",first_name)
            last_name=request.POST.get('last_name')
            print("---------------",last_name)

            email=request.POST.get('email')
            print("---------------",email)

            password=request.POST.get('password1')
            print("---------------",password)

            # gender=request.POST['gen']
            # print("---------------",gender)

          
            phone = request.POST.get("phone")
            gender = request.POST.get("gender")
              # hobby=request.POST["hobby"]1
            hobby=request.POST.getlist('hobby[]')

            x =','.join(hobby)
            hobby=str(x)

            birth_date=request.POST.get("birth_date")
            print("🚀 ~ file: views.py ~ line 14 ~ phone", phone)
            print("🚀 ~ file: views.py ~ line 15 ~ gender", gender)
            print("🚀 ~ file: views.py ~ line 16 ~ hobby", hobby)
            print("🚀 ~ file: views.py ~ line 17 ~ birth_date", birth_date)
            profile = UserProfile.objects.create_user(username=username1,first_name=first_name,last_name=last_name,email=email,password=password,phone=phone,gender=gender,hobby=hobby,birth_date=birth_date)

            profile.save()
            # profile=ProfileForm()
            return HttpResponse("oky")

      else:
        user_form = ProfileForm()
        # return HttpResponse("error...")
        return render(request,'login/reg.html',{'user_form': user_form})


def login_view(request):

  if request.method == "POST":

      fm=AuthenticationForm(request=request,data=request.POST)
      # print("🚀 ~ file: views.py ~ line 66 ~ fm", fm)

      if fm.is_valid():
        uname=fm.cleaned_data.get('username')
        print("🚀 ~ file: views.py ~ line 66 ~ uname", uname)

        upwd=fm.cleaned_data.get('password')
        print("🚀 ~ file: views.py ~ line 68 ~ upwd", upwd)
        
        user=authenticate(username=uname,password=upwd)
        print("🚀 ~ file: views.py ~ line 68 ~ user", user)
        
        if user is not None:
          login(request,user)
          # return HttpResponseRedirect('/profile/')
          return render(request,'login/profile.html',{'uname':user})
  else:
    fm=AuthenticationForm()
  return render(request,'login/login.html',{'form':fm})

def profile(request):
       return render(request,'login/profile.html')
           
def logout_view(request):
      logout(request)     
      return HttpResponseRedirect('/logout/')



def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        
        if query_name:
            results = UserProfile.objects.filter(username__contains=query_name)
            print("🚀 ~ file: views.py ~ line 105 ~ results", results)
            
            return render(request, 'login/search.html', {"results":results})
        else:
          return HttpResponse("not found")
    return render(request, 'login/search.html')