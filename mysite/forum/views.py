from django.shortcuts import render

def index(request):
    TOPIC_LIST = ["HTML", "CSS", "JavaScript", "Python", "Java", "C", "PHP", "R", "Swift", "Kotlin"]
    return render(request, "forum/index.html", {"topics": TOPIC_LIST})

def forum(request, topic):
    pass