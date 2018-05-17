# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Board


def home(request):
    boards = Board.objects.all()
    boards_names = list()
    
    # for board in boards:
    #     boards_names.append(board.name)

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk): # pk指的是primary key 主键
    # try:
    #     board = Board.objects.get(pk=pk)
    #     return render(request, 'topics.html', {'board': board})
    # except Board.DoesNotExist:
    #     raise Http404

    ''' 另一种更简洁的写法 '''
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


