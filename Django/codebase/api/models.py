# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

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