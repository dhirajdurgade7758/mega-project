from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect, render
from notes.models import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login/")
def index(request):
    dep = Department.objects.all()
    context = {"departments":dep}
    return render(request, "index.html",context)

def sub(request):
    dep_id = request.GET.get("department",None)
    sem_id = request.GET.get("semister",None)

    subjects = None
    if dep_id and sem_id is not None:
        get_department = Department.objects.get(id = dep_id)
        get_semister = Semisters.objects.get(id = sem_id)
        subjects = Subject.objects.filter(semister = get_semister, department = get_department)  
    departments = Department.objects.all()
    semisters = Semisters.objects.all()
    studyMaterialTypes = StudyMaterialTypes.objects.all()

    return render(request, "sub.html",locals())

def search_material(request):
    if request.method == "POST":
        subject = request.POST.get("sub","default")
        mType = request.POST.get("mType","default")
        queryset = StudyMaterial.objects.filter(subject=subject,type=mType)
        context = {"studyMaterial":queryset}
        return render(request, "sub.html",context)
    else:
        return render(request, "sub.html" )

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('contact_success')
    return render(request, 'contact_us.html')

def contact_success(request):
    return render(request, 'contact_success.html')

def about(request):
    return render(request,'about.html')
# def load_subjects(request):
#     dep_id = request.GET.get("department")
#     sem_id = request.GET.get("semister")
#     subjects = Subject.objects.filter(department = dep_id, semister = sem_id)
#     return render(request, "subject_options.html",{"subjects":subjects})

def login_page(request):

   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")

      if not User.objects.filter(username = username).exists():
         messages.error(request, "invalid Username")
         return redirect("/login/")
      
      user = authenticate(username = username, password = password)
      if user is None:
         messages.error(request, "invalid Password")
         return redirect("/login/")
      else:
         login(request,user)
         return redirect("/")

   return render(request, "login_page.html")

def logout_page(request):
   logout(request)
   return redirect("/login/")

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name","default")
        last_name = request.POST.get("last_name","default")
        username = request.POST.get("username","default")
        password = request.POST.get("password","default")

      #   if((first_name or last_name or username or password) == "default"):
      #      messages.error(request, "invalid credentials")
      #      return redirect("/register/")
        user = User.objects.filter(username = username)

        if user.exists():
           messages.error(request, "Username alredy taken")
           return redirect("/register/")
        else:
            # Use create_user method to handle password hashing
            user = User.objects.create_user(
                  username=username,
                  first_name=first_name,
                  last_name=last_name,
                  password=password,
            )
            messages.info(request, "Account created succesfully")
            return redirect("/register/")

    return render(request, "register_page.html")

