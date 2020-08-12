from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now = datetime.datetime.now()
    if (now.day == 1 and now.month == 10):
        birth = True
    else:
        birth = False
    return render(request, "birthday/index.html", {
        "birth": birth
    })