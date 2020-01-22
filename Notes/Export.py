#!/usr/bin/env python3 
# Created by Chaz Davis on 2020-01-19

import argparse
import os
from os import path
from dynmen import Menu
import subprocess
import shutil


class Export:
   def __init__(self, command, exportType):
      self.name = command
      self.exportType = exportType

      Home = os.path.expandvars("$HOME")
      NotesDir = os.path.join(Home, 'Notes')
      ExportDir = os.path.join(Home, 'Exports')

      if exportType == 'pdf':
         exportExt = '.pdf'
      if exportType == 'word':
         exportExt = '.docx'

      print(f"you'd like to export a file with {exportExt}")
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

      for fn, fl in zip(fileNames, files):
         if result == fn:
            baseName, baseExt = os.path.splitext(fn)
            newName = baseName + exportExt
            srcDir = os.path.dirname(fl)
            print(f"you'd like to export {baseName}{baseExt} from {srcDir} as {newName} to the {ExportDir}")
            os.chdir(srcDir)
            subprocess.run(['pandoc', '-s', fn, '-o', newName])
            shutil.move(newName, ExportDir)
         else:
            continue
