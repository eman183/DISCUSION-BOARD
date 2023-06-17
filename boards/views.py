from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Board,Topic,Post
from django.contrib.auth.models import User

# Create your views here.
def index(request):
   boards=Board.objects.all()

   return render(request,"boards/home.html",{"boards":boards})



def about(request):
   return HttpResponse("hallo from about")


def board_topics(request,board_id):
#    try:
#        board=Board.objects.get(id=board_id)
#    except Board.DoesNotExist:
#           raise Http404
   board=get_object_or_404(Board,id=board_id)
   return render(request,"boards/topics.html",{"board":board})



def new_topic(request,board_id):
      board=get_object_or_404(Board,id=board_id)
      print(board)
      if request.method=="POST":
          subject=request.POST['subject']
          massage=request.POST['message']
          print(subject)
          print(massage)
          user=User.objects.first()
          topic=Topic.objects.create(
              subject=subject,
              board=board,
              created_by=user)
          post=Post.objects.create(
              massage=massage,
              topic=topic,
              created_by=user)
          return redirect("board_topics",board_id=board.pk)
      return render(request,"boards/new_topic.html",{"board":board})
