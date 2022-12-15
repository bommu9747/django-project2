from django.shortcuts import render

# Create your views here.
def firsts(request):
    return render(request,'first.html')
def secands(request):
    return render(request,'secand.html')
def thirds(request):
    return render(request,'third.html')
def abouts(request):
    return render(request,'about as.html')
def contacts(request):
    return render(request,'contact.html')
def logouts(request):
    return render(request,'third.html')