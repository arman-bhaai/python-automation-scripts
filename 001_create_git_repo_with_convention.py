#        /\          /\          /\          /\          /\          /\          /\          /\          /\          /\
#     /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\    /\//\\/\
#  /\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\//\\\///\\/\
# //\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\\//\/\\///\\
# \\//\/                                                                                                                \/\\//
#  \/                                              "In the Name of Allah"                                                  \/
#  /\                                                                                                                      /\
# //\\                                            Python Automation Scrpits                                               //\\
# \\//                                                                                                                    \\//
#  \/                                                                                                                      \/
#  /\           Script ID: 001                                                                                             /\
# //\\        Script Name: Create Git Repo with Convention                                                                //\\
# \\//        Description: This script creates a git repo maintaining your convention, commits                            \\//
#  \/                      changes, adds remote with user credentials (access token) and finally                           \/
#  /\                      creates a remote  and pushes the repo to the remote.                                            /\
# //\\                                                                                                                    //\\
# \\//        Author Name: Abu Bakar Siddique Arman (#arman_bhaai)                                                        \\//
#  \/               Email: arman.bhaai@gmail.com                                                                           \/
#  /\              GitHub: github.com/arman-bhaai                                                                          /\
# //\\           Facebook: fb.me/arman.bhaai                                                                              //\\
# \\//            Youtube: tiny.cc/arman-bhaai-on-youtube                                                                 \\//
#  \/                      bit.ly/arman-bhaai-on-youtube                                                                   \/
#  /\                                                                                                                      /\
# //\\      Creation Date: 2020-08-22                                                                                     //\\
# \\//            Version: v1.0                                                                                           \\//
#  \/     Versioning Date: 2020-08-22                                                                                      \/
#  /\                                                                                                                      /\
# //\\            License: Custom License                                                                                 //\\
# \\//                                                                                                                    \\//
#  \/        Dev Language: Python 3.6.9                                                                                    \/
#  /\              Dev OS: Linux Mint 19.3 (tricia)                                                                        /\
# //\\                                                                                                                    //\\
# \\//        Source Code: www.github.com/arman-bhaai/python-automation-scripts/001_create_git_repo_with_convention.py    \\//
#  \/          Video Demo: https://youtu.be/-JVjNtWLILM                                                                                             \/
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



########################## Import Packages ##############################!IMPAC!
# run the following command on your shell to install necessary packages
# "$ pip install sh selenium"
# package for manipulating shell commands
import sh
# package for manipulating browser activities
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# package to hault python processes
from time import sleep


##################### Define Primary (User Input) Variables ##################!PRIMVAR!
# github user credentials for pushing repo to remote
github_usr = 'arman-bhaai'
github_pass = 'PASSWORD'
github_access_token = 'TOKEN'
# repo name
repo_name = 'python-automation-scripts'
# repo description
repo_desc = 'A great collection of useful python scripts which I created to boost my works.'
# local parent dir of the repo
repo_parent_dir = '/home/antidote/projects-on-github'
# define branch name
commit_branch = 'master'
# define license file path
license_path = '/home/antidote/projects-on-github/zz-git-repo-template-files/LICENSE.txt'

# define contents for "zz_A_FRESH_START.md" file
a_fresh_start_str = """> ### "اعوذ بالله من الشیطان الرجیم"
> ### "I seek refuge in Allah from shaitan, the accursed one."

> ## "بسم الله الرحمن الرحيم"
> ## "In the name of Allah, the Most Gracious, the Most Merciful"

> # "إياك نعبد و إياك نستعين"
> # "It is You we worship and You we ask for help."
> ## [*- Al Fatihah : 5*](https://quran.com/1/5?translations=20)
"""

