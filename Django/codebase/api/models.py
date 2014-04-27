# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.query_utils import Q
from django.shortcuts import get_list_or_404
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

    for user in User.objects.all():
        Token.objects.get_or_create(user=user)

class Teachers(models.Model):
    name = models.CharField(_(u'Име'), max_length=64, null=False, blank=False)
    degree = models.CharField(_(u'Титла'), max_length=90, null=False, blank=False)
    short = models.CharField(_(u'Инициали'), max_length=5, null=False, blank=False)
    email = models.EmailField(_(u'Имейл'))
    department = models.CharField(_(u'Отдел'), max_length=10)
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True, verbose_name=_(u'добавена'))
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True, verbose_name=_(u'последна промяна'))
    
    class Meta(object):
        verbose_name = _(u'Преподаватели')
        verbose_name_plural = _(u'Преподаватели')
        
    def __unicode__(self):
        return _(u'%(name)s %(degree)s %(short)s') % dict(
            name=self.name,
            degree=self.degree,
            short=self.short,
        )
    
class Subjects(models.Model):
    full_name = models.CharField(_(u'Пълно име'), max_length=128, null=True, blank=True)
    short_name = models.CharField(_(u'Съкращение'), max_length=10, null=True, blank=True)
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True, verbose_name=_(u'добавена'))
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True, verbose_name=_(u'последна промяна'))
    
    class Meta(object):
        verbose_name = _(u'Предмети')
        verbose_name_plural = _(u'Предмети')
    
    def __unicode__(self):
        return _(u'%s' % self.short_name)
    
class Spiciality(models.Model):
    full_name = models.CharField(_(u'Пълно име'), max_length=20, null=True, blank=True)
    short_name = models.CharField(_(u'Съкращение'), max_length=10, null=True, blank=True)
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True, verbose_name=_(u'добавена'))
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True, verbose_name=_(u'последна промяна'))
    
    class Meta(object):
        verbose_name = _(u'Специалности')
        verbose_name_plural = _(u'Специалности')
        
    def __unicode__(self):
        return _(u'%s' % self.full_name)
    
class Groups(models.Model):
    spec_id = models.ForeignKey(Spiciality)
    number = models.IntegerField(_(u'Номер на група'))
    course = models.IntegerField(_(u'Курс'))
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True, verbose_name=_(u'добавена'))
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True, verbose_name=_(u'последна промяна'))
    
    class Meta(object):
        verbose_name = _(u'Групи')
        verbose_name_plural = _(u'Групи')
        
    def __unicode__(self):
        return _(u'%s' % self.number)
        
class Rooms(models.Model):
    name = models.CharField(_(u'Име на стая'), max_length=32, blank=True, null=True)
    floor = models.CharField(_(u'Етаж'), max_length=7)
    seats = models.IntegerField(_(u'Брой места'))
    number = models.CharField(_(u'Номер на стая'), unique=True, max_length=4)
    
    is_computer_room = models.BooleanField()
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True, verbose_name=_(u'добавена'))
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True, verbose_name=_(u'последна промяна'))
    
    class Meta(object):
        verbose_name = _(u'Стаи')
        verbose_name_plural = _(u'Стаи')
        
    def __unicode__(self):
        return _(u'%s' % self.number)
        
