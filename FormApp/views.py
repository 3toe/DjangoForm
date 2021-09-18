from django.shortcuts import render, redirect
def index(request):
   return render(request, "index.html")

def results(request):
   if request.method == "GET":
      print("GET")
      return redirect("/")
   if request.method == "POST":
      context = {
         "name": request.POST["name"],
         "spot": request.POST["spot"],
         "lang": request.POST["lang"],
         "comments": request.POST["comments"]
      }
      print(request.POST)
      return render(request, "results.html", context)