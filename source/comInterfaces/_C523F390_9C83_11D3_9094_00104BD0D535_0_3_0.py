# -*- coding: mbcs -*-
typelib_path = 'C:\\work\\nvda\\nvdajp_jtalk\\source\\typelibs\\AcrobatAccess.tlb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import BSTR
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import CoClass
from comtypes import wireHWND
from comtypes.automation import IDispatch
from comtypes.automation import VARIANT


class IPDDomNode(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'IPDDomNode Interface'
    _iid_ = GUID('{5007373A-20D7-458F-9FFB-ABC900E3A831}')
    _idlflags_ = ['dual', 'oleautomation']
class IAccessible(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{618736E0-3C3D-11CF-810C-00AA00389B71}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
IPDDomNode._methods_ = [
    COMMETHOD([dispid(1610743808)], HRESULT, 'GetParent',
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'ppdispParent' )),
    COMMETHOD([dispid(1610743809)], HRESULT, 'GetType',
              ( ['retval', 'out'], POINTER(c_int), 'pNodeType' )),
    COMMETHOD([dispid(1610743810)], HRESULT, 'GetChildCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcountChildren' )),
    COMMETHOD([dispid(1610743811)], HRESULT, 'GetChild',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'ppdispChild' )),
    COMMETHOD([dispid(1610743812)], HRESULT, 'GetName',
              ( ['retval', 'out'], POINTER(BSTR), 'pszName' )),
    COMMETHOD([dispid(1610743813)], HRESULT, 'GetValue',
              ( ['retval', 'out'], POINTER(BSTR), 'pszName' )),
    COMMETHOD([dispid(1610743814)], HRESULT, 'IsSame',
              ( ['in'], POINTER(IPDDomNode), 'node' ),
              ( ['retval', 'out'], POINTER(c_int), 'IsSame' )),
    COMMETHOD([dispid(1610743815)], HRESULT, 'GetTextContent',
              ( ['retval', 'out'], POINTER(BSTR), 'pszText' )),
    COMMETHOD([dispid(1610743816)], HRESULT, 'GetLocation',
              ( ['out'], POINTER(c_int), 'pxLeft' ),
              ( ['out'], POINTER(c_int), 'pyTop' ),
              ( ['out'], POINTER(c_int), 'pcxWidth' ),
              ( ['out'], POINTER(c_int), 'pcyHeight' )),
    COMMETHOD([dispid(1610743817)], HRESULT, 'GetFontInfo',
              ( ['out'], POINTER(c_int), 'fontStatus' ),
              ( ['out'], POINTER(BSTR), 'pszName' ),
              ( ['out'], POINTER(c_float), 'fontSize' ),
              ( ['out'], POINTER(c_int), 'fontFlags' ),
              ( ['out'], POINTER(c_float), 'red' ),
              ( ['out'], POINTER(c_float), 'green' ),
              ( ['out'], POINTER(c_float), 'blue' )),
    COMMETHOD([dispid(1610743818)], HRESULT, 'GetFromID',
              ( ['in'], BSTR, 'id' ),
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'ppDispNode' )),
    COMMETHOD([dispid(1610743819)], HRESULT, 'GetIAccessible',
              ( ['retval', 'out'], POINTER(POINTER(IAccessible)), 'ppDispIAccessible' )),
    COMMETHOD([dispid(1610743820)], HRESULT, 'ScrollTo'),
    COMMETHOD([dispid(1610743821)], HRESULT, 'GetTextInLines',
              ( ['in'], c_int, 'visibleOnly' ),
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'ppDisp' )),
]
################################################################
## code template for IPDDomNode implementation
##class IPDDomNode_Impl(object):
##    def GetFontInfo(self):
##        '-no docstring-'
##        #return fontStatus, pszName, fontSize, fontFlags, red, green, blue
##
##    def GetLocation(self):
##        '-no docstring-'
##        #return pxLeft, pyTop, pcxWidth, pcyHeight
##
##    def IsSame(self, node):
##        '-no docstring-'
##        #return IsSame
##
##    def GetParent(self):
##        '-no docstring-'
##        #return ppdispParent
##
##    def ScrollTo(self):
##        '-no docstring-'
##        #return 
##
##    def GetName(self):
##        '-no docstring-'
##        #return pszName
##
##    def GetType(self):
##        '-no docstring-'
##        #return pNodeType
##
##    def GetValue(self):
##        '-no docstring-'
##        #return pszName
##
##    def GetChild(self, index):
##        '-no docstring-'
##        #return ppdispChild
##
##    def GetIAccessible(self):
##        '-no docstring-'
##        #return ppDispIAccessible
##
##    def GetFromID(self, id):
##        '-no docstring-'
##        #return ppDispNode
##
##    def GetTextInLines(self, visibleOnly):
##        '-no docstring-'
##        #return ppDisp
##
##    def GetTextContent(self):
##        '-no docstring-'
##        #return pszText
##
##    def GetChildCount(self):
##        '-no docstring-'
##        #return pcountChildren
##

