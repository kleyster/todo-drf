from .models import Tasks
from rest_framework import serializers

class TaskListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'untill_datetime', 'is_done')



class TaskDetailSerializer(serializers.ModelSerializer):
    
    created_by_email = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'untill_datetime', 'is_done','created_by','created_by_email')

        extra_kwargs = {
            "id": {'read_only': True},
            "is_done": {"read_only": True},
            "created_by": {"write_only": True, "required": True},
        }


    def get_created_by_email(self,instance):
        if instance.created_by:
            return instance.created_by.email
        return None
