from django.test import TestCase,Client
from django.urls import reverse
from django.shortcuts import render,get_object_or_404
from yomex.models import WristWatch

class TestViews(TestCase):

    def test_wristwatch(self):
        client=Client()

        response=client.get(reverse('yomex:watch'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'yomex/watch.html')


    def test_detail_wristwatch(self):
        client = Client
        watch = get_object_or_404(WristWatch,id=id)
        url=reverse('yomex:watch',args=watch.id)
        response = self.client.get(url)
        self.assertContains(response, watch)
