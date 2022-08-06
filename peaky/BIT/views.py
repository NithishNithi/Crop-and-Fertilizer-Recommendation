from django.http import HttpResponse
from django.shortcuts import render
import joblib

def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,"home.html")

def result(request):

    cls = joblib.load("crop_model.sav")

    lis = []

    lis.append(request.GET["NITROGEN"])
    lis.append(request.GET["PHOSPHORUS"])
    lis.append(request.GET["POTASSIUM"])
    lis.append(request.GET["TEMPERATURE"])
    lis.append(request.GET["HUMIDITY"])
    lis.append(request.GET["PH"])
    lis.append(request.GET["RAINFALL"])
    
    predict1=cls.predict([lis])
    if (predict1 ==0):
        crop_name='Apple(सेब)(ஆப்பிள்)'
    elif predict1 == 1:
      crop_name = 'Banana(केला)(வாழை)'
    elif predict1 == 2:
      crop_name = 'Blackgram(काला चना)(உளுந்து)'
    elif predict1 == 3:
      crop_name = 'Chickpea(काबुली चना)(சுண்டல்)'
    elif predict1 == 4:
      crop_name = 'Coconut(नारियल)(தேங்காய்)'
    elif predict1 == 5:
      crop_name = 'Coffee(कॉफ़ी)(காபி பயிர்)'
    elif predict1 == 6:
      crop_name = 'Cotton(कपास)(பருத்தி)'
    elif predict1 == 7:
      crop_name = 'Grapes(अंगूर)(திராட்சை)'
    elif predict1 == 8:
      crop_name = 'Jute(जूट)(சணல்)'
    elif predict1 == 9:
      crop_name = 'Kidneybeans(राज़में)(கிட்னி பீன்ஸ்)'
    elif predict1 == 10:
      crop_name = 'Lentil(मसूर की दाल)(பருப்பு)'
    elif predict1 == 11:
      crop_name = 'Maize(मक्का)(சோளம்)'
    elif predict1 == 12:
      crop_name = 'Mango(आम)(மாங்கனி)'
    elif predict1 == 13:
      crop_name = 'Mothbeans(मोठबीन)(அந்துப்பூச்சி பீன்ஸ்)'
    elif predict1 == 14:
       crop_name = 'Mungbeans(मूंग)(பாசிப்பயறு)'
    elif predict1 == 15:
      crop_name = 'Muskmelon(खरबूजा)(முலாம்பழம்)'
    elif predict1 == 16:
      crop_name = 'Orange(संतरा)(ஆரஞ்சு)'
    elif predict1 == 17:
      crop_name = 'Papaya(पपीता)(பப்பாளி)'
    elif predict1 == 18:
      crop_name = 'Pigeonpeas(कबूतर के मटर)(துவரை)'
    elif predict1 == 19:
      crop_name = 'Pomegranate(अनार)(மாதுளை)'
    elif predict1 == 20:
      crop_name = 'Rice(चावल)(அரிசி)'
    elif predict1 == 21:
      crop_name = 'Watermelon(तरबूज)(தர்பூசணி)'
    return render(request,"home.html",{'ans':crop_name})
def fertilizer(request):
    return render(request,"fertilizer.html")
def result2(request):
    krl=joblib.load('fertilizer_model.sav')
    lis2=[]
    lis2.append(request.GET["TEMPERATURE"])
    lis2.append(request.GET["HUMIDITY"])
    lis2.append(request.GET["MOISTURE"])
    lis2.append(request.GET["SOILTYPE"])
    lis2.append(request.GET["CROPTYPE"])
    lis2.append(request.GET["NITROGEN"])
    lis2.append(request.GET["POTASSIUM"])
    lis2.append(request.GET["PHOSPHORUS"])
    predict2=krl.predict([lis2])
    if (predict2 ==0):
        fertilizer_name='10-26-26'
    elif predict2 == 1:
      fertilizer_name = '14-35-14'
    elif predict2 == 2:
      fertilizer_name = '17-17-17'
    elif predict2 == 3:
      fertilizer_name = '20-20'
    elif predict2 == 4:
      fertilizer_name = '28-28'
    elif predict2 == 5:
      fertilizer_name = 'DAP'
    elif predict2 == 6:
      fertilizer_name = 'Urea'

    return render(request,"fertilizer.html",{'ans2':fertilizer_name})
  
    
    