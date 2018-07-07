# from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Homested(models.Model):
    hs_code = models.CharField(max_length=7)
    location = models.PointField(srid=4326)

    def __str__(self):
        return self.hs_code


class Homes(models.Model):
    hs_code = models.ForeignKey(Homested, on_delete=models.CASCADE)
    head = models.CharField(max_length=15)
    hm_code = models.CharField(max_length=8)
    locations = models.PointField(srid=4326)


    def __str__(self):
        return self.hm_code
    


class General(models.Model):
    hs_code = models.ForeignKey(Homested, on_delete=models.CASCADE)
    hm_code = models.ForeignKey(Homes, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25)
    relationshipToHead = models.CharField(max_length=15)
    sex = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    Mother = models.CharField(max_length=25)
    MemberOfHousehold = models.CharField(max_length=25)
    tribe_or_nationality = models.CharField(max_length=25)
    religion = models.CharField(max_length=25)
    maritalStatus = models.CharField(max_length=15)
    birthPlace = models.CharField(max_length=15)
    previousResidence = models.CharField(max_length=15)
    durationOfResidence_Month = models.PositiveIntegerField()
    durationOfResidence_Year = models.PositiveIntegerField()
    orphanhood_father = models.CharField(max_length=10)
    orphanhood_mother = models.CharField(max_length=10)
    noChildrenBoys = models.PositiveIntegerField()
    noChildrenGirls = models.PositiveIntegerField()
    noChildrenInHouseholdBoys = models.PositiveIntegerField()
    noChildrenInHouseholdGirls = models.PositiveIntegerField()
    noChildrenElsewhereBoys = models.PositiveIntegerField()
    noChildrenElsewhereGirls = models.PositiveIntegerField()
    noChildrenDiedBoys = models.PositiveIntegerField()
    noChildrenDiedGirls = models.PositiveIntegerField()
    doblastchildMonth = models.PositiveIntegerField()
    doblastchildYear = models.PositiveIntegerField()
    lastbirthnotified = models.PositiveIntegerField()
    childMale_or_Female = models.CharField(max_length=15)
    childstillAlive = models.CharField(max_length=25)
    Disability1 = models.CharField(max_length=15, blank=True)
    Disability2 = models.CharField(max_length=15, blank=True)
    Disability3 = models.CharField(max_length=15, blank=True)
    difficultyInEngaging = models.CharField(max_length=15)
    learningInstitution = models.CharField(max_length=25, blank=True)
    highestLevelReached = models.CharField(max_length=25, blank=True)
    highestLevelCompleted = models.CharField(max_length=25, blank=True)
    didLast7Days = models.CharField(max_length=15, blank=True)
    mainEmployer = models.CharField(max_length=25, blank=True)
    livebirths = models.CharField(max_length=15, blank=True)
    






    def __str__(self):
        return self.name


