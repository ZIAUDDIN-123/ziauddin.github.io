
from django.urls import path
from .views import HomePageView, AboutPageView, SkillPageView, PlanPageView


urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('skill/',SkillPageView.as_view(), name='skill'),
    path('plan/', PlanPageView.as_view(), name='plan'),
]