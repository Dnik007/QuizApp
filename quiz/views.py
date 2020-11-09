from django.shortcuts import render
from .models import Questions
# Create your views here.

def home(request):
    return render(request, 'quiz/index.html')

def questions(request):
    q=Questions.objects.all()
    return render(request, 'quiz/questions.html',{'q':q})

def result(request):
    if request.method=='POST':
        data=request.POST
        data1=dict(data)
        qid=[]
        qans=[]
        ans=[]
        score=[]
        for key in data1:
            try:
                qid.append(key)
                qans.append(data1[key][0])
            except:
                print("ERROR!!")
        for q in qid:
            ans.append((Questions.objects.get(id=q)).answer)
        total=len(ans)
        for _ in range(total):
            if ans[_]==qans[_]:
                score+=1
    return render(request, 'quiz.html',{'score':score,'total':total})
