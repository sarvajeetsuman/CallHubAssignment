# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HistoryData(models.Model):
    """
    This Table maintains a history of query performed
    """
    input_number = models.IntegerField()
    fibonacci_result = models.CharField(max_length=250, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add = True,blank=True, null=True)
    modified_date = models.DateTimeField(auto_now = True, blank=True, null=True)
    
    class Meta:
        app_label = 'fibonacci_app'
        managed = True

    def __unicode__(self):
        return str(self.input_number)
     
