from django.shortcuts import render
from wordcounter.forms import TextForm
import re

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
                if form.cleaned_data["WordCount"]:
                    li = re.split(r"[.?,!\s]+",st)
                    my_data["WordCount"] = len(li)
                    # print(li)
                    # print(my_data["WordCount"])
                if form.cleaned_data["LineCount"]:
                    li = re.split(r"[\n]",st)
                    my_data["LineCount"] = len(li)
                if form.cleaned_data["LetterCount"]:
                    my_data["LetterCount"] = len(re.split(r"[a-zA-Z]",st))
                if form.cleaned_data["Frequences"]:
                    di = {}
                    li = re.split(r"[.?,!\s]+",st)
                    for i in li:
                        di[i] = di.get(i,0) + 1
                    my_data["Frequences"] = di
                return render(request,"wordcounter/results.html",context = my_data)
    return render(request,"wordcounter/index.html",{"form":form})
