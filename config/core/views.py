from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, "cinema/base.html")

def header(request):
    return render(request, "cinema/header.html")

def footer(request):
    return render(request, "cinema/footer.html")

def SignIn(request):
    return render(request, "cinema/SignIn.html")

def SignUp(request):
    return render(request, "cinema/SignUp.html")
