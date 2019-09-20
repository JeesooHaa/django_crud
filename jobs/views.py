from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from faker import Faker
import requests
from pprint import pprint

Url = 'https://api.giphy.com/v1/gifs/search?api_key=rBmbyDm4lYUOqpUet86sNwmDjRucRfSL&lang=ko&limit=1&q='


def index(request):
    return render(request, 'jobs/index.html')


def past_job(request):
    fake = Faker()
    name = request.POST.get('name')
    
    # Job.objects.filter(name=name).first()

    if Job.objects.filter(name=name):
        job = Job.objects.get(name=name)
    else:
        job = Job()
        job.name = name
        job.past_job = fake.job()
        job.save()
    url = Url + job.past_job
    data = requests.get(url).json()
    try:
        data = data.get('data')[0].get('images').get('downsized').get('url')
    except:
        data = 'No image'
    context = { 
        'job': job,
        'data': data, 
    }
    return render(request, 'jobs/past_job.html', context)
