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
    image = request.FILES.get('image')
    # if image == None:
    #     image = '사진을 넣어주세요'
    
    # Job.objects.filter(name=name).first()

    if Job.objects.filter(name=name):
        job = Job.objects.get(name=name)
        if job.profile_image == '':
            job.profile_image = image
            job.save()
    else:
        job = Job()
        job.name = name
        job.past_job = fake.job()
        job.profile_image = image
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
