#from django.template.loader import get_template
#from django.template import Template, Context
#from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


#returns web-page with current date and time
def current_datetime(request):
  now = datetime.datetime.now()
  return render_to_response('now.html', { 'now': now })


#returns web-page with current date and time increased by ‘offset’ hours
def hours_ahead(request, offset):
  offset = int(offset)
  date_computed = datetime.datetime.now() + datetime.timedelta(hours=offset)
  return render_to_response('now_plus.html', { 'offset': offset, 'date_computed': date_computed })