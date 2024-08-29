from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for entire year",
    "february": "Run minimum 20km ",
    "march": "Run minimum 50km",
    "april": "Walk minimum 10 km",
    "may": "Run minimum 50 km easily at least now",
    "june": "go to gym please",
    "july": "Walk for at least 20 mins today please",
    "august": "idk man ,today just sleep",
    "september": "Hmm, today go to gym",
    "october": "Today, idk man, just  sleep",
    "november": "Run at least 100 km today",
    "december": "Today is your final day, just run gow much you can"
}

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("This month is not supported")
    
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) 
    return HttpResponseRedirect(redirect_path)

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li> <a href=\"{month_path}\"> {capitalized_month} </a> </li>"
    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)
