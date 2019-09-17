#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple script to expand subtitle times in a file
in order to e.g. allow best syncing on/off commands.

Tested with .srt extension files only. Example:

$ subtitle_expand.py input_subtitle.srt
"""

from __future__ import print_function

import datetime, time

from os.path import splitext
from sys import argv

def subtitle_expand(input_file,
    output_file=None,
    seconds=0.1):
    '''
    Expands subtitle time. Accepts arguments:
      input_file: subtitle file name (required)
      output_file: output file name (optional)
      seconds: subtitle interval (default 100ms)
    '''
    num  = 0
    text = ''

    if not output_file:
        name, ext = splitext(input_file)
        output_file = name + '_NEW' + ext

    with open(input_file, 'r') as input_f:

      with open(output_file, 'w') as output_f:

        for line in input_f:
            content = line.rstrip('\n')

            try:    is_number = int(content)
            except: is_number = False
            else:   is_number = True

            if is_number:
                continue

            elif '-->' in content:
                start, end = content.split(' --> ')
                start      = str(start).split(',')[0]
                end        = str( end ).split(',')[0]
                start_time = datetime.datetime.strptime(start, '%H:%M:%S') # '%f'
                end_time   = datetime.datetime.strptime( end , '%H:%M:%S') # '%f'

            elif content.strip(' ') == '':

                start_new  = start_time

                while True:

                    end_new    = start_new + datetime.timedelta(seconds=seconds)

                    if end_new > end_time:
                        end_new = end_time

                    hh, mm, ss = start_new.strftime('%H:%M:%S,%f').split(':')
                    ss,  xx    = ss.split(',')
                    HH, MM, SS = end_new.strftime('%H:%M:%S,%f').split(':')
                    SS,  XX    = SS.split(',')

                    hh = "%02d" % (int(hh),)
                    mm = "%02d" % (int(mm),)
                    ss = "%02d" % (int(ss),)
                    xx = str("%03d" % (int(xx),))[:3]
                    HH = "%02d" % (int(HH),)
                    MM = "%02d" % (int(MM),)
                    SS = "%02d" % (int(SS),)
                    XX = str("%03d" % (int(XX),))[:3]

                    s = str(hh)+':'+str(mm)+':'+str(ss)+','+str(xx)
                    e = str(HH)+':'+str(MM)+':'+str(SS)+','+str(XX)

                    num += 1
                    output_f.write(str(num)+'\n')
                    output_f.write(s+' --> '+e+'\n')
                    output_f.write(text+'\n')

                    start_new = end_new

                    if end_new == end_time:
                        text = ''
                        break

            else: # subtitle text
                text = text + content + '\n'

if __name__ == "__main__":
    if len(argv)>1:
        input_file = argv[1]
        subtitle_expand(input_file)
    else: # print warning and exit
        print('Error: missing input file name.\n$ subtitle_expand.py input_subtitle.srt')
        raise SystemExit
