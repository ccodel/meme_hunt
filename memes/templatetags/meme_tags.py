from django import template

from meme_hunt.lib.time import TimeConverter

register = template.Library()

# Calculates whether the hints are visible given time range
# Assumes that at time = 0, the first hint is visible
@register.filter
def hint_visible(meme, num):
    assert(1 <= num and num <= 7)

    now = TimeConverter.now()
    start_date = TimeConverter.min(meme.start_date)
    end_date = TimeConverter.max(meme.end_date)

    elapsed_secs = (now - start_date).total_seconds()
    total_secs = (end_date - start_date).total_seconds()
    return (elapsed_secs / total_secs) > ((num - 1) / 7)
