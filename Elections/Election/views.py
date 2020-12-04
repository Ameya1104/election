from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Candidate, Election, Election_Result, Voter
from .forms import EditForm, VoterForm
from django.urls import reverse_lazy, reverse
import datetime

# Create your views here.
class AddVoter(CreateView):
	model = Voter
	form_class = VoterForm
	template_name = 'add_voter.html'
	voter = Voter.objects.all().last()
	print(voter.state)
	success_url = reverse_lazy('index')

	def get_context_data(self, *args, **kwargs):
		voters = Voter.objects.all()
		context = super(AddVoter, self).get_context_data(*args, **kwargs)
		context["voters"] = voters
		return context

class DeleteVoter(DeleteView):
	model = Voter
	template_name = 'delete_voter.html'
	success_url = reverse_lazy('index')

	def get_context_data(self, *args, **kwargs):
		edit_voter = Voter.objects.all()
		context = super(DeleteVoter, self).get_context_data(*args, **kwargs)
		context["edit_voter"] = edit_voter
		return context

class VoterDetails(ListView):
	model = Voter
	template_name = 'voter_details.html'
	
	def get_context_data(self, *args, **kwargs):
		voters = Voter.objects.all()
		context = super(VoterDetails, self).get_context_data(*args, **kwargs)

		context["voters"] = voters
		return context

class IndiVoterDetails(DetailView):
	model = Voter
	template_name = 'indi_voter_details.html'

	def get_context_data(self, *args, **kwargs):
		voters = Voter.objects.all()
		context = super(IndiVoterDetails, self).get_context_data(*args, **kwargs)

		context["voters"] = voters
		return context

class IndexView(ListView):
	model = Election_Result
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		results = Election_Result.objects.all()
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context["results"] = results
		return context

class ResultLSView(ListView):
	model = Election_Result
	template_name = 'ls_results.html'

	def get_context_data(self, *args, **kwargs):
		results = Election_Result.objects.all()
		context = super(ResultLSView, self).get_context_data(*args, **kwargs)
		context["results"] = results
		return context

class ResultVSView(ListView):
	model = Election_Result
	
	template_name = 'vs_results.html'
	def get_context_data(self, *args, **kwargs):
		results = Election_Result.objects.all()
		context = super(ResultVSView, self).get_context_data(*args, **kwargs)
		context["results"] = results
		return context

class ElectionView(ListView):
	model = Candidate
	template_name = 'election.html'

	def get_context_data(self, *args, **kwargs):
		candidates = Candidate.objects.all()
		context = super(ElectionView, self).get_context_data(*args, **kwargs)
		context["candidates"] = candidates
		return context

class EditVoterView(UpdateView):
	model = Voter
	template_name = 'edit_voter.html'
	fields = "__all__"
	success_url = reverse_lazy('index')

	def get_context_data(self, *args, **kwargs):
		voters = Voter.objects.all()
		context = super(EditVoterView, self).get_context_data(*args, **kwargs)
		context["voters"] = voters
		return context