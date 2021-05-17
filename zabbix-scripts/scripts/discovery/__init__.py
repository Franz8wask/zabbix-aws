from discovery import ec2
from discovery import elb
from discovery import elbv2
from discovery import emr
from discovery import rds
from discovery import s3
from discovery import basic_discovery

import os
__all__ = [file for file in os.listdir(os.getcwd()) if file.endswith(".py")]
