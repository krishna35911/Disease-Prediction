from django.shortcuts import render,redirect
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

from predictor.forms import BreastCancerForm, DiabetesForm, HeartDiseaseForm

from .models import *
from .forms import *
def index(request):
    return render(request,"index.html")
def predict(request):
    return render(request,"predict.html")
def feed(request):
    return render(request,"feed.html")
def feed1(request):
    return render(request,"feed1.html")
def feed2(request):
    return render(request,"feed2.html")
def doc(request):
    return render(request,"doc.html")
def booking(request):
    return render(request,"booking.html")    
def general(request):
    if request.method=="POST":
        submitbutton=request.POST.get(all)
    area=""
    result=""
    fever=""
    cold=""
    headache=""
    
    form= predictForm(request.POST or None)
    if form.is_valid():
        area= form.cleaned_data.get("area")
       
        if(area==fever,headache):
             result="chance to covid,viral fever..."
        else:
            result="chance to covid,viral fever..." 
        if(area==cold):
             result="chance to covid,cough ,fever..."
        else:
            result="chance to covid,cough fever..."         
        
        
        context={
            "entered_text":result,
            

          

            
            
        }
        return render(request,'predict.html',context=context)
    else:
        return render(request,'general.html')
    

def heart(request):
    """ 
    18:39:18 09 Oct, 2019 by Arjun Adhikari
    Reading the training data set. 
    """
    df = pd.read_csv('static/Heart_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]

    """ 
    18:39:18 09 Oct, 2019 by Arjun Adhikari
    Reading data from the user. 
    """

    value = ''

    if request.method == 'POST':

        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

        user_data = np.array(
            (age,
             sex,
             cp,
             trestbps,
             chol,
             fbs,
             restecg,
             thalach,
             exang,
             oldpeak,
             slope,
             ca,
             thal)
        ).reshape(1, 13)

        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)

        if int(predictions[0]) == 1:
            value = 'have'
        elif int(predictions[0]) == 0:
            value = "don\'t have"
            
        # return redirect(
        #           'feed',
        #           {
        #               'context': value,
        #               'title': 'Heart Disease Prediction',
        #               'active': 'btn btn-success peach-gradient text-white',
        #               'heart': True,
        #               'form': HeartDiseaseForm(),
                     
        #           })

    return render(request,
                  'heart.html',
                  {
                      'context': value,
                      'title': 'Heart Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'heart': True,
                      'form': HeartDiseaseForm(),
                  })


def diabetes(request):
    """ 
    20:13:20 09 Oct, 2019 by Arjun Adhikari
    Reading the training data set. 
    """
    dfx = pd.read_csv('static/Diabetes_XTrain.csv')
    dfy = pd.read_csv('static/Diabetes_YTrain.csv')
    X = dfx.values
    Y = dfy.values
    Y = Y.reshape((-1,))

    """ 
    20:18:20 09 Oct, 2019 by Arjun Adhikari
    Reading data from user. 
    """
    value = ''
    if request.method == 'POST':

        pregnancies = float(request.POST['pregnancies'])
        glucose = float(request.POST['glucose'])
        bloodpressure = float(request.POST['bloodpressure'])
        skinthickness = float(request.POST['skinthickness'])
        bmi = float(request.POST['bmi'])
        insulin = float(request.POST['insulin'])
        pedigree = float(request.POST['pedigree'])
        age = float(request.POST['age'])

        user_data = np.array(
            (pregnancies,
             glucose,
             bloodpressure,
             skinthickness,
             bmi,
             insulin,
             pedigree,
             age)
        ).reshape(1, 8)

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(X, Y)

        predictions = knn.predict(user_data)

        if int(predictions[0]) == 1:
            value = 'have'
        elif int(predictions[0]) == 0:
            value = "don\'t have"

    return render(request,
                  'diabetes.html',
                  {
                      'result': value,
                      'title': 'Diabetes Disease Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'diabetes': True,
                      'form': DiabetesForm(),
                  }
                  )


def breast(request):
    """ 
    20:56:20 09 Oct, 2019 by Arjun Adhikari
    Reading training data set. 
    """
    df = pd.read_csv('static/Breast_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1]
    print(X.shape, Y.shape)

    """ 
    20:57:20 09 Oct, 2019 by Arjun Adhikari
    Reading data from user. 
    """
    value = ''
    if request.method == 'POST':

        radius = float(request.POST['radius'])
        texture = float(request.POST['texture'])
        perimeter = float(request.POST['perimeter'])
        area = float(request.POST['area'])
        smoothness = float(request.POST['smoothness'])

        """ 
        21:02:21 09 Oct, 2019 by Arjun Adhikari
        Creating our training model. 
        """
        rf = RandomForestClassifier(
            n_estimators=16, criterion='entropy', max_depth=5)
        rf.fit(np.nan_to_num(X), Y)

        user_data = np.array(
            (radius,
             texture,
             perimeter,
             area,
             smoothness)
        ).reshape(1, 5)

        predictions = rf.predict(user_data)
        print(predictions)

        if int(predictions[0]) == 1:
            value = 'have'
        elif int(predictions[0]) == 0:
            value = "don\'t have"

    return render(request,
                  'breast.html',
                  {
                      'result': value,
                      'title': 'Breast Cancer Prediction',
                      'active': 'btn btn-success peach-gradient text-white',
                      'breast': True,
                      'form': BreastCancerForm(),
                  })


def home(request):

    return render(request,
                  'home.html')


""" 
20:07:20 10 Oct, 2019 by Arjun Adhikari
Handling 404 error pages. 
"""


def handler404(request):
    return render(request, '404.html', status=404)

def register(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        add=request.POST.get('add')
        email=request.POST.get('email')
        
        psw=request.POST.get('psw')
        reg(name=name,age=age,add=add,email=email,psw=psw).save()
        return redirect('login')
    else:
        return render(request,'register.html')  

def login(request):
    return render(request,'login.html')    

def log(request):
    if request.method=='POST':
        email=request.POST.get('email')
        psw=request.POST.get('psw')
        cr=reg.objects.filter(email=email,psw=psw)
        if cr:
            user=reg.objects.get(email=email,psw=psw)
            id=user.id
            email=user.email
            psw=user.psw
            request.session['id']=id
            request.session['email']=email
            request.session['psw']=psw
            return redirect('home')
        else:
            return render(request,'login.html')    
    else:
         return render(request,'register.html') 
def log1(request):
    if request.method=='POST':
        spcl=request.POST.get('spcl')
        hos=request.POST.get('hos')
        cr=doctor.objects.filter(spcl=spcl,hos=hos)
        if cr:
            user=doctor.objects.get(spcl=spcl,hos=hos)
            id=user.id
            spcl=user.spcl
            hos=user.hos
            name=user.name
            place=user.place
            mobile=user.mobile
            request.session['id']=id
            request.session['hos']=hos
            request.session['spcl']=spcl
            request.session['name']=name  
            request.session['mobile']=mobile
            request.session['place']=place
            return redirect('docview')
        else:
            return render(request,'doc.html')    
    else:
         return render(request,'doc.html')   
     
def docview(request):
    id=request.session['id']
    name=request.session['name']
    spcl=request.session['spcl']
    hos=request.session['hos']
    mobile=request.session['mobile']
    place=request.session['place']
    return render(request,"docview.html",{'id':id,'name':name,'hos':hos,'spcl':spcl,'mobile':mobile,'place':place})
        

def result(request):
    if request.method=="POST":
        name=request.POST.get('name')
        disease=request.POST.get('disease')
    return render(request,'result.html')     
