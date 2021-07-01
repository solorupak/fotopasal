from django.apps import apps
from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone


class DateTimeModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
    )
    updated_at = models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
    )
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, hard=False):
        if not hard:
            self.deleted_at = timezone.now()
            super().save()
        else:
            super().delete()


class Designation(DateTimeModel):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=(
        ('FEMALE', 'FEMALE'),
        ('MALE', 'MALE'),
        ('OTHERS', 'OTHERS'),
    ))
    date_of_birth = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Designation'
        verbose_name_plural = 'Designations' 

    def __str__(self):
        return self.name

# class Events(DateTimeModel):
#     title = models.CharField(max_length=200)

# class Package(DateTimeModel):
#     title = models.CharField(max_length=200)

# class FamilyNames(DateTimeModel):
#     relation = models.CharField(max_length=200)
#     full_name = models.CharField(max_length=200)

# class Photographer(DateTimeModel):
#     full_name = models.CharField(max_length=200)

# class VideoGrapher(DateTimeModel):
#     full_name = models.CharField(max_length=200)


# class Data(DateTimeModel):
#     bill_number = models.PositiveBigIntegerField()
#     client_name = models.CharField(max_length=200)
#     contact_no = models.CharField(max_length=200)
#     events = models.ForeignKey(Events, on_delete=models.CASCADE)
#     date = models.DateField()
#     package = models.ForeignKey(Package, on_delete=models.CASCADE)
#     total_price = models.PositiveBigIntegerField()
#     advance = models.PositiveBigIntegerField()
#     due =  models.PositiveBigIntegerField()
#     photo_selection = models.BooleanField()
#     # songs 
#     family_names = models.ForeignKey(FamilyNames, on_delete=models.CASCADE)
#     photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
#     videographer = models.ForeignKey(VideoGrapher, on_delete=models.CASCADE)
#     #backup1
#     #backup2
#     deadline = models.DateField()
#     #workstatus
#     copied_to = models.CharField(max_length=200)
#     delivery_status = models.CharField(max_length=200, choices=DELIVERY STATUS)
    
