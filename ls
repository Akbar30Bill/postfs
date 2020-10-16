#!/bin/python
import os
import dbcon
result = dbcon.runq(f'select * from "{dbcon.getpwd()}"', result_type = 999)
print(result)
