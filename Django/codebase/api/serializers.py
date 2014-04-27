from django.forms import widgets
from rest_framework import serializers
from api.models import Teachers, Groups, Rooms, Schedule, Spiciality, Subjects


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'name', 'degree', 'short')
        depth = 2
        
class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('full_name', 'short_name')
        depth = 2
        
class SpicialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Spiciality
        fields = ('full_name', 'short_name')
        depth = 2
        
class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('spec_id', 'number', 'course')
        depth = 2
        
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ('id', 'name', 'seats', 'number', 'is_computer_room')
        depth = 2
        
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('room_id', 'teacher_id', 'subject_id', 'group_id', 'is_full_time', 'speciality_id', 'from_date', 'to_date')
        depth = 2
     
    def is_valid(self, *args, **kwargs):
        self.init_data['room_id'] = self.get_or_not_room(self.init_data['room_id'])
        super(ScheduleSerializer, self).is_valid(*args, **kwargs)
        
    def get_or_not_room(self, room_id):
        return Rooms.objects.get(id=room_id)
    
class ScheduleSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('teacher_id', 'subject_id', 'room_id', 'from_date', 'to_date')