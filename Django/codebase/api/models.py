# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.query_utils import Q
from django.shortcuts import get_list_or_404
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

class Teachers(models.Model):
    name = models.CharField(_(u'Име'), max_length=64, null=False, blank=False)
    degree = models.CharField(_(u'Титла'), max_length=16, null=False, blank=False)
    short = models.CharField(_(u'Инициали'), max_length=5, null=False, blank=False)
    
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
    name = models.CharField(_(u'Име на стая'), max_length=32)
    floor = models.CharField(_(u'Етаж'), max_length=7)
    seats = models.IntegerField(_(u'Брой места'))
    number = models.CharField(_(u'Номер на стая'), max_length=4)
    
    is_computer_room = models.BooleanField()
    
    created = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True, verbose_name=_(u'добавена'))
    updated = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True, verbose_name=_(u'последна промяна'))
    
    class Meta(object):
        verbose_name = _(u'Стаи')
        verbose_name_plural = _(u'Стаи')
        
    def __unicode__(self):
        return _(u'%s' % self.name)
        
class Schedule(models.Model):
    room_id = models.ForeignKey(u'Rooms')
    teacher_id = models.ForeignKey(u'Teachers')
    subject_id = models.ForeignKey(u'Subjects')
    group_id = models.ForeignKey(u'Groups')
    from_date = models.DateTimeField(_(u'От дата'))
    to_date = models.DateTimeField(_(u'До дата'))
    is_full_time = models.BooleanField()
    
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
        
        data = get_list_or_404(cls, Q(room_id__number__contains=get_request['room']) |  \
                                    Q(room_id__name__contains=get_request['room']), \
                                    (Q(subject_id__full_name__contains=get_request['subject']) |  \
                                    Q(subject_id__short_name__contains=get_request['subject'])),
                                    (Q(teacher_id__name__contains=get_request['teacher']) | \
                                    Q(teacher_id__short__contains=get_request['teacher']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_subject_teacher(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls,(Q(subject_id__full_name__contains=get_request['subject']) |  \
                                    Q(subject_id__short_name__contains=get_request['subject'])),
                                    (Q(teacher_id__name__contains=get_request['teacher']) | \
                                    Q(teacher_id__short__contains=get_request['teacher']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_room_teacher(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(room_id__number__contains=get_request['room']) |  \
                                    Q(room_id__name__contains=get_request['room']), \
                                   (Q(teacher_id__name__contains=get_request['teacher']) | \
                                    Q(teacher_id__short__contains=get_request['teacher']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_only_room(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(room_id__number__contains=get_request['room']) | Q(room_id__name__contains=get_request['room']))
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_room_subject(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(room_id__number__contains=get_request['room']) |  \
                                         Q(room_id__name__contains=get_request['room']), \
                                        (Q(subject_id__full_name__contains=get_request['subject']) |  \
                                         Q(subject_id__short_name__contains=get_request['subject']))
                               )
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_only_subject(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(subject_id__full_name__contains=get_request['subject']) | Q(subject_id__short_name__contains=get_request['subject']))
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_only_teacher(cls, get_request):
        from api.serializers import ScheduleSerializer
        
        data = get_list_or_404(cls, Q(teacher_id__name__contains=get_request['teacher']) | Q(teacher_id__short__contains=get_request['teacher']))
        serializer = ScheduleSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_free_rooms_from_to_date(cls, get_request):
        from api.serializers import RoomsSerializer

        from_date = datetime.strptime(get_request['from_date'], "%Y-%m-%d %H:%M:%S")
        to_date = datetime.strptime(get_request['to_date'], "%Y-%m-%d %H:%M:%S")
        
        get_all_busy_room = get_list_or_404(cls, from_date__gte=from_date, to_date__lte=to_date)
        
        day_filter = Q()
        for x in get_all_busy_room:
            day_filter = day_filter & ~Q(id=(x.room_id).id)
        
        objects = get_list_or_404(Rooms, day_filter)
        serializer = RoomsSerializer(objects, many=True)
        return serializer.data