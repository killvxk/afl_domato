#!/usr/bin/env python
# encoding: utf-8
'''
Simple Chunk Cross-Over Replacement Module for AFLFuzz

@author:     Christian Holler (:decoder)

@license:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

@contact:    choller@mozilla.com
'''

import random
from grammar import Grammar

jsgrammar = Grammar()

def init(seed):
    '''
    Called once when AFLFuzz starts up. Used to seed our RNG.
    '''
    # CheckGrammar(jsgrammar)
    err = jsgrammar.parse_from_file('js.txt')
    return 0

def fuzz(buf, add_buf):
    '''
    Called per fuzzing iteration.
    '''
    result_string = jsgrammar._generate_code(1)
    #result_string = "function foo() { o = Error(); for (var s in o) { print(o[s]); o = Error(); } } for (var i = 0; i < 100; ++i) { foo(); }"
    #print result_string
    ret = bytearray()
    ret.extend(result_string)

    # Return data
    return ret

if __name__ == '__main__':
    fuzz()
