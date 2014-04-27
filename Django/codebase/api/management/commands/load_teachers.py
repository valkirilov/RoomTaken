from django.core.management.base import NoArgsCommand
from datetime import date
import json

import logging
from api.models import Teachers
logger = logging.getLogger(__name__)

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        self.stdout.write('Load teachers')       
        json_data=open('/home/krassi/HackFMI/RoomTaken/RoomTaken/Django/codebase/script_loaddata/teachers.json')
        
        data = json.load(json_data)
        for x in data:
            full_name = x['teacherFullname']
            arr_short = full_name.split(' ')
            if len(arr_short) == 1:
                short = arr_short[0][0]
            else:
                short = arr_short[0][0] + arr_short[1][0]
            degree = x['teacherPosition']
            email = x['teacherEmail']
            department = x['department']
            
            teacher = Teachers.objects.create(name=full_name, short=short, degree=degree, email=email, department=department)
            teacher.save()

        json_data.close()
        
        self.stdout.write('Finished load teachers')