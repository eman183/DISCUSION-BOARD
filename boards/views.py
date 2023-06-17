from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.
def index(request):
   boards=Board.objects.all()
   board_names=[]
   for board in boards:
       board_names.append(board.name)
       return HttpResponse(f"{board_names}")