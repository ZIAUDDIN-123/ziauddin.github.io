from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'    

class SkillPageView(TemplateView):
    template_name = 'skill.html'  

class PlanPageView(TemplateView):
    template_name = 'plan.html'      























 





 





