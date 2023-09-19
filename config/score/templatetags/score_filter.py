from django import template
import time

register = template.Library()


@register.filter
def sub(value, arg):
    return value[arg][0]


@register.filter
def GetChampionName(value, arg):
    return value[arg]['name']


@register.filter
def Division(value, arg):
    return value/arg


@register.filter
def LenArray(value):
    return len(value)
