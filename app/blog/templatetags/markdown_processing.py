import markdown as md
from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


# Fenced Code Blocks
# https://python-markdown.github.io/extensions/fenced_code_blocks/
@register.filter()
@stringfilter
def markdown(value):
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])
