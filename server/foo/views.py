from django.shortcuts import render
import os
from celery import Celery
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import traceback
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')

app.config_from_object('django.conf:settings', namespace='CELERY')


@api_view(['POST'])
@parser_classes([JSONParser])
def index(request):
    try:
        x: int = request.data.get('x')
        y: int = request.data.get('y')
        z = app.send_task('add', kwargs=dict(x=x, y=y))
        #task_id
        print(z.id)
        return Response(status=status.HTTP_200_OK)
    except Exception:
        print(traceback.format_exc())
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
