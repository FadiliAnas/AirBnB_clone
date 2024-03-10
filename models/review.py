#!/usr/bin/python3
"""This module defines the class method"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class represents a review model"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
