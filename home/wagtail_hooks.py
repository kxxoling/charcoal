# coding: utf-8
from django.utils.html import format_html, format_html_join
from django.conf import settings
from wagtail.wagtailcore import hooks
from wagtail.wagtailcore.whitelist import attribute_rule, check_url


@hooks.register('construct_whitelister_element_rules')
def whitelister_element_rules():
    return {
        'a': attribute_rule({'href': check_url, 'target': True}),
        'blockquote': attribute_rule({'class': True}),
    }


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'js/hallo_custombuttons.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )

    return js_includes + format_html(
        '''
        <script>
          registerHalloPlugin('blockquotebutton');
        </script>
        '''
    )


@hooks.register('insert_editor_css')
def editor_css():
    return format_html('<link rel="stylesheet" href="%sfa/css/font-awesome.min.css">' % settings.STATIC_URL)
