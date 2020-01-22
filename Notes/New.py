#!/usr/bin/env python3 
# Created by Chaz Davis on 2020-01-19

import argparse
import os
from os import path
from datetime import datetime

Home = os.path.expandvars("$HOME")
NotesDir = os.path.join(Home, 'Notes')

class New:
    def __init__(self, command, baseName, fileType, path):
        self.name = command
        self.baseName = baseName
        self.path = path
        self.fileType = fileType

        # create time stamp for empty baseName
        now = datetime.now()
        today = now.strftime("%Y-%m-%w:%H:%M")

        if baseName == 'quickNote':
            baseName = today
        else:
            baseName = baseName

        # Create the file Extensions for the passed fileType
        if fileType == 'latex':
            fileExt = '.tex'
        if fileType == 'markdown':
            fileExt = '.md'

        # create the destPath for the passed path
        if path == 'NotesDir':
            destPath = NotesDir
        if path == 'journal':
            destPath = os.path.join(NotesDir, 'Journal')
        if path == 'engineering':
            destPath = os.path.join(NotesDir, 'EngineeringJournal')
        if path == 'code':
            destPath = os.path.join(NotesDir, 'CodeIdeas')



        print(f'You\'d like to create a new note named {baseName}{fileExt} in {destPath}')
