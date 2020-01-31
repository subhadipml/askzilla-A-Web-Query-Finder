from django.shortcuts import render, redirect

# Create your views here.
# asked = "I will show the answer here..."
def asking(request):
    
    '''import wikipedia
    import wolframalpha
    import speech_recognition as sr
    app_id = "X4GXWV-9ETJLHU7XY"

    r = sr.Recognizer()
    with sr.Microphone() as source:
        asked = "Listening..."
        audio = r.listen(source)
    try:
        w_input = r.recognize_google(audio)
        asked = "I am searching for" + w_input
        
        try:
            client = wolframalpha.Client(app_id)
            res = client.query(w_input)#result
            asked = next(res.results).text
                #return render(request, 'ask/index.html', context=next(res.results).text)
        except:
            try:
                asked = wikipedia.summary(w_input)
                    #return render(request, 'ask/index.html', context=wikipedia.summary(w_input))
            except:
                asked = "Sorry, I failed to solve your query..."
                    #return render(request, 'ask/index.html', context="Sorry, I failed to solve your query...")
    except sr.UnknownValueError:
        asked = "I could not understand your voice..."
            #return render(request, 'ask/index.html', context="I could not understand your voice...")'''
    return render(request, 'ask/index.html', {'asked':"you are right"})

def index(request):
    asked = "I will show the answer here..."
    return render(request, 'ask/index.html', {'asked':asked})