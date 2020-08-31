#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dchanna
#
# Created:     12/07/2020
# Copyright:   (c) dchanna 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import boto
conn=boto.connect_s3()
bucket= s3.create_bucket('boto-demp')