from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Homested(models.Model):
    hs_code = models.CharField(max_length=7)
    location = models.PointField(srid=4326)


class Homes(models.Model):
    hs_code = models.ForeignKey(Homested, on_delete=cascade)
    head = models.CharField(max_length=15)
    hm_code = models.CharField(max_length=8)
    locations = models.PointField(srid=4326)
    


class General(models.Model):
    hs_code = models.ForeignKey(Homested, on_delete=cascade)
    hm_code = models.ForeignKey(Home, on_delete=cascade)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25)
    relationshipToHead = models.CharField(max_length=15)
    sex = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    Mother = models.CharField(max_length=25)
    MemberOfHousehold = models.CharField(max_length=25)
    tribe_or_nationality = models.CharField(max_length=25)
    religion = models.CharField(max_length=25)


