from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

Projects=[
    {
    'slug':'Sydney Modern Project, Sydney, Australia ',
    'title': 'Sydney Modern Project, Sydney, Australia ',
    'image': '2.jpg',
    'content': 'Perched above Sydney Harbour, the 19th-century Art Gallery of New South Wales is being reimagined as a series of stepped pavilions that mimic the surrounding landscape.',
    },
    {
        'slug': 'San Pellegrino Flagship Factory, Bergamo, Italy',
        'title': 'San Pellegrino Flagship Factory, Bergamo, Italy ',
        'image': '2.jpg',
        'content':'In 2017, Danish architecture firm Bjarke Ingels Group (BIG) won a design competition to renovate and expand the headquarters of Italian mineral water brand San Pellegrino. Nestled between the Brembo river and San Pellegrino Terme, the Italian town from which the company derives its name, the $102 million project’s contemporary arched design has seen it dubbed “Factory of the Future.” '
    },
{
        'slug': 'Qorner Tower, Quito, Ecuador',
        'title': 'Qorner Tower, Quito, Ecuador',
        'image': '3.jpg',
        'content':'Plant-covered high-rises – or “garden skyscrapers,” as they’re often known – have become an increasingly common sight in Europe since the completion of Milan’s Vertical Forest in 2014. And the phenomenon continues to gain traction around the world.'
    }
]


def OurProjects(request):
    return render(request,'projects/projects.html',{'Projects':Projects})


def Project_details(request,slug):
    Project=next(Project for Project in Projects if Project['slug']==slug)
    return render(request,'projects/projects_details.html',{'project':Project})