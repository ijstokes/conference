from django.db import models
from django import forms
from django.contrib.auth.models import User


class Speaker(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField()


class Proposal(models.Model):
    speaker_name = models.CharField(max_length=150)
    speaker_email = models.EmailField()
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    bio = models.TextField()
    additional_info = models.TextField(blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal


class oldProposalForm(forms.Form):
    full_name = forms.CharField(max_length=50, label='Your Name')
    email = forms.EmailField(label='Email Address')
    title = forms.CharField(max_length=255, label='Title of Presentation')
    abstract = forms.CharField(widget=forms.Textarea, label='Abstract of Presentation')
    bio = forms.CharField(widget=forms.Textarea, label='Your Bio')
    additional = forms.CharField(widget=forms.Textarea, label='Any additional information', required=False)
