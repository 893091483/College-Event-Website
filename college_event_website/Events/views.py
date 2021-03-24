from django.shortcuts import render
from crispy_forms.helper import FormHelper
from .forms import EventForm, CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Event, Comment
from Universities.models import University
from Users.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Events.models import Locations

# Create your views here.

@login_required(login_url='/Users/login/')
def list_events(response):
  if response.method == "POST":
    if response.POST.get("search-button"):
      university_name = response.POST.get("search-university")
      university = University.objects.filter(name = university_name).first()
      events = Event.objects.filter(university = university)
  else:
    events = Event.objects.all()
  
  user_university = University.objects.filter(name = response.user.university).first()
  all_university = University.objects.all()
  return render(response, 'Events/base.html', { 
    'events' : events,
    'user_university': user_university,
    'all_university': all_university
    })

@login_required(login_url='/Users/login/')
def add_event(response):
  if response.method == "POST":
    if response.POST.get("create-event-btn"):
      event_form = EventForm(response.POST)
      is_private = response.POST.get("universityEvent")
      is_RSO = response.POST.get("rsoEvent")
      if event_form.is_valid():
          location = get_location(response)
          user_university = None
          if response.POST.get("universityEvent"):
            user_university = response.user.university
          event_form.save(is_private, is_RSO, response.user.is_admin, location, user_university)
          messages.success(response, "Event added")
      return HttpResponseRedirect('../../Events/')
    else:
      return HttpResponseRedirect('../../Events/create')
  event_form = EventForm(None)
  return render(response, "Events/create.html", { 'form' : event_form })


def edit_event(response):
  if response.method == "POST":
    pass
  return render(response, 'Events/?????')


@login_required(login_url='/Users/login/')
def event_info(response, event_id):
  if response.method == "POST":
    if response.POST.get("delete-comment-btn"):
      comment_id = response.POST.get("delete-comment-btn")
      delete_comment(comment_id, response.user)
      return HttpResponseRedirect('../../Events/' + str(event_id) + '')
    
    if response.POST.get("edit-comment-btn"):
      comment_id = response.POST.get("edit-comment-btn")
      comment_rating = response.POST.get("edit-comment-btn")
      if delete_comment(comment_id, response.user) == False:
        return  HttpResponseRedirect('../../Events/' + str(event_id) + '')

    comment_form = CommentForm(response.POST)
    if comment_form.is_valid():
        current_event = Event.objects.filter(id = event_id).first()
        current_user = User.objects.filter(id = response.user.id).first()
        comment_form.save(current_user, current_event)
        messages.success(response, "Comment added")
    return HttpResponseRedirect('../../Events/' + str(event_id) + '')
  else:
    comment_form = CommentForm(None)
    event = Event.objects.filter(id = event_id).first()
    all_comments = Comment.objects.filter(event= event).order_by('-timestamp')
    rating  = get_rating(all_comments)
    return render(response, "Events/details.html", { 
      'form' : comment_form,
      'event' : event,
      'rating': rating,
      'comments': all_comments
      })

@login_required(login_url='/Users/login/')
def approve(response):
  
  return render(response, "Events/approve.html")

def delete_comment(comment_id, current_user):
  current_comment = Comment.objects.filter(id=comment_id)[0]
  if current_comment.user.id == current_user.id:
    current_comment.delete()
    return True
  else:
    return False

def get_rating(all_comments):
  if len(all_comments) == 0:
    return 0
  
  count = 0
  for comment in all_comments:
    count += comment.rating 

  result =  count / len(all_comments)

  return round(result, 2)


def get_location(response):
  current_location = Locations(
    name = response.POST.get("location_name"),
    latitude = response.POST.get("location_latitude"),
    longitude = response.POST.get("location_longitude")
  )
  current_location.save()
  return current_location