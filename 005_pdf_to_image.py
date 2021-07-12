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
#  /\              Script ID: 005                                                                                          /\
# //\\           Script Name: PDF to Image                                                                                //\\
# \\//           Description: This script can be used to convert pdf into images                                          \\//
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
# //\\         Creation Date: 2021-07-12                                                                                  //\\
# \\//               Version: v0.0.1                                                                                      \\//
#  \/        Versioning Date: 2021-07-12                                                                                   \/
#  /\                                                                                                                      /\
# //\\               License: Custom License                                                                              //\\
# \\//                                                                                                                    \\//
#  \/           Dev Language: Python 3.9.4                                                                                 \/
#  /\                 Dev OS: Windows 10 (Home)                                                                            /\
# //\\                                                                                                                    //\\
# \\//           Source Code: www.github.com/arman-bhaai/python-automation-scripts/005_pdf_to_image.py                    \\//
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
# $ pip install pymupdf
import logging
import argparse
import fitz
import pathlib
import os

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
sample usage: python 005_pdf_to_image.py -pdf doc.pdf -r 5
"""
aparser = argparse.ArgumentParser(description=ap_desc)
aparser.add_argument(
    '-pdf', '--pdf_path',
    required=True,
    help=r'eg: C:\Users\doc.pdf | doc.pdf'
)
aparser.add_argument(
    '-exp',
    '--export_path',
    default='',
    help=r'eg: <blank> | C:\Users\Output'
)
aparser.add_argument(
    '-fmt', '--format',
    default='page_%s',
    help='eg: page_(percent)s'
)
aparser.add_argument(
    '-ext', '--image_extension',
    default='jpg',
    help='eg: jpg | png'
)
aparser.add_argument(
    '-z', '--zoom_level',
    default='2',
    type=int,
    help='eg: 2 | 3 | 4'
)
aparser.add_argument(
    '-r', '--page_range',
    default='5',
    help='eg: 5 | full'
)
args = aparser.parse_args()



############### Variables ###############


doc_path = args.pdf_path # 'pd.pdf' # 'C:/Users/test/doc.pdf'
exp_path = args.export_path # 'C:/Users/test'
filename_format = args.format # 'image_%s' 
img_extension = args.image_extension # 'jpg'
zoom = args.zoom_level # 2
pg_range = args.page_range #

source_path = pathlib.Path(doc_path)
export_path = pathlib.Path(exp_path)
doc = fitz.open(source_path)

if pg_range.isdigit():
    pg_range = int(pg_range)
elif pg_range == 'full':
    pg_range = doc.page_count
else:
    print('invalid args')

page_count = 0
for page in range(pg_range):
    pg = doc[page]
    mat = fitz.Matrix(zoom, zoom)
    pix = pg.getPixmap(matrix=mat)
    if exp_path:
        out_filename = str(exp_path) + os.sep + str(filename_format % (page+1)) + '.' + img_extension
    else:
        out_filename = str(exp_path) + str(filename_format % (page+1)) + '.' + img_extension
    inf('Saving %s' % out_filename)
    pix.save(out_filename)
    page_count += 1

inf('%i pages have been converted' % page_count)