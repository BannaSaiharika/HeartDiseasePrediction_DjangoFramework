from django.shortcuts import render
from joblib import load
model=load('C:/Users/banna/model.joblib')
def home(request):
    return render(request,'index.html')

def result(request):

    age=int(request.GET['age'])
    sex=int(request.GET['sex'])
    cp=int(request.GET['cp'])
    trestbps=int(request.GET['trestbps'])
    chol=int(request.GET['chol'])
    restecg=int(request.GET['restecg'])
    thalach=int(request.GET['thalach'])
    exang=int(request.GET['exang'])
    oldpeak=float(request.GET['oldpeak'])
    slope=int(request.GET['slope'])
    thal=int(request.GET['thal'])
    probability = model.predict_proba([[age,sex,cp,trestbps,chol,restecg,thalach,exang,oldpeak,slope,thal]])
    probability=probability[0][0]*100
    return render(request,'result.html',{'y_pred':probability})

# Create your views here.
