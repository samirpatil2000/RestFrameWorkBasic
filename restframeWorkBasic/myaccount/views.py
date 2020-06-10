from django.contrib import messages
from django.shortcuts import render, redirect
from.forms import UserRegisterForm #,ProfileUpdateForm,UserUpdateForm
# Create your views here.
def index(request):
    return render(request,'myaccount/index.html')

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account Has Been Created {username} !')
            return redirect('login')
    else:
        form=UserRegisterForm()

    return render(request,'myaccount/register.html',{'form':form})
