import importlib.util
import os

head, tail = os.path.split( __file__)
sPath = os.path.join( head, '')
print( sPath)

class myFunc:
    

    def __init__(self):
        self.dynPt = None
        self.load()

    def load( self):
        spec = importlib.util.spec_from_file_location("dynPt", sPath + "dynCode.py")
        self.dynPt = importlib.util.module_from_spec(spec)
        spec.loader.exec_module( self.dynPt)


_obj = myFunc()

def get():
    return _obj.dynPt

def lget():
    _obj.load()
    return _obj.dynPt

def load():
    _obj.load()