# define contents for "ReadMe.md" file
readme_str = """> ### "اعوذ بالله من الشیطان الرجیم"
> ### "I seek refuge in Allah from shaitan, the accursed one."
    
> ## "بسم الله الرحمن الرحيم"
> ## "In the name of Allah, the Most Gracious, the Most Merciful."
    
> # "إياك نعبد و إياك نستعين"
> # "It is You we worship and You we ask for help."
> ## [*- Al Fatihah : 05*](https://quran.com/1/5?translations=20)
<br>
<br>

* ### *Author* ---> **[#arman_bhaai](https://www.google.com/search?q=%23arman_bhaai&oq=%23arman_bhaai)** *(either click on this hashtag or make a google search to discover more about my works)*
* ### *My Personal Portfolio* ---> **[arman-bhaai.github.io](https://arman-bhaai.github.io)** *(some of my great projects are listed on my portfolio, so make sure you went through it)*
* ### *Find Me on Github* ---> **[github.com/arman-bhaai](https://github.com/arman-bhaai)**
* ### *Find Me on Facebook* ---> **[fb.me/arman.bhaai](https://www.facebook.com/arman.bhaai)**
* ### *Find Me on Youtube* ---> **[bit.ly/arman-bhaai-on-youtube](https://www.youtube.com/channel/UCUle8WAow1k5ATi3ta9lfkA)**
<br>
<br>

# *Documentation contents starts from here...*
"""


##################### Define Secondary (Generated) Variables ###################!SECVAR!
# remote repo to add remote on git
remote_repo_url = f'https://github.com/{github_usr}/{repo_name}.git'


################################# Start Working ################################!MAIN!
# create a new dir with repo name and initialize git on the dir
sh.mkdir(f'{repo_parent_dir}/{repo_name}')
sh.cd(f'{repo_parent_dir}/{repo_name}')
sh.git.init('.')

# create a file for the memory of first commit (my covention)
with open('zz_A_FRESH_START.md', 'a') as file_obj:
    file_obj.write(a_fresh_start_str)

# write readme.md
with open('ReadMe.md', 'a') as file_obj:
    file_obj.write(readme_str)

# copy license.txt file to current dir
sh.cp(license_path, '.')
# add all the files to staging area
sh.git.add('-A')
# conventional first commit
sh.git.commit('-m', '"بسم الله الرحمن الرحيم"')

# open chrome instance
driver = webdriver.Chrome()
# maximize chrome window
driver.maximize_window()
# go to my profile
driver.get(f'https://www.github.com/{github_usr}')
sleep(5)
# go to create repository url
driver.get('https://www.github.com/new')
sleep(3)
# populate username and password fields with account credentials and press submit button
inp_usr = driver.find_element_by_name('login')
inp_usr.clear()
inp_usr.send_keys(github_usr)
sleep(3)
inp_pass = driver.find_element_by_name('password')
inp_pass.clear()
inp_pass.send_keys(github_pass)
sleep(3)
inp_pass.send_keys(Keys.RETURN)
sleep(3)
# populate repo name and repo descripion fields with corresponding strings and press submit button
inp_repo_name = driver.find_element_by_id('repository_name')
inp_repo_name.send_keys(repo_name)
sleep(3)
inp_repo_desc = driver.find_element_by_id('repository_description')
inp_repo_desc.send_keys(repo_desc)
sleep(3)
inp_repo_desc.send_keys(Keys.RETURN)
sleep(4)
# close chrome instance
driver.close()

# add remote
# tokenize remote url so that the script can push the repo without user credentials
# tokenized url looks like --> https://username:token@github.com/username/project-repo.git
# warning! <-- tokenized url resides in repo's config file
# concept taken from --> https://www.tecmint.com/fix-git-user-credentials-for-https/
# concept taken from --> https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
tokenized_remote_repo_url = remote_repo_url[ : 8] + github_usr + ':' + github_access_token + '@' + remote_repo_url[8 : ]
sh.git.remote('add', 'origin', tokenized_remote_repo_url)
# push changes to remote
sh.git.push('origin', commit_branch)


################################### Final Output #################################!FOUT!
# show process summary
proc_summary = f"""
###################### Process Summary ########################
---------------------------------------------------------------

       Repository Name : {repo_name}
Repository Description : {repo_desc}
 Repository Parent Dir : {repo_parent_dir}
           Branch Name : {commit_branch}
 Repository Remote URL : {remote_repo_url}

---------------------------------------------------------------
                 Process Has Been Finished!!!
###############################################################
"""
print(proc_summary)
