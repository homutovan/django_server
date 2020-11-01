from datetime import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import os

from .sheduler_API import Sheduler

# Create your views here.
from main.settings import STATIC_ROOT, BASE_DIR


class GetData(APIView):
    """Получает данные из файла и выводит их по урлу"""
    def get(self, request):
        file_patch = STATIC_ROOT + '/data_events.json'
        with open(file_patch, encoding='utf-8') as file:
            json_data = json.load(file)

        try:
            end_date = datetime.strptime(request.GET.get('end_date'), '%Y-%m-%d')
            start_date = datetime.strptime(request.GET.get('start_date'), '%Y-%m-%d')
        except TypeError:
            return Response({
                'lessions': json_data, 
                'success': 'true',
                })

        lessions = [
            {
                'id': lession['id'],
                'group': lession['group'],
                'teacher': lession['teacher'],
                'lecture': lession['lecture'],
                'date': lession['date'],
                'time': lession['time'],
            }
            for lession in json_data 
            if (lession.get('id') 
                and datetime.strptime(lession['date'], '%Y-%m-%d') >= start_date) 
                and (datetime.strptime(lession['date'], '%Y-%m-%d') <= end_date)]

        return Response({
            'lessions': lessions, 
            'success': 'true',
            })
    

class UpdateEvents(APIView):
    def get(self, request):
        sheduler = Sheduler()
        events = sheduler.get_all_events()
        file_patch = STATIC_ROOT + '/data_events.json'
        with open(file_patch, 'w', encoding='utf-8',newline='\n') as file:
            json.dump(events, file)
        return Response({'success': 'true'})
    
    
class UpdateExperts(APIView):
    def get(self, request):
        sheduler = Sheduler()
        experts = sheduler.get_experts()
        file_patch = STATIC_ROOT + '/data_experts.json'
        with open(file_patch, 'w', encoding='utf-8',newline='\n') as file:
            json.dump(experts, file)
        return Response({'success': 'true'})
    
class UpdateImages(APIView):
    def get(self, request):
        sheduler = Sheduler()
        images = sheduler.get_images()
        file_patch = STATIC_ROOT + '/data_images.json'
        with open(file_patch, 'w', encoding='utf-8',newline='\n') as file:
            json.dump(images, file)
        return Response({'success': 'true'})
    
class UpdateDefaultEvents(APIView):
    def get(self, request):
        sheduler = Sheduler()
        images = sheduler.get_default_events()
        file_patch = STATIC_ROOT + '/data_default_lessons.json'
        with open(file_patch, 'w', encoding='utf-8',newline='\n') as file:
            json.dump(images, file)
        return Response({'success': 'true'})