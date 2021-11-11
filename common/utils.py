from urllib import parse

from cluster import settings


def construct_media_url(relative_url):
    return parse.urlparse(settings.MEDIA_URL, relative_url).scheme