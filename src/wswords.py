#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, 2009 Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
#
# 
import string
from lang import to as language

class wsWords():
    def __init__(self, wordlist = [], maxlength = 15):
        self.wordlist = wordlist
        self.maxlength = maxlength
        self.wordlist_rejected = []

    def sanitize(self, wordlist = None, maxlength = None):
        """
        Sanitise the Wordlist by building a list of acceptable characters for a word
        rejecting 
        """
        lang = language()
        
        if wordlist is None:
            wordlist = self.wordlist

        if maxlength is None:
            maxlength = self.maxlength
        
        goodwords = []
        longwords = []
        
        for word in wordlist:
            if len(word) == 0:
                continue
            word = lang.w_Tokens(word)[0]            
            if len(word) > maxlength:
                longwords.append(word)
            else:
                goodwords.append(word)            
        return goodwords, longwords
