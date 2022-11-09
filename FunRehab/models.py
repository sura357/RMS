from django.db import models
from django.core.validators import MaxValueValidator  # 內容驗證


# Create your models here.
class Test(models.Model):
    cName = models.CharField(max_length=20, null=False)
    cSex = models.CharField(max_length=2, default='M', null=False)
    cBirthday = models.DateField(null=False)
    cEmail = models.EmailField(max_length=100, blank=True, default='')
    cPhone = models.CharField(max_length=50, blank=True, default='')
    cAddr = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.cName


class KinectStatus(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    purchase_date = models.DateField(max_length=8, null=False)
    useful_life = models.PositiveIntegerField(null=False)
    rent = models.PositiveIntegerField(null=False)
    status = models.IntegerField(default=1, null=False)

    def __str__(self):
        return str(self.id)


class Patient(models.Model):
    id = models.CharField(primary_key=True, max_length=10, null=False)
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=10, null=False)
    birthday = models.DateField(max_length=10, null=False)
    phonenumber = models.PositiveIntegerField(null=False)
    email = models.EmailField(max_length=40, null=False)
    remark = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.id)


class Rehabilitator(models.Model):
    id = models.CharField(primary_key=True, max_length=10,  null=False)
    password = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=10, null=False)
    professional1 = models.CharField(max_length=20, null=False)
    professional2 = models.CharField(max_length=20, null=False)
    phonenumber = models.PositiveIntegerField(null=False)
    email = models.EmailField(max_length=40, null=False)
    remark = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.id)


class RentalRecords(models.Model):
    """class Meta:
        unique_together = (('kID', 'pID'),)"""

    id = models.AutoField(primary_key=True)
    kID = models.ForeignKey(KinectStatus, on_delete=models.CASCADE, to_field='id')
    pID = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='id')
    startingdate = models.DateField(max_length=8, null=False)
    duration = models.PositiveIntegerField(null=False)
    status = models.IntegerField(default=1, null=False)

    def __str__(self):
        return str(self.id)


class GameSample(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.PositiveIntegerField(null=False)
    bodypart = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=10, null=False)
    description = models.CharField(max_length=200, null=False)
    game_file = models.CharField(max_length=80, null=False)
    ico_file = models.CharField(max_length=80, null=False)
    remark = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.id)


class Motion(models.Model):
    id = models.AutoField(primary_key=True)
    rid = models.ForeignKey(Rehabilitator, on_delete=models.CASCADE, to_field='id')
    type = models.PositiveIntegerField(null=False)
    bodypart = models.CharField(max_length=10, null=False)
    name = models.CharField(max_length=75, null=False)
    video_file = models.CharField(max_length=75, null=True)
    standard_file = models.CharField(max_length=75, null=True)
    game_id = models.ForeignKey(GameSample, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return self.name


class Disease(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.PositiveIntegerField(null=False)

    def __str__(self):
        return str(self.id)


class FitDisease(models.Model):
    class Meta:
        unique_together = (('mID', 'dID'),)

    id = models.AutoField(primary_key=True)
    mID = models.ForeignKey(Motion, on_delete=models.CASCADE, to_field='id')
    dID = models.ForeignKey(Disease, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return str(self.id)


class PlanSetDetail(models.Model):
    id = models.AutoField(primary_key=True)
    duration = models.PositiveIntegerField(null=False)
    times = models.PositiveIntegerField(null=False)
    breadtime = models.PositiveIntegerField(null=False)
    ontop_duration = models.PositiveIntegerField(null=True)
    type = models.PositiveIntegerField(null=False)
    motion_time = models.PositiveIntegerField(null=False)

    def __str__(self):
        return str(self.id)


class PlanSetMotion(models.Model):
    """
    class Meta:
        unique_together = (('sdID', 'mID'),)"""

    id = models.AutoField(primary_key=True)
    mID = models.ForeignKey(Motion, on_delete=models.CASCADE, to_field='id')
    sdID = models.ForeignKey(PlanSetDetail, on_delete=models.CASCADE, to_field='id')

    def __str__(self):
        return str(self.id)


class PlanSet(models.Model):
    """
    class Meta:
        unique_together = (('SetID', 'orders'),)"""

    id = models.AutoField(primary_key=True)
    SetID = models.DateField(max_length=8, null=False)
    smID = models.ForeignKey(PlanSetMotion, on_delete=models.CASCADE, to_field='id')
    # orders = models.PositiveIntegerField(null=False)

    def __str__(self):
        return str(self.id)


class RehubRecord(models.Model):
    id = models.AutoField(primary_key=True)
    sid = models.ForeignKey(PlanSet, on_delete=models.CASCADE, to_field='id')
    # sdID = models.OneToOneField(PlanSetDetail, on_delete=models.CASCADE, to_field='id', primary_key=True)
    accuracy = models.PositiveIntegerField(null=False)
    times = models.PositiveIntegerField(null=False)
    duration = models.PositiveIntegerField(null=False)
    progress = models.PositiveIntegerField(null=False)

    def __str__(self):
        return str(self.id)


class Plan(models.Model):
    class Meta:
        unique_together = (('id', 'setID'),)

    id = models.AutoField(primary_key=True)
    planID = models.PositiveIntegerField(null=False)
    planName = models.CharField(max_length=40, null=True)
    setID = models.ForeignKey(PlanSet, on_delete=models.CASCADE, to_field='id')
    creating_date = models.DateField(max_length=14, null=False)

    def __str__(self):
        return str(self.id)


class PlanCart(models.Model):
    class Meta:
        unique_together = (('id', 'setID'),)

    id = models.AutoField(primary_key=True)
    planID = models.PositiveIntegerField(null=False)
    setID = models.ForeignKey(PlanSet, on_delete=models.CASCADE, to_field='id')
    creating_date = models.DateField(max_length=14, null=False)

    def __str__(self):
        return str(self.id)


class MedicalRecord(models.Model):
    """
    class Meta:
        unique_together = (('rID', 'pID', 'planID'),)
        """

    id = models.AutoField(primary_key=True)
    rID = models.ForeignKey(Rehabilitator, on_delete=models.CASCADE, to_field='id')
    pID = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='id')
    planID = models.ForeignKey(Plan, on_delete=models.CASCADE, to_field='id')
    creating_date = models.DateField(max_length=16, null=False)
    disease = models.CharField(max_length=30, null=False)
    symptom = models.CharField(max_length=40, null=False)
    status = models.PositiveIntegerField(null=False)
    remark = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class ContactRecord(models.Model):
    id = models.AutoField(primary_key=True)
    rID = models.ForeignKey(Rehabilitator, on_delete=models.CASCADE, to_field='id')
    pID = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='id')
    send_time = models.DateField(max_length=14, null=False)
    content = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.id)


class RehubURL(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=120, null=False)

    def __str__(self):
        return str(self.id)
