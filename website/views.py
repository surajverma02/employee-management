from django.shortcuts import render,redirect
from website.models import Employee
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
@login_required(login_url="/login/")
def home_page(request):
    emps = Employee.objects.all()

    if request.GET.get('search'):
        
        emps = emps.filter(Q(first_name__icontains = request.GET.get('search')) |Q(last_name__icontains = request.GET.get('search')) |Q(state__icontains = request.GET.get('search')))

    return render(request, 'home.html', {'emp':emps})


def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect("/login/")

        else:
            login(request, user)
            return redirect("/")
        
    return render(request, 'login.html', {})


@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return redirect("/login/")


def signup_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request, "Username already taken")
            return redirect("/signup/")

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
                    )
    
        user.set_password(password)
        user.save()
        messages.info(request, "Account created successfully")

        return redirect ("/signup/")

    return render(request, 'signup.html', {})


@login_required(login_url="/login/")
def Employee_Data(request):
    
    if request.method=="POST":
        
        # Data fetching
        first_name  = request.POST.get("first_name")
        last_name  = request.POST.get("last_name")
        address  = request.POST.get("address")
        city  = request.POST.get("city")
        state  = request.POST.get("state")
        email  = request.POST.get("email")
        phone  = request.POST.get("phone")

        # create models object and set data
        e = Employee()
        e.first_name = first_name
        e.last_name = last_name
        e.address = address
        e.city = city
        e.state = state
        e.email = email
        e.phone = phone
        
        e.save()
        print(e.email)


        return redirect('/')
    
    return render(request, 'register.html', {})


@login_required(login_url="/login/")
def Delete_data(request, id):
    e = Employee.objects.get(id=id)
    
    e.delete()
    return redirect('/')


@login_required(login_url="/login/")
def Update_data(request, id):
    e = Employee.objects.get(id = id)
    return render(request, 'update.html', {'emp':e})


@login_required(login_url="/login/")
def updated(request, id):
    if request.method=="POST":
        
        # Data fetching
        first_name  = request.POST.get("first_name")
        last_name  = request.POST.get("last_name")
        address  = request.POST.get("address")
        city  = request.POST.get("city")
        state  = request.POST.get("state")
        email  = request.POST.get("email")
        phone  = request.POST.get("phone")

        # create models object and set data
        
        e = Employee.objects.get(id = id)
        e.first_name = first_name
        e.last_name = last_name
        e.address = address
        e.city = city
        e.state = state
        e.email = email
        e.phone = phone
        
        e.save()
        return redirect('/')