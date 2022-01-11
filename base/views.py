from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Member

class MemberList(ListView):
    model = Member
    context_object_name = 'members'

class MemberDetail(DetailView):
    model = Member
    context_object_name = 'member'

class MemberCreate(CreateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members')
    template_name = 'base/member_form.html'

class MemberUpdate(UpdateView):
    model = Member
    fields = '__all__'
    success_url = reverse_lazy('members')
    template_name = 'base/member_form_edit.html'
    
class MemberDelete(DeleteView):
    model = Member
    context_object_name = 'member'
    success_url = reverse_lazy('members')

