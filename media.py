# coding=utf-8

"""
Module to display movie object, attributes and instances
"""

class Movie():
    """
    Class object stores movie related information
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        Initialize instance of class Movie

        :param title: string
        :param poster_image_url: string
        :param trailer_youtube_url: string
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
