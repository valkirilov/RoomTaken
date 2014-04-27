from api.models import Schedule, Rooms, Groups, Spiciality, Subjects, Teachers
from django.contrib import admin

class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ('room_id',)
    list_display = ('room_id', 'teacher_id', 'subject_id', 'group_id', 'created', 'updated',)
    list_filter = ('room_id', 'teacher_id', 'subject_id', 'group_id', 'created', 'updated',)
    ordering = ('-created',)

class RoomsAdmin(admin.ModelAdmin):
    search_fields = ('room_id',)
    list_display = ('seats', 'number', 'is_computer_room', 'created', 'updated',)
    list_filter = ('seats', 'number', 'is_computer_room', 'created', 'updated',)
    ordering = ('-created',)
    
class GroupsAdmin(admin.ModelAdmin):
    search_fields = ('spec_id',)
    list_display = ('spec_id', 'number', 'course', 'created', 'updated',)
    list_filter = ('spec_id', 'number', 'course', 'created', 'updated',)
    ordering = ('-created',)
    
class SpicialityAdmin(admin.ModelAdmin):
    search_fields = ('full_name',)
    list_display = ('full_name', 'short_name', 'created', 'updated',)
    list_filter = ('full_name', 'short_name', 'created', 'updated',)
    ordering = ('-created',)
    
class SubjectsAdmin(admin.ModelAdmin):
    search_fields = ('full_name',)
    list_display = ('full_name', 'short_name', 'created', 'updated',)
    list_filter = ('full_name', 'short_name', 'created', 'updated',)
    ordering = ('-created',)
    
class TeachersAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'degree', 'short', 'created', 'updated',)
    list_filter = ('name', 'degree', 'short', 'created', 'updated',)
    ordering = ('-created',)

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Spiciality, SpicialityAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(Teachers, TeachersAdmin)

