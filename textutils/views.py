from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # getting the input text
    djtext = request.POST.get('text', 'default')

    # getting the switch input
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    CharCounter = request.POST.get('CharCounter', 'off')

    punctuations = '''!()-[]{};\:'",<>./?@#$%^&*_~'''
    if removepunc == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if capitalize == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Newline Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extraspace Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if CharCounter == 'on':
        analyzed = " "
        count = 0
        for char in djtext:
            if char != " ":
                count = count + 1
        counter = count
        analyzed = djtext
        params = {'purpose': 'Number of Characters', 'analyzed_text': analyzed, 'counter': count}

    if removepunc != "on" and capitalize != "on" and newlineremover != "on" and extraspaceremover != "on" and CharCounter != "on":
        return HttpResponse("Error: Please SELECT atleast one feature")

    return render(request, 'analyze.html', params)

# params update in each step and last params value is rendered
