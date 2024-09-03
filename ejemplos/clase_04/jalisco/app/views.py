from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == "POST":
        number = request.POST.get("myNumber")
        answer = number + 1
    return render(request, 'index.html')
