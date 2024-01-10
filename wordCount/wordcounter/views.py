from django.shortcuts import render
from wordcounter.forms import TextForm
import re
import json
from django.http import HttpResponse

# Create your views here.
def index(request):
    form = TextForm()
    
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            if len(form.cleaned_data["sentence"]) == 0:
                return render(request,"wordcounter/index.html",{"message":"Please Enter any sentence"})
            else:
                my_data = {}
                # print(form.cleaned_data["sentence"])
                # print(form.cleaned_data["WordCount"])
                # print(form.cleaned_data["LineCount"])
                # print(form.cleaned_data["LetterCount"])
                st = form.cleaned_data["sentence"]
                # if form.cleaned_data["WordCount"]:
                #     li = re.split(r"[.?,!\s]+",st)
                #     my_data["WordCount"] = len(li)
                #     # print(li)
                #     # print(my_data["WordCount"])
                # if form.cleaned_data["LineCount"]:
                #     li = re.split(r"[\n]",st)
                #     my_data["LineCount"] = len(li)
                # if form.cleaned_data["LetterCount"]:
                #     my_data["LetterCount"] = len(re.split(r"[a-zA-Z]",st))
                di = {}
                li = re.split(r"[''.?,!\s]+",st)
                for i in li:
                    di[i] = di.get(i,0) + 1
                my_data["Frequences"] = di
                my_data["form"]=form
                return render(request,"wordcounter/base.html",context = my_data)
    # print(form.changed_data)
    return render(request,"wordcounter/base.html",{"form":form})

#at present for this project it is not in use. If you want you can comment out this function or view.
def word_counter(request):
    print("helo")
    if request.method == "POST":
       
        # print(form)
        my_data = {}
        
        st = request.POST.get("text").strip()
        print(st)
        li = re.split(r"[''.?,!\s]+",st)
        # print(li)
        ans = 0
        if '' in li:
            ans = li.count('')
        my_data["WordCount"] = len(li) - ans
        li = re.split(r"[\n]",st)
        my_data["LineCount"] = len(li) - li.count('')
        my_data["LetterCount"] = len(re.split(r"[a-zA-Z]",st)) - 1
        # print(my_data)
        return HttpResponse(json.dumps(my_data), content_type='application/json')