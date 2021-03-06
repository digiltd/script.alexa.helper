#!/usr/bin/python

from utils import process_method_on_list
from kodidb import KodiDb


class Artists(object):
  def __init__(self, addon, options):
    self.addon = addon
    self.options = options
    self.kodidb = KodiDb()

  def search(self):
    '''search for artists that match a given string'''
    all_items = self.kodidb.artists()
    return process_method_on_list(self.process_artist, all_items)

  def process_artist(self, item):
    '''transform the json received from kodi into something we can use'''
    item['file'] = 'musicdb://artists/%s' % item['artistid']
    item['isFolder'] = True
    return item
