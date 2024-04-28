from django.shortcuts import render

# Temporar Model for Applications
applications = [
    {
        "job_title": "Front-end Developer",
        "link": "",
        "id": 1,
        "location": "San Francisco, CA",
        "dateApplied": "2024-04-25",
        "datePosted": "2024-04-20",
        "coverLetter": True,
        "status": "Pending"
    },
    {
        "job_title": "Data Scientist",
        "link": "",
        "id": 2,
        "location": "New York, NY",
        "dateApplied": "2024-04-24",
        "datePosted": "2024-04-15",
        "coverLetter": True,
        "status": "Under Review"}
]

# Create your views here.

def home (request):
    return render (request, 'home.html')

def about (request):
    return render(request, 'about.html')

def applications_index (request):
    return render(request, 'applications/index.html', {
        'applications': applications
    })