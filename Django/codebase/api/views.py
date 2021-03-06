from api.models import Schedule, Teachers
from api.serializers import ScheduleSerializer, TeachersSerializer, \
    ScheduleSerializerIn
from django.http.response import Http404
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class TeachersList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, format=None):
        teachers = Teachers.objects.all()
        serializer = TeachersSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeachersSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FreeRooms(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    serializer_class = ScheduleSerializer
    notnested_serializer_class = ScheduleSerializerIn
    
    def get_serializer_class(self):
        if self.request.method == "POST":
            return self.notnested_serializer_class
        else:
            return self.serializer_class
    
    def get(self, request, format=None):
        schedule = self.get_free_rooms(request.GET)
        return Response(schedule.data)
    
    def get_free_rooms(self, get_request):
        if 'to_date' in get_request and 'from_date' in get_request and 'seats' in get_request:
            return Response(Schedule.get_free_rooms_from_to_seats(get_request))
        
        if 'to_date' in get_request and 'from_date' in get_request:
            return Response(Schedule.get_free_rooms_from_to_date(get_request))
        
        else:
            raise Http404

    def post(self, request, format=None):
        request.DATA['subject_id'] = 9
        request.DATA['teacher_id'] = 605
        serializer = ScheduleSerializerIn(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ScheduleList(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, format=None):
        schedule = self.get_some_data(request.GET)
        return Response(schedule.data)
    
    def get_some_data(self, get_request):
        """
        ITS VERYY VERYY BAD STYLEE
        """
        if 'subject' in get_request and 'room' in get_request and 'teacher' in get_request:
            return Response(Schedule.get_room_subject_teacher(get_request))
        
        elif 'subject' in get_request and 'teacher' in get_request:
            return Response(Schedule.get_subject_teacher(get_request))
        
        elif 'room' in get_request and 'teacher' in get_request:
            return Response(Schedule.get_room_teacher(get_request))
        
        elif 'subject' in get_request and 'room' in get_request:
            return Response(Schedule.get_room_subject(get_request))
        
        elif 'room' in get_request:
            return Response(Schedule.get_only_room(get_request))
        
        elif 'subject' in get_request:
            return Response(Schedule.get_only_subject(get_request))
        
        elif 'teacher' in get_request:
            return Response(Schedule.get_only_teacher(get_request))
        
        else:
            data = Schedule.objects.all()
            serializer = ScheduleSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)