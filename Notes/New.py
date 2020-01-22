#!/usr/bin/env python3 
# Created by Chaz Davis on 2020-01-19

import argparse
import os
from os import path
import datetime as dt
from datetime import datetime as dtt
import subprocess

Home = os.path.expandvars("$HOME")
NotesDir = os.path.join(Home, 'Notes')

class New:
    def __init__(self, command, baseName, fileType, path):
        self.name = command
        self.baseName = baseName
        self.path = path
        self.fileType = fileType

        # create time stamp for empty baseName
        now = dtt.now()
        today = now.strftime("%Y-%m-%w:%H:%M")
        date = dt.date.today()

        if baseName == 'quickNote':
            baseName = today
        else:
            baseName = baseName

        # Create the file Extensions for the passed fileType
        if fileType == 'latex':
            fileExt = '.tex'
            fileHeader = '\document{article}\n\n\\begin{document}\n\n\\author{Chaz Davis}\n\n\\maketitle\n\n'
        if fileType == 'markdown':
            fileExt = '.md'
            fileHeader =  f'[//]: # (Created by Chaz Davis on {date})'

        # create the destPath for the passed path
        if path == 'NotesDir':
            destPath = NotesDir
        if path == 'journal':
            destPath = os.path.join(NotesDir, 'Journal')
        if path == 'engineering':
            destPath = os.path.join(NotesDir, 'EngineeringJournal')
        if path == 'code':
            destPath = os.path.join(NotesDir, 'CodeIdeas')

        fileName = baseName + fileExt
        os.chdir(destPath)
        with open(fileName, 'a+') as f:
            f.writelines(fileHeader)
            os.stat(fileName)
            os.chmod(fileName, 0o751)
        subprocess.run(['nvim', fileName])
