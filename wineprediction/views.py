from django.http import HttpResponse
from django.shortcuts import render
import joblib



def home(request):
    return render(request,'home.html')

def result(request):
    
    #clf = pickle.load(open('WinePickle.sav', 'rb'))
    clf = joblib.load("WinePickle.sav")
    
    paramlis = []
    paramlis.append(request.GET['FA'])
    paramlis.append(request.GET['VA'])
    paramlis.append(request.GET['CA'])
    paramlis.append(request.GET['RS'])
    paramlis.append(request.GET['CL'])
    paramlis.append(request.GET['TSD'])
    paramlis.append(request.GET['PH'])
    paramlis.append(request.GET['SU'])
    paramlis.append(request.GET['AL'])
    
    print(paramlis)
    
    ans = clf.predict([paramlis])
    print(ans)
    if ans == [0]:
        grade = 'Bad'
    elif ans == [1]:
        grade = 'Good'
    
    return render(request,'result.html',{'ans':grade})
        