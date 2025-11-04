from django.shortcuts import render, redirect
from .models import users
from .forms import UsersModelForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

def contact(request):
   if request.method == "POST":
       form = UsersModelForm(request.POST)
       if form.is_valid():
          form.save()
       return redirect("table")
   else:
        form = UsersModelForm()
   return render(request, 'contact.html', {"form": form})


def table(request):
    all_users = users.objects.all()
    return render(request, 'table.html', {"users": all_users})

        

    
def update(request, id):
    user = users.objects.get(id=id)  
    
    if request.method == "POST":
        form = UsersModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("table")
    else:
        form = UsersModelForm(instance=user)

    return render(request, "update.html", {"form": form})
     
def delete(request, id):
    user = users.objects.get(id=id)
    if request.method == "POST":
        user.delete()
        return redirect("table")
    return render(request, "delete.html", {"user": user})
         
    
        
        
       
