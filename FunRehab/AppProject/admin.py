from django.contrib import admin
from AppProject.models import *


# Register your models here.
class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cSex', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter = ('cName', 'cSex')
    search_fields = ('cName', )
    ordering = ('id', )


class KinectStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'purchase_date', 'useful_life', 'rent', 'status')
    list_filter = ('id', 'purchase_date')
    search_fields = ('id',)
    ordering = ('id',)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'password', 'name', 'birthday', 'email', 'remark',)
    list_filter = ('id', 'name')
    search_fields = ('id',)
    ordering = ('id',)


class RehabilitatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'password', 'name', 'professional1', 'professional2', 'phonenumber', 'email', 'remark')
    list_filter = ('id', 'name')
    search_fields = ('id',)
    ordering = ('id',)


class RentalRecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'kID', 'pID', 'startingdate', 'duration', 'status',)
    list_filter = ('id', 'kID')
    search_fields = ('id',)
    ordering = ('id',)


class GameSampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'bodypart', 'name', 'description', 'game_file', 'remark')
    list_filter = ('id', 'type')
    search_fields = ('id',)
    ordering = ('id',)


class MotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'rid', 'type', 'bodypart', 'name', 'video_file', 'standard_file', 'game_id')
    list_filter = ('id', 'type')
    search_fields = ('id',)
    ordering = ('id',)


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id',)
    ordering = ('id',)


class FitDiseaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'mID', 'dID')
    list_filter = ('id', 'mID')
    search_fields = ('id',)
    ordering = ('id',)


class PlanSetDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'duration', 'times', 'breadtime', 'ontop_duration', 'type', 'motion_time')
    list_filter = ('id', 'type')
    search_fields = ('id',)
    ordering = ('id',)


class RehubRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'Setid', 'accuracy', 'times', 'duration', 'progress')
    list_filter = ('id', 'progress')
    search_fields = ('id',)
    ordering = ('id',)


class PlanSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'SetID', )  # 'mID', 'sdID' 'orders',
    list_filter = ('id', 'SetID')
    search_fields = ('id',)
    ordering = ('id',)


class PlanSetMotionAdmin(admin.ModelAdmin):
    list_display = ('id', )  # 'mID', 'sdID'
    list_filter = ('id', )  # 'sdID'
    search_fields = ('id',)
    ordering = ('id',)


class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'planID', 'setID', 'creating_date')
    list_filter = ('id', 'planID')
    search_fields = ('id',)
    ordering = ('id',)


class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'rID', 'pID', 'planID', 'creating_date', 'disease', 'symptom', 'status', 'remark')
    list_filter = ('id', 'planID')
    search_fields = ('id',)
    ordering = ('id',)


class ContactRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'rID', 'pID', 'send_time', 'content')
    list_filter = ('id', 'rID')
    search_fields = ('id',)
    ordering = ('id',)


admin.site.register(Test, TestAdmin)
admin.site.register(KinectStatus, KinectStatusAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Rehabilitator, RehabilitatorAdmin)
admin.site.register(RentalRecords, RentalRecordsAdmin)
admin.site.register(GameSample, GameSampleAdmin)
admin.site.register(Motion, MotionAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(FitDisease, FitDiseaseAdmin)
admin.site.register(PlanSetDetail, PlanSetDetailAdmin)
# admin.site.register(RehubRecord, RehubRecordAdmin)
admin.site.register(PlanSet, PlanSetAdmin)
admin.site.register(PlanSetMotion, PlanSetMotionAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
admin.site.register(ContactRecord, ContactRecordAdmin)

