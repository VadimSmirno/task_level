from django.db import models

class Task(models.Model):
    PRIORITY_NONE = 0
    PRIORITY_LOW = 1
    PRIORITY_MODERATE = 2
    PRIORITY_HIGH = 3
    PRIORITIES = (
        (PRIORITY_NONE, ('')),
        (PRIORITY_LOW, ('Low')),
        (PRIORITY_MODERATE, ('Moderate')),
        (PRIORITY_HIGH, ('High')),
    )

    name = models.CharField(max_length=30)
    descriptions = models.TextField()
    create_date_time = models.DateTimeField(auto_now=True)
    finish_date_time = models.DateTimeField()
    priority = models.PositiveIntegerField(choices=PRIORITIES,default=PRIORITY_NONE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_date_time']

class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name