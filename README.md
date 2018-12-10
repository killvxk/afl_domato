# afl_domato
it combines afl and domato, afl for detecting crash and domato for generating samples.
For more imformation, you can refer to http://lcamtuf.coredump.cx/afl/ and https://github.com/googleprojectzero/domato.
Afl's python extension is copied from https://github.com/choller/afl/blob/master/docs/mozilla/python_modules.txt.

# 1. build 
CFLAGS="-DUSE_PYTHON -I/usr/include/python2.7" LDFLAGS="-lpython2.7" make

# 2. run
AFL_PYTHON_MODULE="pymodules.domato_fuzz" PYTHONPATH=. ./afl-fuzz