class Schedule(models.Model):
    room_id = models.ForeignKey(u'Rooms')
    teacher_id = models.ForeignKey(u'Teachers', null=True, blank=True)
    subject_id = models.ForeignKey(u'Subjects', null=True, blank=True)
    group_id = models.ForeignKey(u'Groups', null=True, blank=True)
    speciality_id = models.ForeignKey(u'Spiciality', null=True, blank=True)
    from_date = models.DateTimeField(_(u'От дата'))
    to_date = models.DateTimeField(_(u'До дата'))
    is_full_time = models.BooleanField(default=False)
    
    class Meta(object):
        verbose_name = _(u'Програма')
        verbose_name_plural = _(u'Програма')
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True, verbose_name=_(u'добавена'))
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True, verbose_name=_(u'последна промяна'))
    
    def __unicode__(self):
        return _(u'%s' % self.pk)
    
    @classmethod
    def get_room_subject_teacher(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(room_id__number__icontains=get_request['room']) |  \
                                    Q(room_id__name__icontains=get_request['room']), \
                                    (Q(subject_id__full_name__icontains=get_request['subject']) |  \
                                    Q(subject_id__short_name__icontains=get_request['subject'])),
                                    (Q(teacher_id__name__icontains=get_request['teacher']) | \
                                    Q(teacher_id__short__icontains=get_request['teacher']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_subject_teacher(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls,(Q(subject_id__full_name__icontains=get_request['subject']) |  \
                                    Q(subject_id__short_name__icontains=get_request['subject'])),
                                    (Q(teacher_id__name__icontains=get_request['teacher']) | \
                                    Q(teacher_id__short__icontains=get_request['teacher']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_room_teacher(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(room_id__number__icontains=get_request['room']) |  \
                                    Q(room_id__name__icontains=get_request['room']), \
                                   (Q(teacher_id__name__icontains=get_request['teacher']) | \
                                    Q(teacher_id__short__icontains=get_request['teacher']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_only_room(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(room_id__number__icontains=get_request['room']) | Q(room_id__name__icontains=get_request['room']))
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_room_subject(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(room_id__number__icontains=get_request['room']) |  \
                                         Q(room_id__name__icontains=get_request['room']), \
                                        (Q(subject_id__full_name__icontains=get_request['subject']) |  \
                                         Q(subject_id__short_name__icontains=get_request['subject']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_only_subject(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(subject_id__full_name__icontains=get_request['subject']) | Q(subject_id__short_name__icontains=get_request['subject']) | Q(subject_id__short_name__icontains=get_request['subject']))
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_only_teacher(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(teacher_id__name__icontains=get_request['teacher']) | Q(teacher_id__short__icontains=get_request['teacher']))
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_free_rooms_from_to_date(cls, get_request):
        from api.serializers import RoomsSerializer
        
        from_date = datetime.strptime(get_request['from_date'], "%Y-%m-%d %H:%M:%S")
        to_date = datetime.strptime(get_request['to_date'], "%Y-%m-%d %H:%M:%S")

        get_all_busy_room = cls.objects.filter(
                                               (Q(from_date__lte=from_date) & \
                                                Q(to_date__gt=from_date)) | \
                                               (Q(from_date__lte=to_date) & 
                                                Q(to_date__gt=to_date)))
        
        print get_all_busy_room.query
        
        day_filter = Q()
        for x in get_all_busy_room:
            day_filter = day_filter & ~Q(id=(x.room_id).id)

        objects = get_list_or_404(Rooms, day_filter)
        serializer = RoomsSerializer(objects, many=True)
        return serializer.data
    
    @classmethod
    def get_free_rooms_from_to_seats(cls, get_request):
        from api.serializers import RoomsSerializer
        from_date = datetime.strptime(get_request['from_date'], "%Y-%m-%d %H:%M:%S")
        to_date = datetime.strptime(get_request['to_date'], "%Y-%m-%d %H:%M:%S")
        seats = get_request['seats']
        
        seats_tuple = cls.config_seats(seats)
        get_all_busy_room = cls.objects.filter(from_date__gte=from_date, to_date__lte=to_date)
        day_filter = Q()
        for x in get_all_busy_room:
            day_filter = day_filter & ~Q(id=(x.room_id).id)
        objects = get_list_or_404(Rooms.objects.all().filter(seats__gte=seats_tuple[0], seats__lte=seats_tuple[1]), day_filter)
        serializer = RoomsSerializer(objects, many=True)
        return serializer.data
    
    @classmethod
    def config_seats(cls, seats):
        seats = int(seats)
        if seats % 100 == 0:
            return (int(round(seats - (seats*(15.0/100)))), int(round(seats + (seats*(15.0/100)))))
        elif seats % 10 == 0:
            return (int(round(seats - (seats*(5.0/100)))), int(round(seats + (seats*(5.0/100)))))
        elif seats >= 1000:
            return (int(round(seats - (seats*(3.0/100)))), int(round(seats + (seats*(3.0/100)))))
        
    @classmethod
    def get_r_sp_t_su(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(speciality_id__full_name__icontains=get_request['speciality']) |  \
                                    Q(speciality_id__short_name__icontains=get_request['speciality']),
                                    (Q(room_id__number__icontains=get_request['room']) |  \
                                    Q(room_id__name__icontains=get_request['room'])), \
                                    (Q(subject_id__full_name__icontains=get_request['subject']) |  \
                                    Q(subject_id__short_name__icontains=get_request['subject'])),
                                    (Q(teacher_id__name__icontains=get_request['teacher']) | \
                                    Q(teacher_id__short__icontains=get_request['teacher']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_speciality(cls, get_request):
        from api.serializers import ScheduleSerializer
        print get_request['speciality']
        a = cls.objects.filter(Q(speciality_id__full_name=get_request['speciality']) |  \
                               Q(speciality_id__short_name=get_request['speciality']))
        
        print unicode(a.query)
        
        data = get_list_or_404(cls, Q(speciality_id__full_name__icontains=get_request['speciality']) |  \
                                    Q(speciality_id__short_name__icontains=get_request['speciality']))
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data