from django.shortcuts import render
from django.http import HttpResponse
import datetime

def say_yoga(request):
	position = 'Downward Dog'
	html = '<html><body><h1>Yoga %s!</h1></body></html>' % position
	return HttpResponse(html)

def get_now(request):
	now = datetime.datetime.now()
	return render(request, "Yoga/base.html", {"current_date": now})

def inheritance_test(request):
    return render(request, "Yoga/home.html",
                  {"a_variable": "gbftyfvyoga",
                   "another_variable": "moreyoga"})

def timetable_page(request):
    return render(request, "Yoga/timetable.html",
                  {"b_variable": "Class Timetable",
                   "other_variable": "Winter class timetable, for private lessons, please visit the contact page."})

def tips_page(request):
    return render(request, "Yoga/tips.html",
                  {"c_variable": "Yoga Tips",
                   "the_variable": "Tips on how to improve your yoga practice."})