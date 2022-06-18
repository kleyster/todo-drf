from django.db import models

class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    untill_datetime = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey('users.CustomUser',related_name='created_tasks',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.title