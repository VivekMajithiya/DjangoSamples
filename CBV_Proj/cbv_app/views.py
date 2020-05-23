from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from cbv_app.models import School, Student
from . import models
import emoji
from django.urls import reverse_lazy

# Create your views here.
class CBVindex(TemplateView):
    template_name = 'cbv_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = (emoji.emojize('I am injected from CBVIndex :thumbs up:'))
        return context

class SchoolListView(ListView):
    context_object_name='schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model = models.School
    template_name = 'cbv_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('cbv_app:list')
