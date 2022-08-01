from django.db import models
from tastypie.resources import ModelResource
from backend.models import Choice
# Create your models here.
class ReactionResource(ModelResource):
    class Meta:
         queryset=Choice.objects.all()
         resource_name='choices'
