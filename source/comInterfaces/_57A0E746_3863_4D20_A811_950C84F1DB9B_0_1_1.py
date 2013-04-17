# -*- coding: mbcs -*-
typelib_path = 'C:\\work\\nvda\\nvdajp_jtalk\\source\\typelibs\\FlashAccessibility.tlb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes.automation import IDispatch
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid


class Library(object):
    name = u'FlashAccessibility'
    _reg_typelib_ = ('{57A0E746-3863-4D20-A811-950C84F1DB9B}', 1, 1)

class IFlashAccessibility(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{57A0E747-3863-4D20-A811-950C84F1DB9B}')
    _idlflags_ = ['dual', 'oleautomation']
IFlashAccessibility._methods_ = [
    COMMETHOD([dispid(1001)], HRESULT, 'SuppressInessentialEvents'),
    COMMETHOD([dispid(1002)], HRESULT, 'CopyDescriptionIntoName'),
    COMMETHOD([dispid(1003)], HRESULT, 'HaltEvents'),
    COMMETHOD([dispid(1004)], HRESULT, 'ResumeEvents'),
    COMMETHOD([dispid(1005)], HRESULT, 'HaltEvents_ProcessScope'),
    COMMETHOD([dispid(1006)], HRESULT, 'ResumeEvents_ProcessScope'),
    COMMETHOD([dispid(1007)], HRESULT, 'GetFlashAX',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppFlashAxOut' )),
]
################################################################
## code template for IFlashAccessibility implementation
##class IFlashAccessibility_Impl(object):
##    def HaltEvents_ProcessScope(self):
##        '-no docstring-'
##        #return 
##
##    def SuppressInessentialEvents(self):
##        '-no docstring-'
##        #return 
##
##    def GetFlashAX(self):
##        '-no docstring-'
##        #return ppFlashAxOut
##
##    def ResumeEvents_ProcessScope(self):
##        '-no docstring-'
##        #return 
##
##    def HaltEvents(self):
##        '-no docstring-'
##        #return 
##
##    def CopyDescriptionIntoName(self):
##        '-no docstring-'
##        #return 
##
##    def ResumeEvents(self):
##        '-no docstring-'
##        #return 
##

class ISimpleTextSelection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{307F64C0-621D-4D56-BBC6-91EFC13CE40D}')
    _idlflags_ = ['dual', 'oleautomation']
ISimpleTextSelection._methods_ = [
    COMMETHOD([dispid(1101)], HRESULT, 'GetSelection',
              ( ['out'], POINTER(c_int), 'pFixedPosOut' ),
              ( ['out'], POINTER(c_int), 'pActivePosOut' )),
]
################################################################
## code template for ISimpleTextSelection implementation
##class ISimpleTextSelection_Impl(object):
##    def GetSelection(self):
##        '-no docstring-'
##        #return pFixedPosOut, pActivePosOut
##

__all__ = ['ISimpleTextSelection', 'IFlashAccessibility']
from comtypes import _check_version; _check_version('501')
