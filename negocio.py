#!/usr/bin/env python3
import pwd

#list all users in system

for users in pwd.getpwall():
    print(users.pw_name)