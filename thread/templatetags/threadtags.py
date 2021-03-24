from django import template
from django.db.models import Count
from ..models import Category

register = template.Library()

@register.inclusion_tag('thread/tags/category_tag.html')
def categorytag():
        ctx = {}
        ctx['category_list'] = Category.objects.annotate(
                count=Count('topic')).order_by('sort')
        return ctx