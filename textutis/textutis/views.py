# this is website by -pratham

from django.http import HttpResponse
from django.shortcuts import render



def analyze(request):
#get the text analyze the text
    djtext = (request.GET.get('text','default'))
    removepunc = (request.GET.get('removepunc','off'))
    fullcaps = (request.GET.get('fullcaps','off'))
    print(removepunc)
    print(djtext)

    if (removepunc == "on"):
        removepunc = djtext
        punctuations = (''' !@#$%$%^&&*()_:";',.?|{}[]\/ ''')

        for c in removepunc :

            if c  in punctuations:
                removepunc = removepunc.replace(c, "")

        params = {'purpose':'removepunctuation','analyzed_text': removepunc}
        return render(request,'analyze.html', params )

    elif(fullcaps == "on"):

        a = "your text :- "
        b = a + djtext.upper()

        params = {'purpose':'changed to uppercase','analyzed_text': b }
        return render(request,'analyze.html', params )

    else :
        return HttpResponse('error')

def index(request):

    return render(request,'index.html',)


