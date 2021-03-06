#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from core.alert import *


def logo():
    from core.alert import write
    write('''    
   ______          __      _____ _____  
  / __ \ \        / /\    / ____|  __ \ 
 | |  | \ \  /\  / /  \  | (___ | |__) |
 | |  | |\ \/  \/ / /\ \  \___ \|  ___/ 
 | |__| | \  /\  / ____ \ ____) | |     
  \____/   \/  \/_/    \_\_____/|_|      
                          _   _      _   _             _            
                         | \ | |    | | | |           | |            
  github.com/viraintel   |  \| | ___| |_| |_ __ _  ___| | _____ _ __ 
  owasp.org              | . ` |/ _ \ __| __/ _` |/ __| |/ / _ \ '__|
  viraintel.com          | |\  |  __/ |_| || (_| | (__|   <  __/ |   
                         |_| \_|\___|\__|\__\__,_|\___|_|\_\___|_|   
                                               
    \n\n''')


def version():
    return int(sys.version_info[0])


def check(language):
    if 'linux' in sys.platform or 'darwin' in sys.platform:
        pass
        # os.system('clear')
    elif 'win32' == sys.platform or 'win64' == sys.platform:
        pass
        # os.system('cls')
    else:
        sys.exit(error(messages(language, 47)))
    if version() is 2 or version() is 3:
        pass
    else:
        sys.exit(error(messages(language, 48)))
    logo()
    return


def os_name():
    return sys.platform
