from rest_framework import viewsets
from rest_framework.response import Response
from .models import Tasks
from rest_framework import status
from .serializers import TaskDetailSerializer,TaskListSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from .utils import send_notification_about_task_to_email

class TaskViewSet(viewsets.ViewSet):

    queryset = Tasks.objects.all()


    @swagger_auto_schema(responses={200:TaskListSerializer})
    def list(self,request,*args,**kwargs):
        data = Tasks.objects.all()
        serializer = TaskListSerializer(data,read_only=True,many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(responses={200:TaskDetailSerializer})
    def retrieve(self,request,pk):
        data = self.queryset.filter(pk=pk)
        if not data.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskDetailSerializer(data.first())
        return Response(serializer.data)
    
    @swagger_auto_schema(responses={200:TaskDetailSerializer},request_body=TaskDetailSerializer)
    def create(self,request):
        data = request.data
        data['created_by'] = request.user.pk
        serializer = TaskDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    @swagger_auto_schema(responses={200:TaskDetailSerializer},request_body=TaskDetailSerializer)
    def patch(self,request,pk):
        instance = self.queryset.filter(pk=pk)
        if not instance.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskDetailSerializer(data=request.data,instance=instance.first())
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self,request,pk):
        instance = self.queryset.filter(pk=pk)
        if not instance.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance.delete()
        return Response()
    
    @action(detail=True,methods=['POST'])
    def execute(self,request,pk):
        instance = self.queryset.filter(pk=pk)
        if not instance.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        instance = instance.first()
        instance.is_done = not(instance.is_done)
        instance.save()
        serializer = TaskDetailSerializer(instance)
        send_notification_about_task_to_email.apply_async(kwargs=serializer.data)
        return Response(serializer.data)