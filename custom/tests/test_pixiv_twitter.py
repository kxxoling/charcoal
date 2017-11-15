# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

import pytest

from custom.utils import old_pixiv_image_filename_pattern, pixiv_image_filename_pattern
from custom.utils import twitter_image_filename_pattern


@pytest.fixture(scope='module')
def pixiv_fixtures():
    return (
        (
            '[もねてぃ]_チャイナ慧音先生_59192484_',
            ('もねてぃ', 'チャイナ慧音先生', '59192484', ''),
            {
                'ext': None,
                'author': 'もねてぃ',
                'name': 'チャイナ慧音先生',
                'id': '59192484',
                'order': '',
            }
        ),
        (
            '[もねてぃ]_チャイナ慧音先生_59192484_.jpg',
            ('もねてぃ', 'チャイナ慧音先生', '59192484', ''),
            {
                'ext': 'jpg',
                'author': 'もねてぃ',
                'name': 'チャイナ慧音先生',
                'id': '59192484',
                'order': '',
            }
        ),
    )  # yapf: disable


@pytest.fixture(scope='module')
def old_pixiv_fixtures():
    return (
        (
            '狸狸 - 泣き終わりましたか？ (9817326) ',
            ('狸狸', '泣き終わりましたか？', '9817326', ''),
            {
                'ext': None,
                'author': '狸狸',
                'name': '泣き終わりましたか？',
                'id': '9817326',
                'order': '',
            }
        ),
        (
            '狸狸 - 泣き終わりましたか？ (9817326) .jpg',
            ('狸狸', '泣き終わりましたか？', '9817326', ''),
            {
                'ext': 'jpg',
                'author': '狸狸',
                'name': '泣き終わりましたか？',
                'id': '9817326',
                'order': '',
            }
        ),
    )  # yapf: disable


@pytest.fixture(scope='module')
def twitter_fixtures():
    return (
        (
            '[lidukelaya]_912995296048590848_据说是放一起光环很爽的组合_DKucDZrVAAAPMDE',
            ('lidukelaya', '912995296048590848', '据说是放一起光环很爽的组合', 'DKucDZrVAAAPMDE'),
            {
                'ext': None,
                'author': 'lidukelaya',
                'name': '据说是放一起光环很爽的组合',
                'pk': '912995296048590848',
                'hash': 'DKucDZrVAAAPMDE',
            }
        ),
        (
            '[lidukelaya]_912995296048590848_据说是放一起光环很爽的组合_DKucDZrVAAAPMDE.jpg',
            ('lidukelaya', '912995296048590848', '据说是放一起光环很爽的组合', 'DKucDZrVAAAPMDE', 'jpg'),
            {
                'ext': 'jpg',
                'author': 'lidukelaya',
                'name': '据说是放一起光环很爽的组合',
                'pk': '912995296048590848',
                'hash': 'DKucDZrVAAAPMDE',
            }
        ),
    )  # yapf: disable


def test_pixiv_pattern(pixiv_fixtures):
    for pixiv_fixture in pixiv_fixtures:
        filename, groups, groupdict = pixiv_fixture
        search = pixiv_image_filename_pattern.search(filename)
        assert search.groups()[:4] == groups
        assert search.groupdict() == groupdict


def test_old_pixiv_pattern(old_pixiv_fixtures):
    for fixture in old_pixiv_fixtures:
        filename, groups, groupdict = fixture
        search = old_pixiv_image_filename_pattern.search(filename)
        assert search.groups()[:4] == groups
        assert search.groupdict() == groupdict


def test_twitter_pattern(twitter_fixtures):
    for fixture in twitter_fixtures:
        filename, groups, groupdict = fixture
        search = twitter_image_filename_pattern.search(filename)
        assert search.groups()[:4] == groups[:4]
        assert search.groupdict() == groupdict
