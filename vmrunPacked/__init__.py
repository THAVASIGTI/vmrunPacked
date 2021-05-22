import subprocess,os,sys,logging
from vmrunPacked.util import *

class Pack:
    def __init__(self,vmxFilePath,userName=str,passWord=str,product=WS):
        self.vmx = vmxFilePath

    def start(self):
        try:
            print(f"start: {self.vmx}")
        except Exception as e:
            logging.debug(e)