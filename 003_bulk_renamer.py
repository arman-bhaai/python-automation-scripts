#        /\          /\          /\          /\          /\          /\          /\          /\          /\          /\
#     /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\
#  /\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\
# //\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\
# \\//\/                                                                                                                \/\\//
#  \/                                                "In the Name of Allah"                                                \/
#  /\                                              ===========================                                             /\
# //\\                                              Python Automation Scripts                                             //\\
# \\//                                                                                                                    \\//
#  \/                                                                                                                      \/
#  /\              Script ID: 003                                                                                          /\
# //\\           Script Name: Bulk Renamer                                                                                //\\
# \\//           Description: This script can be used to rename files or directories in mass                              \\//
#  \/                                                                                                                      \/
#  /\                                                                                                                      /\
# //\\                                                                                                                    //\\
# \\//           Author Name: Abu Bakar Siddique Arman (#arman_bhaai)                                                     \\//
#  \/                  Email: arman.bhaai@gmail.com                                                                        \/
#  /\                 GitHub: github.com/arman-bhaai                                                                       /\
# //\\              Facebook: fb.me/arman.bhaai                                                                           //\\
# \\//               Youtube: tiny.cc/arman-bhaai-on-youtube                                                              \\//
#  \/                         bit.ly/arman-bhaai-on-youtube                                                                \/
#  /\                                                                                                                      /\
# //\\         Creation Date: 2021-06-05                                                                                  //\\
# \\//               Version: v0.0.1                                                                                      \\//
#  \/        Versioning Date: 2021-06-05                                                                                   \/
#  /\                                                                                                                      /\
# //\\               License: Custom License                                                                              //\\
# \\//                                                                                                                    \\//
#  \/           Dev Language: Python 3.9.4                                                                                 \/
#  /\                 Dev OS: Windows 10 (Home)                                                                            /\
# //\\                                                                                                                    //\\
# \\//           Source Code: www.github.com/arman-bhaai/python-automation-scripts/003_bulk_renamer.py                    \\//
#  \/             Video Demo: ###                                                                                          \/
#  /\                                                                                                                      /\
# //\\/\                                                                                                                /\//\\
# \\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\//
#  \/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/
#     \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/    \/\\//\/
#        \/          \/          \/          \/          \/          \/          \/          \/          \/          \/

#       ,
#   /\^/`\
#  | \/   |                                         Custom License!!!
#  | |    |                                                                                                       jgs
#  \ \    /                                                                                                     _ _
#   '\\//'                      Copyright (c) 2020 Abu Bakar Siddique Arman (#arman_bhaai)                    _{ ' }_
#     ||                                                                                                     { `.!.` }
#     ||                                                                                                     ',_/Y\_,'
#     ||                 Only Muslim brothers and sisters may use this file/project/source-code.               {_,_}
#     ||          And bear in mind that this file/project/source-code may only be used in an islamically         |
#     ||             lawful (halaal) purpose/project. So, any kinds of islamically unlawful (haraam)             |
#     ||  ,            implementation/use of this file/project/source-code is strictly prohibited!               |
# |\  ||  |\                                                                                                     |
# | | ||  | |                For any further queries, contact me at --> arman.bhaai@gmail.com                  (\|  /)
# | | || / /                                                                                                    \| //
#  \ \||/ /                                                                                                      |//
#   `\\//`   \   \./    \\   \./    \\   \./    \\   \./    \\   \./    \\   \./    \\   \./    \\   \./    \ \\ |/ /
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



#################################### Import Packages ####################################!IMPAC
import pathlib
import os
import logging
import sys
import argparse

############### Logger Configs ###############
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
# logging.basicConfig(format='%(levelname)s: %(message)s', filename='debug.log', level=logging.DEBUG, filemode='w')

# aliases for logging
def dbg(msg):
    logging.info(msg)

def inf(msg):
    logging.info(msg)

def err(msg):
    logging.error(msg)

############### CLI Configs ###############
aparser = argparse.ArgumentParser()
aparser.add_argument(
    'init_page_count',
    type=int,
    help='Resume page count'
)
aparser.add_argument(
    '-gp',
    '--glob_pattern',
    default='*.jpg',
    help='specify the name pattern of the files you want to rename'
)
aparser.add_argument(
    '-p', '--paper_name',
    default='bio1',
    help='eg: bio1'
)
aparser.add_argument(
    '-c', '--chp_name',
    default='ch1',
    help='specify the chapter name. \
            eg: ch1'
)
aparser.add_argument(
    '-ext', '--file_extension',
    default='jpg',
    help='eg: jpg'
)
args = aparser.parse_args()
###########################################


new_name_prefix = f'pg{str(args.init_page_count).zfill(3)}'

p = pathlib.Path()
fnames = p.glob(args.glob_pattern)
fnames_check = p.glob(args.glob_pattern)
if next(fnames_check, None) is None:
    err('No match found! Please input glob pattern correctly.')
    sys.exit()

total_rename_count = 1
for fname in fnames:
    new_path_name = f'{args.paper_name}_pg{str(args.init_page_count).zfill(3)}_{args.chp_name}.{args.file_extension}'
    inf(f'Renaming: "{fname}" >> "{new_path_name}"')
    os.rename(fname, new_path_name)
    args.init_page_count += 1
    total_rename_count +=1
inf(f'Total Renamed Files: {total_rename_count}')