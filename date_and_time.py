#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

from datetime import datetime 

# datetime.now() - the current date and time
now = datetime.now()


current_year = now.year
current_month = now.month
current_day = now.day

print now.year
print now.month
print now.day

print '%s-%s-%s' % (now.year, now.month, now.day) # 2014-02-19
print '%s/%s/%s' % (now.month, now.day, now.year) # 6/25/2017
print '%s:%s:%s' % (now.hour, now.minute, now.second) # 18:18:33
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second) # 6/25/2017 18:21:17