#!/usr/bin/env python3 
# Created by Chaz Davis on 2020-01-19

import argparse
import os
from os import path
from dynmen import Menu
import subprocess

class Open:
    def __init__(self, command):
        self.name = command
        
        Home = os.path.expandvars("$HOME")
        NotesDir = os.path.join(Home, 'Notes')

        print('Gathering List of notes to be opened')
        files = []
        fileNames = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(NotesDir):
            for file in f:
                if '.md' in file or '.tex' in file:
                    files.append(os.path.join(r, file))
                    fileNames.append(file)
        
        cmd = ['rofi', '-dmenu']
        menu= Menu(cmd)
        out = menu(fileNames)
        result = out.selected
        print(result)

        for fn, fl in zip(fileNames, files):
            if result == fn:
                subprocess.run(['nvim', fl])
            else:
                continue
