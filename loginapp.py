# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 23:15:37 2018

@author: ASUS
"""

import dbconnector as db

def verifyCred(email, password):
    success, corpass=db.getPassword2(email)
    if success:
        if password==corpass:
            return True, "success"
        else:
            return False, "password mismatch"
    else:
        return False, corpass
        
    
def recordLogin(email):
    t=1

def loginmain(email, password):
    success, msg=verifyCred(email, password)
    if success:
        recordLogin(email)
        
    return success, msg