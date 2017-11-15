# coding: utf-8
import re

old_pixiv_image_filename_pattern = re.compile(
    r'''
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
''', re.VERBOSE
)

pixiv_image_filename_pattern = re.compile(
    r'''
^\[
(?P<author>.+)
\]\_
(?P<name>.+)
\_
(?P<id>\d*)
\_
(?P<order>\d*)
(\.(?P<ext>jpg|png|jpeg))?
''', re.VERBOSE
)

twitter_image_filename_pattern = re.compile(
    r'''
^\[
(?P<author>.+)
\]\_
(?P<pk>\d+)
\_
(?P<name>.*)
\_
(?P<hash>\w*)
(\.(?P<ext>jpg|png|jpeg))?
''', re.VERBOSE
)


def auto_check_image(instance):
    # Overwrite image default show, is_restricted attr when it's created.
    if instance.id is None:
        instance.is_restricted = False
        instance.show = True

    pixiv_search = pixiv_image_filename_pattern.search(
        instance.title
    ) or old_pixiv_image_filename_pattern.search(instance.title)
    if pixiv_search:
        author, name, pixiv_id, order = pixiv_search.groups()[:4]
        instance.title = u'%s - %s' % (author, name)
        instance.pixiv_id = int(pixiv_id)
        instance.pixiv_order = int(order or 0)
        instance.orig_link = instance.get_pixiv_link()
        return
    else:
        twitter_search = twitter_image_filename_pattern.search(instance.title)
        if twitter_search:
            author, twitter_pk, name, hash_ = twitter_search.groups()[:4]
            instance.title = u'%s - %s - %s' % (author, name, hash_)
            instance.orig_link = instance.orig_link or 'https://twitter.com/%s/status/%s' % (
                author, twitter_pk
            )
        else:
            instance.title = instance.title\
                .strip('.jpg').strip('.png').strip('.gif').strip().strip('_')

    # Set pixiv ID from link
    if instance.orig_link:
        try:
            from urllib.parse import urlparse
        except ImportError:
            from urlparse import urlparse
        parsed = urlparse(instance.orig_link)
        if parsed.hostname == 'www.pixiv.net':
            # It's a pixiv image!
            instance.pixiv_id = int(instance.orig_link.rsplit('=', 1)[-1])
        elif parsed.hostname.endswith('.deviantart.com'):
            # It's a deviantart image!
            instance.da_username = parsed.hostname.replace('.deviantart.com', '')
            instance.da_path = parsed.path.rsplit('/', 1)[-1]
            instance.da_id = int(instance.da_path.rsplit('-', 1)[-1])

    # Construct link from pixiv ID
    if not instance.orig_link and instance.pixiv_id:
        instance.orig_link = instance.get_pixiv_link()
