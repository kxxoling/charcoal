# coding: utf-8
import re


old_pixiv_image_filename_pattern = re.compile(r'''
^
(?P<author>.+)
\s-\s
(?P<name>.+)
\s\(
(?P<id>\d*)
\)\s
(?P<order>\d*)
(ページ)?
(\.(?P<ext>jpg|png|jpeg))?
''', re.VERBOSE)


pixiv_image_filename_pattern = re.compile(r'''
^\[
(?P<author>.+)
\]\_
(?P<name>.+)
\_
(?P<id>\d*)
\_
(?P<order>\d*)
(\.(?P<ext>jpg|png|jpeg))?
''', re.VERBOSE)


def auto_check_image(instance):
    # Overwrite image default show, is_restricted attr when it's created.
    if instance.id is None:
        instance.is_restricted = False
        instance.show = True

    pixiv_search = pixiv_image_filename_pattern.search(instance.title) or old_pixiv_image_filename_pattern.search(instance.title)
    if pixiv_search:
        author, name, pixiv_id, order = pixiv_search.groups()[:4]
        instance.title = u'%s - %s' % (author, name)
        instance.pixiv_id = int(pixiv_id)
        instance.pixiv_order = int(order or 0)
        instance.orig_link = instance.get_pixiv_link()
        return
    else:
        instance.title = instance.title.strip('.jpg').strip('.png').strip('.gif').strip().strip('_')

    # Set pixiv ID from link
    if instance.orig_link and instance.orig_link.startswith('https://www.pixiv.net/'):
        instance.pixiv_id = int(instance.orig_link.rsplit('=', 1)[-1])
    # Construct link from pixiv ID
    if not instance.orig_link and instance.pixiv_id:
        instance.orig_link = instance.get_pixiv_link()
    # Clean file name

