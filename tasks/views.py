from django.shortcuts import render

tasks = ["Django", "SQL", "Testing"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })