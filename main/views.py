from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def add(request):

    
    # if(request.method=='post'):
    search=int(request.POST['search'])
    # try:
    result=search*search
    # except:
    #     return HttpResponse("exception")

    return render(request, 'results.html',{'result':result})