class Accessible(CoClass):
    u'Accessible Class'
    _reg_clsid_ = GUID('{C523F39F-9C83-11D3-9094-00104BD0D535}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C523F390-9C83-11D3-9094-00104BD0D535}', 3, 0)
class IOleWindow(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000114-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IAccID(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IAccID Interface'
    _iid_ = GUID('{81F9B44F-BA3A-4F5D-9B51-090C74A9B3A4}')
    _idlflags_ = ['dual', 'oleautomation']
class IGetPDDomNode(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'GetPPDom Interface'
    _iid_ = GUID('{F9F2FE81-F764-4BD0-AFA5-5DE841DDB625}')
    _idlflags_ = ['dual', 'oleautomation']
class ISelectText(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'ISelectText Interface'
    _iid_ = GUID('{B4848E37-7C66-40A6-9F66-D3A9BC8F4636}')
    _idlflags_ = ['dual', 'oleautomation']
Accessible._com_interfaces_ = [IAccessible, IOleWindow, comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT, IAccID, IGetPDDomNode, ISelectText]

class Library(object):
    u'Acrobat Access 3.0 Type Library'
    name = u'AcrobatAccessLib'
    _reg_typelib_ = ('{C523F390-9C83-11D3-9094-00104BD0D535}', 3, 0)

class IPDDomWord(IPDDomNode):
    _case_insensitive_ = True
    u'IPDDomWord Interface'
    _iid_ = GUID('{03C2AEA5-BEFA-4C84-A187-C9245AC784F6}')
    _idlflags_ = ['dual', 'oleautomation']
IPDDomWord._methods_ = [
    COMMETHOD([dispid(1610809344)], HRESULT, 'LastWordOfLine',
              ( ['retval', 'out'], POINTER(c_int), 'isLast' )),
]
################################################################
## code template for IPDDomWord implementation
##class IPDDomWord_Impl(object):
##    def LastWordOfLine(self):
##        '-no docstring-'
##        #return isLast
##


# values for enumeration '__MIDL___MIDL_itf_AcrobatAccess_0000_0009_0001'
IPDDOM_OPT_CLIPPEDLOCATION = 1
IPDDOM_OPT_RELATIVELOCATION = 2
__MIDL___MIDL_itf_AcrobatAccess_0000_0009_0001 = c_int # enum
class IPDDomGroupInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'GroupInfo Interface'
    _iid_ = GUID('{35ADDC4B-B470-45F9-B29C-B6845949A4FE}')
    _idlflags_ = ['dual', 'oleautomation']
IPDDomGroupInfo._methods_ = [
    COMMETHOD([dispid(24), helpstring(u'method GetGroupPosition')], HRESULT, 'GetGroupPosition',
              ( ['out'], POINTER(c_int), 'groupSize' ),
              ( ['out'], POINTER(c_int), 'position' )),
]
################################################################
## code template for IPDDomGroupInfo implementation
##class IPDDomGroupInfo_Impl(object):
##    def GetGroupPosition(self):
##        u'method GetGroupPosition'
##        #return groupSize, position
##

IOleWindow._methods_ = [
    COMMETHOD([], HRESULT, 'GetWindow',
              ( ['out'], POINTER(wireHWND), 'phwnd' )),
    COMMETHOD([], HRESULT, 'ContextSensitiveHelp',
              ( ['in'], c_int, 'fEnterMode' )),
]
################################################################
## code template for IOleWindow implementation
##class IOleWindow_Impl(object):
##    def GetWindow(self):
##        '-no docstring-'
##        #return phwnd
##
##    def ContextSensitiveHelp(self, fEnterMode):
##        '-no docstring-'
##        #return 
##

IAccessible._methods_ = [
    COMMETHOD([dispid(-5000), 'hidden', 'propget'], HRESULT, 'accParent',
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppdispParent' )),
    COMMETHOD([dispid(-5001), 'hidden', 'propget'], HRESULT, 'accChildCount',
              ( ['retval', 'out'], POINTER(c_int), 'pcountChildren' )),
    COMMETHOD([dispid(-5002), 'hidden', 'propget'], HRESULT, 'accChild',
              ( ['in'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(POINTER(IDispatch)), 'ppdispChild' )),
    COMMETHOD([dispid(-5003), 'hidden', 'propget'], HRESULT, 'accName',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pszName' )),
    COMMETHOD([dispid(-5004), 'hidden', 'propget'], HRESULT, 'accValue',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pszValue' )),
    COMMETHOD([dispid(-5005), 'hidden', 'propget'], HRESULT, 'accDescription',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pszDescription' )),
    COMMETHOD([dispid(-5006), 'hidden', 'propget'], HRESULT, 'accRole',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarRole' )),
    COMMETHOD([dispid(-5007), 'hidden', 'propget'], HRESULT, 'accState',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarState' )),
    COMMETHOD([dispid(-5008), 'hidden', 'propget'], HRESULT, 'accHelp',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pszHelp' )),
    COMMETHOD([dispid(-5009), 'hidden', 'propget'], HRESULT, 'accHelpTopic',
              ( ['out'], POINTER(BSTR), 'pszHelpFile' ),
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(c_int), 'pidTopic' )),
    COMMETHOD([dispid(-5010), 'hidden', 'propget'], HRESULT, 'accKeyboardShortcut',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pszKeyboardShortcut' )),
    COMMETHOD([dispid(-5011), 'hidden', 'propget'], HRESULT, 'accFocus',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarChild' )),
    COMMETHOD([dispid(-5012), 'hidden', 'propget'], HRESULT, 'accSelection',
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarChildren' )),
    COMMETHOD([dispid(-5013), 'hidden', 'propget'], HRESULT, 'accDefaultAction',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pszDefaultAction' )),
    COMMETHOD([dispid(-5014), 'hidden'], HRESULT, 'accSelect',
              ( ['in'], c_int, 'flagsSelect' ),
              ( ['in', 'optional'], VARIANT, 'varChild' )),
    COMMETHOD([dispid(-5015), 'hidden'], HRESULT, 'accLocation',
              ( ['out'], POINTER(c_int), 'pxLeft' ),
              ( ['out'], POINTER(c_int), 'pyTop' ),
              ( ['out'], POINTER(c_int), 'pcxWidth' ),
              ( ['out'], POINTER(c_int), 'pcyHeight' ),
              ( ['in', 'optional'], VARIANT, 'varChild' )),
    COMMETHOD([dispid(-5016), 'hidden'], HRESULT, 'accNavigate',
              ( ['in'], c_int, 'navDir' ),
              ( ['in', 'optional'], VARIANT, 'varStart' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarEndUpAt' )),
    COMMETHOD([dispid(-5017), 'hidden'], HRESULT, 'accHitTest',
              ( ['in'], c_int, 'xLeft' ),
              ( ['in'], c_int, 'yTop' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'pvarChild' )),
    COMMETHOD([dispid(-5018), 'hidden'], HRESULT, 'accDoDefaultAction',
              ( ['in', 'optional'], VARIANT, 'varChild' )),
    COMMETHOD([dispid(-5003), 'hidden', 'propput'], HRESULT, 'accName',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['in'], BSTR, 'pszName' )),
    COMMETHOD([dispid(-5004), 'hidden', 'propput'], HRESULT, 'accValue',
              ( ['in', 'optional'], VARIANT, 'varChild' ),
              ( ['in'], BSTR, 'pszValue' )),
]
################################################################
## code template for IAccessible implementation
##class IAccessible_Impl(object):
##    @property
##    def accRole(self, varChild):
##        '-no docstring-'
##        #return pvarRole
##
##    @property
##    def accDescription(self, varChild):
##        '-no docstring-'
##        #return pszDescription
##
##    def accLocation(self, varChild):
##        '-no docstring-'
##        #return pxLeft, pyTop, pcxWidth, pcyHeight
##
##    @property
##    def accState(self, varChild):
##        '-no docstring-'
##        #return pvarState
##
##    def accNavigate(self, navDir, varStart):
##        '-no docstring-'
##        #return pvarEndUpAt
##
##    def accDoDefaultAction(self, varChild):
##        '-no docstring-'
##        #return 
##
##    @property
##    def accChild(self, varChild):
##        '-no docstring-'
##        #return ppdispChild
##
##    @property
##    def accChildCount(self):
##        '-no docstring-'
##        #return pcountChildren
##
##    @property
##    def accHelp(self, varChild):
##        '-no docstring-'
##        #return pszHelp
##
##    def _get(self, varChild):
##        '-no docstring-'
##        #return pszName
##    def _set(self, varChild, pszName):
##        '-no docstring-'
##    accName = property(_get, _set, doc = _set.__doc__)
##
##    def accSelect(self, flagsSelect, varChild):
##        '-no docstring-'
##        #return 
##
##    @property
##    def accKeyboardShortcut(self, varChild):
##        '-no docstring-'
##        #return pszKeyboardShortcut
##
##    def accHitTest(self, xLeft, yTop):
##        '-no docstring-'
##        #return pvarChild
##
##    @property
##    def accSelection(self):
##        '-no docstring-'
##        #return pvarChildren
##
##    @property
##    def accDefaultAction(self, varChild):
##        '-no docstring-'
##        #return pszDefaultAction
##
##    @property
##    def accParent(self):
##        '-no docstring-'
##        #return ppdispParent
##
##    @property
##    def accHelpTopic(self, varChild):
##        '-no docstring-'
##        #return pszHelpFile, pidTopic
##
##    def _get(self, varChild):
##        '-no docstring-'
##        #return pszValue
##    def _set(self, varChild, pszValue):
##        '-no docstring-'
##    accValue = property(_get, _set, doc = _set.__doc__)
##
##    @property
##    def accFocus(self):
##        '-no docstring-'
##        #return pvarChild
##

IAccID._methods_ = [
    COMMETHOD([dispid(22), helpstring(u'method get_accID')], HRESULT, 'get_accID',
              ( ['retval', 'out'], POINTER(c_int), 'pID' )),
]
################################################################
## code template for IAccID implementation
##class IAccID_Impl(object):
##    def get_accID(self):
##        u'method get_accID'
##        #return pID
##

class IPDDomNodeExt(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPDDomNodeExt Interface'
    _iid_ = GUID('{4A894040-247E-4AFF-BB08-3489E9905235}')
    _idlflags_ = ['dual', 'oleautomation']
IPDDomNodeExt._methods_ = [
    COMMETHOD([dispid(1610678272)], HRESULT, 'GetState',
              ( ['retval', 'out'], POINTER(c_int), 'pState' )),
    COMMETHOD([dispid(1610678273)], HRESULT, 'Navigate',
              ( ['in'], c_int, 'navDir' ),
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'ppEnd' )),
    COMMETHOD([dispid(1610678274)], HRESULT, 'SetFocus'),
    COMMETHOD([dispid(1610678275)], HRESULT, 'GetIndex',
              ( ['retval', 'out'], POINTER(c_int), 'pIndex' )),
    COMMETHOD([dispid(1610678276)], HRESULT, 'GetPageNum',
              ( ['out'], POINTER(c_int), 'firstPage' ),
              ( ['out'], POINTER(c_int), 'lastPage' )),
    COMMETHOD([dispid(1610678277)], HRESULT, 'DoDefaultAction'),
    COMMETHOD([dispid(1610678278)], HRESULT, 'ScrollToEx',
              ( [], c_int, 'favorLeft' ),
              ( [], c_int, 'favorTop' )),
    COMMETHOD([dispid(1610678279)], HRESULT, 'Relationship',
              ( ['in'], POINTER(IPDDomNode), 'node' ),
              ( ['out'], POINTER(c_int), 'pRel' )),
]
################################################################
## code template for IPDDomNodeExt implementation
##class IPDDomNodeExt_Impl(object):
##    def SetFocus(self):
##        '-no docstring-'
##        #return 
##
##    def GetIndex(self):
##        '-no docstring-'
##        #return pIndex
##
##    def GetState(self):
##        '-no docstring-'
##        #return pState
##
##    def Relationship(self, node):
##        '-no docstring-'
##        #return pRel
##
##    def DoDefaultAction(self):
##        '-no docstring-'
##        #return 
##
##    def Navigate(self, navDir):
##        '-no docstring-'
##        #return ppEnd
##
##    def GetPageNum(self):
##        '-no docstring-'
##        #return firstPage, lastPage
##
##    def ScrollToEx(self, favorLeft, favorTop):
##        '-no docstring-'
##        #return 
##

class IPDDomGlobalOptions(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IPDDom Global Options Interface'
    _iid_ = GUID('{C37B1794-B61E-402B-9C7C-B073DE579AC1}')
    _idlflags_ = ['dual', 'oleautomation']
IPDDomOptIds = __MIDL___MIDL_itf_AcrobatAccess_0000_0009_0001
IPDDomGlobalOptions._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'method GetOption')], HRESULT, 'GetOption',
              ( ['in'], IPDDomOptIds, 'optId' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'value' )),
    COMMETHOD([dispid(2), helpstring(u'method SetOption')], HRESULT, 'SetOption',
              ( ['in'], IPDDomOptIds, 'optId' ),
              ( ['in'], VARIANT, 'value' )),
]
################################################################
## code template for IPDDomGlobalOptions implementation
##class IPDDomGlobalOptions_Impl(object):
##    def SetOption(self, optId, value):
##        u'method SetOption'
##        #return 
##
##    def GetOption(self, optId):
##        u'method GetOption'
##        #return value
##

class IPDDomElement(IPDDomNode):
    _case_insensitive_ = True
    u'IPDDomElement Interface'
    _iid_ = GUID('{198F17AE-B921-4308-9543-288D426A5C2B}')
    _idlflags_ = ['dual', 'oleautomation']
class IPDDomDocument(IPDDomElement):
    _case_insensitive_ = True
    u'IPDDomDocument Interface'
    _iid_ = GUID('{00FFD6C4-1A94-44BC-AD3E-8AC18552E3E6}')
    _idlflags_ = ['dual', 'oleautomation']
IPDDomElement._methods_ = [
    COMMETHOD([dispid(1610809344)], HRESULT, 'GetTagName',
              ( ['retval', 'out'], POINTER(BSTR), 'pszTagName' )),
    COMMETHOD([dispid(1610809345)], HRESULT, 'GetStdName',
              ( ['retval', 'out'], POINTER(BSTR), 'pszStdName' )),
    COMMETHOD([dispid(1610809346)], HRESULT, 'GetID',
              ( ['retval', 'out'], POINTER(BSTR), 'pszId' )),
    COMMETHOD([dispid(1610809347)], HRESULT, 'GetAttribute',
              ( ['in'], BSTR, 'pszAttr' ),
              ( ['in'], BSTR, 'pszOwner' ),
              ( ['retval', 'out'], POINTER(BSTR), 'pszAttrVal' )),
]
################################################################
## code template for IPDDomElement implementation
##class IPDDomElement_Impl(object):
##    def GetStdName(self):
##        '-no docstring-'
##        #return pszStdName
##
##    def GetAttribute(self, pszAttr, pszOwner):
##        '-no docstring-'
##        #return pszAttrVal
##
##    def GetID(self):
##        '-no docstring-'
##        #return pszId
##
##    def GetTagName(self):
##        '-no docstring-'
##        #return pszTagName
##

IPDDomDocument._methods_ = [
    COMMETHOD([dispid(1610874880)], HRESULT, 'GetFocusNode',
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'node' )),
    COMMETHOD([dispid(1610874881)], HRESULT, 'NextFocusNode',
              ( ['in'], c_int, 'forward' ),
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'node' )),
    COMMETHOD([dispid(1610874882)], HRESULT, 'GetDocInfo',
              ( ['out'], POINTER(BSTR), 'fileName' ),
              ( ['out'], POINTER(c_int), 'nPages' ),
              ( ['out'], POINTER(c_int), 'firstVisiblePage' ),
              ( ['out'], POINTER(c_int), 'lastVisiblePage' ),
              ( ['out'], POINTER(c_int), 'status' ),
              ( ['out'], POINTER(BSTR), 'lang' )),
    COMMETHOD([dispid(1610874883)], HRESULT, 'selectText',
              ( ['in'], POINTER(IPDDomWord), 'startID' ),
              ( ['in'], c_int, 'startCharIndex' ),
              ( ['in'], POINTER(IPDDomWord), 'stopID' ),
              ( ['in'], c_int, 'stopCharIndex' )),
    COMMETHOD([dispid(1610874884)], HRESULT, 'GetTextSelection',
              ( ['out'], POINTER(BSTR), 'pSelection' )),
    COMMETHOD([dispid(1610874885)], HRESULT, 'GetSelectionBounds',
              ( ['out'], POINTER(POINTER(IPDDomWord)), 'pStart' ),
              ( ['out'], POINTER(c_int), 'startIndex' ),
              ( ['out'], POINTER(POINTER(IPDDomWord)), 'pStop' ),
              ( [], POINTER(c_int), 'stopIndex' )),
    COMMETHOD([dispid(1610874886)], HRESULT, 'GetCaret',
              ( ['out'], POINTER(c_int), 'pxLeft' ),
              ( ['out'], POINTER(c_int), 'pyTop' ),
              ( ['out'], POINTER(c_int), 'pcxWidth' ),
              ( ['out'], POINTER(c_int), 'pcyHeight' ),
              ( ['out'], POINTER(POINTER(IPDDomNode)), 'node' ),
              ( ['out'], POINTER(c_int), 'index' )),
    COMMETHOD([dispid(1610874887)], HRESULT, 'SetCaret',
              ( ['in'], POINTER(IPDDomWord), 'node' ),
              ( ['in'], c_int, 'index' )),
    COMMETHOD([dispid(1610874888)], HRESULT, 'GoToPage',
              ( ['in'], c_int, 'pageNum' )),
]
################################################################
## code template for IPDDomDocument implementation
##class IPDDomDocument_Impl(object):
##    def GoToPage(self, pageNum):
##        '-no docstring-'
##        #return 
##
##    def NextFocusNode(self, forward):
##        '-no docstring-'
##        #return node
##
##    def GetCaret(self):
##        '-no docstring-'
##        #return pxLeft, pyTop, pcxWidth, pcyHeight, node, index
##
##    def SetCaret(self, node, index):
##        '-no docstring-'
##        #return 
##
##    def GetSelectionBounds(self, stopIndex):
##        '-no docstring-'
##        #return pStart, startIndex, pStop
##
##    def GetDocInfo(self):
##        '-no docstring-'
##        #return fileName, nPages, firstVisiblePage, lastVisiblePage, status, lang
##
##    def GetTextSelection(self):
##        '-no docstring-'
##        #return pSelection
##
##    def GetFocusNode(self):
##        '-no docstring-'
##        #return node
##
##    def selectText(self, startID, startCharIndex, stopID, stopCharIndex):
##        '-no docstring-'
##        #return 
##

class __MIDL_IWinTypes_0009(Union):
    pass
__MIDL_IWinTypes_0009._fields_ = [
    ('hInproc', c_int),
    ('hRemote', c_int),
]
assert sizeof(__MIDL_IWinTypes_0009) == 4, sizeof(__MIDL_IWinTypes_0009)
assert alignment(__MIDL_IWinTypes_0009) == 4, alignment(__MIDL_IWinTypes_0009)
class PDDom(CoClass):
    u'PDDom Class'
    _reg_clsid_ = GUID('{ECAF4D9D-B473-4EC5-86F4-3DBB46F3F31A}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{C523F390-9C83-11D3-9094-00104BD0D535}', 3, 0)
PDDom._com_interfaces_ = [IPDDomNode, comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IEnumVARIANT, IPDDomElement, IPDDomWord, IPDDomNodeExt, IPDDomDocument, IPDDomGroupInfo, IPDDomGlobalOptions]

IGetPDDomNode._methods_ = [
    COMMETHOD([dispid(24), helpstring(u'method get_PDDomNode')], HRESULT, 'get_PDDomNode',
              ( ['in'], VARIANT, 'varID' ),
              ( ['retval', 'out'], POINTER(POINTER(IPDDomNode)), 'ppDispDoc' )),
]
################################################################
## code template for IGetPDDomNode implementation
##class IGetPDDomNode_Impl(object):
##    def get_PDDomNode(self, varID):
##        u'method get_PDDomNode'
##        #return ppDispDoc
##

class _RemotableHandle(Structure):
    pass
_RemotableHandle._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0009),
]
assert sizeof(_RemotableHandle) == 8, sizeof(_RemotableHandle)
assert alignment(_RemotableHandle) == 4, alignment(_RemotableHandle)
ISelectText._methods_ = [
    COMMETHOD([dispid(23), helpstring(u'method selectText')], HRESULT, 'selectText',
              ( ['in'], c_int, 'startID' ),
              ( ['in'], c_int, 'startCharIndex' ),
              ( ['in'], c_int, 'stopID' ),
              ( ['in'], c_int, 'stopCharIndex' )),
]
################################################################
## code template for ISelectText implementation
##class ISelectText_Impl(object):
##    def selectText(self, startID, startCharIndex, stopID, stopCharIndex):
##        u'method selectText'
##        #return 
##

__all__ = ['Accessible', 'IPDDomElement', 'ISelectText',
           'IPDDOM_OPT_RELATIVELOCATION', 'IAccessible',
           'IPDDomNodeExt', '_RemotableHandle',
           '__MIDL___MIDL_itf_AcrobatAccess_0000_0009_0001',
           'IPDDomGroupInfo', '__MIDL_IWinTypes_0009', 'IAccID',
           'IPDDomDocument', 'IPDDomGlobalOptions', 'IPDDomNode',
           'IPDDomOptIds', 'IGetPDDomNode', 'IOleWindow', 'PDDom',
           'IPDDOM_OPT_CLIPPEDLOCATION', 'IPDDomWord']
from comtypes import _check_version; _check_version('501')
