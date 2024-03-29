from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/accounts/login/')
    context = {
        "form": form,
    }
    return render(request, "accounts/register.html", context=context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)

    context = {
        "form":form,
    }
    return render(request, "accounts/login.html",context=context)

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/")
    return render(request, "accounts/logout.html")