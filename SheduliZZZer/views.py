
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import os

# Create your views here.
from main.settings import STATICFILES_DIRS, BASE_DIR


class GetData(APIView):
    def get(self, request):
        file_patch = STATICFILES_DIRS[0] + '/data_lessons.json'
        with open(file_patch, encoding='utf-8') as file:
            json_data = json.load(file)

        lessions = [
            {
                'id': lession['id'],
                'group': lession['group'],
                'teacher': lession['teacher'],
                'lecture': lession['lecture'],
                'date': lession['date'],
                'time': lession['time'],
            }
            for lession in json_data if lession.get('id', 0)]

        return Response({'lessions': lessions})