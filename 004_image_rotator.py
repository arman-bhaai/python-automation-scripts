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
#  /\              Script ID: 004                                                                                          /\
# //\\           Script Name: Image Skew Fixer                                                                            //\\
# \\//           Description: This script can be used to rotate images to given degrees and fix image skew.               \\//
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
# \\//           Source Code: www.github.com/arman-bhaai/python-automation-scripts/004_image_skew_fixer.py                \\//
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
# "$ pip install pillow"
import logging
import argparse
from PIL import Image, ImageDraw

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
sample usage: py 004_image_rotator.py 8 /rr -5/5/1 #show images
sample usage: py 004_image_rotator.py 8 /s 5 # save image with angle
"""
aparser = argparse.ArgumentParser(description=ap_desc, prefix_chars='/')
aparser.add_argument(
    'page_no',
    type=int,
    help='Page number of the image which we\'re gonna rotate'
)
aparser.add_argument(
    '/p', '//paper_no',
    default='bio1',
    help='eg: bio1'
)
aparser.add_argument(
    '/c', '//chp_no',
    default='ch1',
    help='specify the chapter name. \
            eg: ch1'
)
aparser.add_argument(
    '/s', '//save_img',
    type=int,
    help='Takes an angle. Rotates it  and then saves with previous filename.',
)
group = aparser.add_mutually_exclusive_group()
group.add_argument(
    '/r', '//rot_angle',
    type=int,
    help='Angle of rotation. Positive values are Counter-Clockwise. Negative values are Clockwise. '
)
group.add_argument(
    '/rr', '//angle_range',
    help='eg: -10/10/5 # start-stop-step'
)
args = aparser.parse_args()
###########################################


def show_rotation_set(im):
    rot_rng_start = int(args.angle_range.split('/')[0])
    rot_rng_end = int(args.angle_range.split('/')[1])
    rot_rng_step = int(args.angle_range.split('/')[2])
    rot_angles = [angle for angle in range(rot_rng_start, rot_rng_end+1, rot_rng_step)]
    total_img_count = len(rot_angles)
    (w,h) = im.size
    im_res = im.resize((w//4, h//4))
    (imr_w, imr_h) = im_res.size # imr means image resized
    mf_width = (imr_w+200)*4 # mf means main frame
    mf_height = (imr_h+200)*(total_img_count/4)*1.2 # 4 x n image table
    main_frame = Image.new('RGB', (int(mf_width), int(mf_height)), '#ccc') # create main frame for n small images
    paste_x = 100 # for pasting small images to main frame
    paste_y = 100
    small_im_count = 1
    for rot_angle in rot_angles:
        im_rot = im_res.rotate(rot_angle, expand=True)
        draw = ImageDraw.Draw(im_rot)
        for i in range(30, imr_h-30, 10):
            draw.line([(0, i),(imr_w, i)], '#ff0000')
        draw.text((150,100), f'Angle: {rot_angle}', '#0000ff')
        main_frame.paste(im_rot, (paste_x, paste_y))
        paste_x += imr_w+150 # shift image to the next column
        if small_im_count % 4 == 0: # if 4 images are placed, switch image to the first column and next row 
            paste_x = 100
            paste_y += imr_h+150
        small_im_count += 1
    main_frame.show()

def confirm(im, img_path):
    inf(f'Saving image as : {img_path}...')
    # im.save('edt.jpg', quality=1)
    im = im.rotate(args.save_img)
    im.save(img_path)

def main():
    img_path = f'{args.paper_no}_pg{str(args.page_no)}_{args.chp_no}.jpg'
    inf(f'Working on Image: {img_path}')
    im = Image.open(img_path)
    if args.angle_range:
        show_rotation_set(im)

    if args.save_img:
        confirm(im, img_path)


if __name__ == '__main__':
    main()