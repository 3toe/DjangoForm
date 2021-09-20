from django.shortcuts import render, redirect
def index(request):
   return render(request, "index.html")

def process(request):
   if request.method == "GET":
      print("GET happened")
      return redirect("/")
   if request.method == "POST":
      print("POST happened")
      request.session['name'] = request.POST['name']
      request.session['spot'] = request.POST['spot']
      request.session['lang'] = request.POST['lang']
      request.session['comments'] = request.POST['comments']
      return redirect("/results")

def results(request):
   if request.method == "GET":
      return render(request, "results.html")
   if request.method == "POST":
      return redirect("/")