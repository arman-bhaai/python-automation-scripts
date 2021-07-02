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
# \\//               Version: v0.0.2                                                                                      \\//
#  \/        Versioning Date: 2021-06-09                                                                                   \/
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
ap_desc = """\
sample usage: python 003_bulk_renamer.py -b plus -ipg 5 -p bio1 -c 12 -iss 3 -ise 10
"""
aparser = argparse.ArgumentParser(description=ap_desc)
aparser.add_argument(
    '-ipg', '--init_page_count',
    type=int,
    required=True,
    help='Resume page count'
)
aparser.add_argument(
    '-gp',
    '--glob_pattern',
    default='*.jpg',
    help='specify the name pattern of the files you want to rename'
)
aparser.add_argument(
    '-p', '--paper_code',
    default='bio1',
    help='eg: bio1'
)
aparser.add_argument(
    '-c', '--chp_no',
    default='ch1',
    help='specify the chapter name. \
            eg: ch1'
)
aparser.add_argument(
    '-ext', '--file_extension',
    default='jpg',
    help='eg: jpg'
)
aparser.add_argument(
    '-b', '--book',
    required=True,
    help='eg: plus/royal/tbook'
)
aparser.add_argument(
    '-iss', '--img_selection_start',
    help='eg: 55'
)
aparser.add_argument(
    '-ise', '--img_selection_end',
    help='eg: 60'
)
args = aparser.parse_args()



############### Variables ###############
init_page_count = args.init_page_count
glob_pattern = args.glob_pattern
book = args.book
paper_code = args. paper_code
chp_no = args.chp_no
file_ext = args.file_extension
img_sel_start =  args.img_selection_start #'CCI_000208'
img_sel_end = args.img_selection_end #'CCI_000212'


new_name_prefix = f'pg{str(args.init_page_count).zfill(3)}'
# img_sel_start_path = f'{img_sel_start}.{file_ext}'
# img_sel_end_path = f'{img_sel_end}.{file_ext}'
if img_sel_start:
    img_sel_start_path = f'CCI_{img_sel_start.zfill(6)}.{file_ext}'
    img_sel_end_path = f'CCI_{img_sel_end.zfill(6)}.{file_ext}'
    img_start_found = False

p = pathlib.Path()
fnames = p.glob(glob_pattern)
fnames_check = p.glob(glob_pattern)
if next(fnames_check, None) is None:
    err('No match found! Please input glob pattern correctly.')
    sys.exit()

total_rename_count = 1
for fname in fnames:
    # skip loop until start point has been found
    if img_sel_start:
        if not str(fname) == img_sel_start_path:
            if not img_start_found:
                continue
        else:
            img_start_found = True
    new_path_name = f'{book}_{str(init_page_count).zfill(4)}_{paper_code}_ch{str(chp_no).zfill(2)}.{file_ext}'
    inf(f'Renaming: "{fname}" >> "{new_path_name}"')
    os.rename(fname, new_path_name)
    init_page_count += 1
    total_rename_count +=1
    # exit loop if loop reached to last desired image
    if img_sel_end:
        if str(fname) == img_sel_end_path:
            break
inf(f'Total Renamed Files: {total_rename_count-1}')