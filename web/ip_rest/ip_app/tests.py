from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ip_app.models import IpLogModel


class IplogTests(APITestCase):

    def test_create_log_record(self):
        url = reverse('ip-list')
        response = self.client.post(url, {}, format='json', HTTP_X_REAL_IP='127.0.0.1')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(IpLogModel.objects.count(), 1)
        self.assertEqual(IpLogModel.objects.get().ip, '127.0.0.1')

    def test_create_log_record_fail(self):
        url = reverse('ip-list')
        response = self.client.post(url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(IpLogModel.objects.count(), 0)

    def test_get_list(self):
        url = reverse('ip-list')
        self.client.post(url, {}, format='json', HTTP_X_REAL_IP='127.0.0.1')
        self.client.post(url, {}, format='json', HTTP_X_REAL_IP='172.10.0.2')
        self.assertEqual(IpLogModel.objects.count(), 2)
        response = self.client.get(url)
        self.assertEqual(2, len(response.data))
        self.assertEqual('127.0.0.1', response.data[0]['ip'])
        response = self.client.get(url + '?limit=1&offset=1')
        self.assertEqual('172.10.0.2', response.data['results'][0]['ip'])
