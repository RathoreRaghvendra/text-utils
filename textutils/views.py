#I have created this file-RP
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    # return HttpResponse('''Hello RP! <a href="https://www.youtube.com/watch?v=zs2Ux1jfDD0&list=PLu0W_
    # 9lII9ah7DDtYtflgwMwpT3xmjXY9&index=6&ab_channel=CodeWithHarry"> My Notes </a> ''')
def about(request):
    return HttpResponse("About rp") 

def analyze(request):
    # Getting the text
    djtext = request.POST.get('text', 'default')
    # In removepunc one value is off bcoz if the checkbox doesn't signed then the default value will be off
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(removepunc)
    # print(djtext)
    # print(uppercase)
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char 
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
     # Analyzing the text
     # The above return statement is opening the analyze.html post index.html
    elif  uppercase== "on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'UpperCase', 'analyzed_text':analyzed}
        djtext=analyzed
    elif lineremover=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed=analyzed+char
        params={'purpose':'Line Remover', 'analyzed_text':analyzed}
        djtext=analyzed
    elif spaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':'Extra Space Remover', 'analyzed_text':analyzed}        
        djtext=analyzed
    elif charcount=="on":
        analyzed=0
        for char in djtext:
            analyzed=analyzed+1
        params={'purpose':'Character Counter', 'analyzed_text':analyzed}   
        djtext=analyzed    
    elif removepunc!="on" and uppercase!="on" and lineremover!="on" and spaceremover!="on" and charcount!="on":
        return HttpResponse("Error")
    
    return render(request, 'analyze.html',params)