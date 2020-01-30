#!/usr/bin/env python3 
# Created by Chaz Davis on 2020-01-18
import argparse
import os
from datetime import datetime
from Notes.New import New
from Notes.Export import Export
from Notes.Open import Open

def main():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help="sub-command that are called along with note, they will take you to the the program you wish to have executed.")


    # creating the arguments to be passed for the 'note new' command
    new_parser = subparsers.add_parser('new', aliases=['nn'], help="used to create a new note, make if no name is given a quick-note will be created, and place it in the correct directory")
    new_parser.add_argument("baseName", nargs='?', default='quickNote', help="the basename of your new file")
    path_parser = new_parser.add_mutually_exclusive_group()
    path_parser.add_argument('-n', '--NotesDir', action='store_const', dest="path", const='NotesDir', help="Create a new note and place it in the ~/Notes directory")
    path_parser.add_argument('-j', '--journal', action='store_const', dest="path", const='journal', help="Create a new note and place it in the ~/Journal directory")
    path_parser.add_argument('-e', '--engineering', action='store_const', dest="path", const='engineering', help="Create a new note and place it in the EngineeringJournal directory")
    path_parser.add_argument('-c', '--code', action='store_const', dest='path', const='code', help="Create a new note and place it in the CodeIdeas directory")
    path_parser.set_defaults(path='NotesDir')
    # mutually exclusive parser for latex or markdown
    fileType_parser = new_parser.add_mutually_exclusive_group()
    fileType_parser.add_argument('-m', '--markdown', action='store_const', dest="fileType", const='markdown', help="Create a new note of fileType markdown")
    fileType_parser.add_argument('-x', '--latex', action='store_const', dest="fileType", const='latex', help="Create a new note of fileType Latex")
    fileType_parser.set_defaults(fileType='markdown')


    # create the arguments for the 'note export' command
    export_parser = subparsers.add_parser('export', aliases=['ex'], help="Export a note, file will be changed from either markdown or latex to either a docx file or a pdf and then moved to the Exports folder")
    exportType_parser = export_parser.add_mutually_exclusive_group()
    exportType_parser.add_argument('-p', '--pdf', action='store_const', dest="exportType", const='pdf', help="export a note to fileType pdf")
    exportType_parser.add_argument('-w', '--word', action='store_const', dest="exportType", const='word', help="Export a note to fileType docx")
    exportType_parser.set_defaults(exportType='pdf')

    # create the arguments for the 'note open' command
    open_parser = subparsers.add_parser('open', aliases=['op'], help="Open a note")


    try:
        args = parser.parse_args()
    except SystemExit:
        parser.print_help()
        raise

    # deciding the directory to create file in
    if args.command == 'new' or args.command == 'nn':
        New(**vars(args))
    if args.command == 'export' or args.command == 'ex':
        Export(**vars(args))
    if args.command == 'open' or args.command == 'op':
        Open(**vars(args))


if __name__ == "__main__":
    main()

