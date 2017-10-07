# coding: utf-8
from django import template

register = template.Library()


@register.inclusion_tag('_pagination.html')
def pagination(lst):
    start = 1
    end = lst.paginator.num_pages + 1
    width = 3
    current = lst.number
    has_left_ellips = (current - width) > (start + 1)
    has_right_ellips = (end - width) > (current + 1)
    page_range = range(max(start, current - width), current)\
        + [ current ]\
        + range(current + 1, min(end, current + width))

    return dict(
        start=start,
        end=end,
        current=current,
        has_left_ellips=has_left_ellips,
        has_right_ellips=has_right_ellips,
        show_start=(page_range[0] != start),
        show_end=(page_range[-1] != end),
        page_range=page_range,
        has_previous=lst.has_previous(),
        has_next=lst.has_next(),
        previous_page_number=lst.previous_page_number,
        next_page_number=lst.next_page_number,
    )
