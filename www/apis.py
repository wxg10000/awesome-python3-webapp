#!/bin/env python3
# _*_ coding: utf-8 _*_


__author__ = 'Xiangui Wang'

'''
JSON API definition
'''

import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''
    def __init__(self, error, data='', message=''):
        super(APIError,self).__init__(message)
        self.error = error
        self.data = data
        self.message = message


class APIValueError(APIError):
    '''

    '''
