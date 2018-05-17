# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase

from .views import home, board_topics
from .models import Board


class HomeTests(TestCase):

    def setUp(self):
        self.board = Board.objects.create(name='Django', description="Django board")
        url = reverse('home')
        self.resp = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.resp.status_code, 200)

    def test_home_url_resolves_home_view(self):
        # 使用resolve来将浏览器发起请求的URL与urls.py模块中列出的URL进行匹配
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.resp, f'href="{board_topics_url}"')


class BoardTopicsTests(TestCase):
    
    def setUp(self):
        Board.objects.create(name='Django', description='Django Board')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        resp = self.client.get(url)
        self.assertEquals(resp.status_code, 404)

    def test_board_topics_url_resolves_board_topic_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        resp = self.client.get(board_topics_url)
        homepage_url = reverse('home')
        self.assertContains(resp, f'href="{homepage_url}"')
    
