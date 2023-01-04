
__author__ = 'joswin'
# Code for tagging temporal expressions in text
# For details of the TIMEX format, see http://timex2.mitre.org/

import re
import datefinder #module for identifying date/time in text
import string
import os
import sys

# Requires eGenix.com mx Base Distribution
# http://www.egenix.com/products/python/mxBase/
try:
    from mx.DateTime import *
except ImportError:
    print """
Requires eGenix.com mx Base Distribution
http://www.egenix.com/products/python/mxBase/"""

# Predefined strings.
numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten| \
          eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen| \
          eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty| \
          ninety|hundred|thousand)"
day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
week_day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
month = "(january|february|march|april|may|june|july|august|september| \
          october|november|december)"
dmy = "(year|day|week|month)"
rel_day = "(today|yesterday|tomorrow|tonight|tonite)"
exp1 = "(before|after|earlier|later|ago)"
exp2 = "(this|next|last)"
iso = "\d+[/-]\d+[/-]\d+ \d+:\d+:\d+\.\d+"
year = "((?<=\s)\d{4}|^\d{4})"
regxp1 = "((\d+|(" + numbers + "[-\s]?)+) " + dmy + "s? " + exp1 + ")"