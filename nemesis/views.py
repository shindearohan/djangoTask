from django.shortcuts import render, HttpResponse, redirect
from nemesis.models import Sign
from django.contrib import messages
from nemesis.forms import empforms

# Create your views here.
def index(request):
    if request.method == "POST":
        try:
            Userdetails=Sign.objects.get(email=request.POST['email'], password=request.POST['password'])
            
            request.session['email']=Userdetails.email
            return render(request,"user.html")
        except Sign.DoesNotExist as e:
            messages.success(request,'Username / password Invalid')
    return render(request, 'index.html')
    #return HttpResponse("this is home page")

def user(request):
    return render(request,'user.html')    

def sign(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        address = request.POST.get('address')
        sign = Sign(username=username, email=email, password=password, confirmpassword=confirmpassword, address=address)
        sign.save()
        messages.success(request, 'Your message has been send')
        return render(request,'index.html')
    return render(request,'sign.html')

def logoutuser(request):
    try:
        del request.session['email']
    except:
        return render(request,"index.html")

    return redirect('/index')    

def userdetails(request):
    home = Sign.objects.all()
    return render(request,"userdetails.html", {'alluser': home,"alluser":home})
    #return render(request,"userdetails.html", {'sign':all_data})
    
def delete(request, id):
    stud = Sign.objects.get(id=id)
    stud=Sign(id=id)
    stud.delete()
    return redirect('/userdetails')

def editrec(request, id):
    updateemp = Sign.objects.get(id=id)
    form = empforms(request.POST,instance=updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,"Record updated succesfully...!")
        return render(request,"useredit.html")
    else:
        return render(request,"useredit.html",{'Sign':updateemp})


       
        