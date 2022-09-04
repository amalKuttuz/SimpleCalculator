from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def add(request):

    
    # if(request.method=='post'):
    a=int(request.POST['a'])
    b=int(request.POST['b'])
    s=(request.POST['s'])

    if(s=='+'):
        result=a+b
        return render(request, 'results.html', {'result': result})
    elif(s=='-'):
        result=a-b
        return render(request, 'results.html', {'result': result})
    elif(s=='*'):
        result=a*b
        return render(request, 'results.html', {'result': result})
    elif(s=='/'):
        result=a/b
        return render(request, 'results.html', {'result': result})
    elif(s=='%'):
        result=a%b
        return render(request, 'results.html', {'result': result})
    elif (s == ''):
        return HttpResponse("operator box is empty")

    else:
        return HttpResponse("Enter a valid operator")


    # return render(request, 'results.html',{'result':result})