from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessTracker,Webpages


# Create your views here.
def index(request):
    mydict = {'num1':'8108128262', 'num2':'8108128262', 'email':'vmpk2001@gmail.com'}
    return render(request,'first_app/index.html', context=mydict)

def accessrec(request):
    Acc_records=AccessTracker.objects.order_by('date')
    acc_list={'acc_records':Acc_records,'count':len(Acc_records)}
    return render(request,'first_app/acc.html',context=acc_list)
