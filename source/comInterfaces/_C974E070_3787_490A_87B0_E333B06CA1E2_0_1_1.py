# -*- coding: mbcs -*-
typelib_path = 'C:\\work\\nvda\\nvdajp_jtalk\\source\\typelibs\\ia2.tlb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import BSTR
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes.automation import VARIANT
STRING = c_char_p
from comtypes.automation import VARIANT
from comtypes.automation import IDispatch
from comtypes import wireHWND
from comtypes import IUnknown


class IAccessibleAction(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B70D9F59-3B5A-4DBA-AB9E-22012F607DF5}')
    _idlflags_ = []
class IAccessibleHyperlink(IAccessibleAction):
    _case_insensitive_ = True
    _iid_ = GUID('{01C20F2B-3DD2-400F-949F-AD00BDAB1D41}')
    _idlflags_ = []
IAccessibleAction._methods_ = [
    COMMETHOD([], HRESULT, 'nActions',
              ( ['retval', 'out'], POINTER(c_int), 'nActions' )),
    COMMETHOD([], HRESULT, 'doAction',
              ( ['in'], c_int, 'actionIndex' )),
    COMMETHOD(['propget'], HRESULT, 'description',
              ( ['in'], c_int, 'actionIndex' ),
              ( ['retval', 'out'], POINTER(BSTR), 'description' )),
    COMMETHOD(['propget'], HRESULT, 'keyBinding',
              ( ['in'], c_int, 'actionIndex' ),
              ( ['in'], c_int, 'nMaxBindings' ),
              ( ['out'], POINTER(POINTER(BSTR)), 'keyBindings' ),
              ( ['retval', 'out'], POINTER(c_int), 'nBindings' )),
    COMMETHOD(['propget'], HRESULT, 'name',
              ( ['in'], c_int, 'actionIndex' ),
              ( ['retval', 'out'], POINTER(BSTR), 'name' )),
    COMMETHOD(['propget'], HRESULT, 'localizedName',
              ( ['in'], c_int, 'actionIndex' ),
              ( ['retval', 'out'], POINTER(BSTR), 'localizedName' )),
]
################################################################
## code template for IAccessibleAction implementation
##class IAccessibleAction_Impl(object):
##    @property
##    def description(self, actionIndex):
##        '-no docstring-'
##        #return description
##
##    @property
##    def keyBinding(self, actionIndex, nMaxBindings):
##        '-no docstring-'
##        #return keyBindings, nBindings
##
##    @property
##    def localizedName(self, actionIndex):
##        '-no docstring-'
##        #return localizedName
##
##    def doAction(self, actionIndex):
##        '-no docstring-'
##        #return 
##
##    def nActions(self):
##        '-no docstring-'
##        #return nActions
##
##    @property
##    def name(self, actionIndex):
##        '-no docstring-'
##        #return name
##

IAccessibleHyperlink._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'anchor',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'anchor' )),
    COMMETHOD(['propget'], HRESULT, 'anchorTarget',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'anchorTarget' )),
    COMMETHOD(['propget'], HRESULT, 'startIndex',
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD(['propget'], HRESULT, 'endIndex',
              ( ['retval', 'out'], POINTER(c_int), 'index' )),
    COMMETHOD(['propget'], HRESULT, 'valid',
              ( ['retval', 'out'], STRING, 'valid' )),
]
################################################################
## code template for IAccessibleHyperlink implementation
##class IAccessibleHyperlink_Impl(object):
##    @property
##    def anchorTarget(self, index):
##        '-no docstring-'
##        #return anchorTarget
##
##    @property
##    def endIndex(self):
##        '-no docstring-'
##        #return index
##
##    @property
##    def startIndex(self):
##        '-no docstring-'
##        #return index
##
##    @property
##    def valid(self):
##        '-no docstring-'
##        #return valid
##
##    @property
##    def anchor(self, index):
##        '-no docstring-'
##        #return anchor
##


# values for enumeration 'IA2TextBoundaryType'
IA2_TEXT_BOUNDARY_CHAR = 0
IA2_TEXT_BOUNDARY_WORD = 1
IA2_TEXT_BOUNDARY_SENTENCE = 2
IA2_TEXT_BOUNDARY_PARAGRAPH = 3
IA2_TEXT_BOUNDARY_LINE = 4
IA2_TEXT_BOUNDARY_ALL = 5
IA2TextBoundaryType = c_int # enum
class Library(object):
    u'IAccessible2 Type Library'
    name = u'IAccessible2Lib'
    _reg_typelib_ = ('{C974E070-3787-490A-87B0-E333B06CA1E2}', 1, 1)

class IAccessibleValue(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{35855B5B-C566-4FD0-A7B1-E65465600394}')
    _idlflags_ = []
IAccessibleValue._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'currentValue',
              ( ['retval', 'out'], POINTER(VARIANT), 'currentValue' )),
    COMMETHOD([], HRESULT, 'setCurrentValue',
              ( ['in'], VARIANT, 'value' )),
    COMMETHOD(['propget'], HRESULT, 'maximumValue',
              ( ['retval', 'out'], POINTER(VARIANT), 'maximumValue' )),
    COMMETHOD(['propget'], HRESULT, 'minimumValue',
              ( ['retval', 'out'], POINTER(VARIANT), 'minimumValue' )),
]
################################################################
## code template for IAccessibleValue implementation
##class IAccessibleValue_Impl(object):
##    def setCurrentValue(self, value):
##        '-no docstring-'
##        #return 
##
##    @property
##    def currentValue(self):
##        '-no docstring-'
##        #return currentValue
##
##    @property
##    def minimumValue(self):
##        '-no docstring-'
##        #return minimumValue
##
##    @property
##    def maximumValue(self):
##        '-no docstring-'
##        #return maximumValue
##

class IAccessible(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    _iid_ = GUID('{618736E0-3C3D-11CF-810C-00AA00389B71}')
    _idlflags_ = ['dual', 'oleautomation', 'hidden']
class IAccessible2(IAccessible):
    _case_insensitive_ = True
    _iid_ = GUID('{E89F726E-C4F4-4C19-BB19-B647D7FA8478}')
    _idlflags_ = []
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

class IAccessibleRelation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7CDF86EE-C3DA-496A-BDA4-281B336E1FDC}')
    _idlflags_ = []

# values for enumeration 'IA2ScrollType'
IA2_SCROLL_TYPE_TOP_LEFT = 0
IA2_SCROLL_TYPE_BOTTOM_RIGHT = 1
IA2_SCROLL_TYPE_TOP_EDGE = 2
IA2_SCROLL_TYPE_BOTTOM_EDGE = 3
IA2_SCROLL_TYPE_LEFT_EDGE = 4
IA2_SCROLL_TYPE_RIGHT_EDGE = 5
IA2_SCROLL_TYPE_ANYWHERE = 6
IA2ScrollType = c_int # enum

# values for enumeration 'IA2CoordinateType'
IA2_COORDTYPE_SCREEN_RELATIVE = 0
IA2_COORDTYPE_PARENT_RELATIVE = 1
IA2CoordinateType = c_int # enum
class IA2Locale(Structure):
    pass
IAccessible2._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'nRelations',
              ( ['retval', 'out'], POINTER(c_int), 'nRelations' )),
    COMMETHOD(['propget'], HRESULT, 'relation',
              ( ['in'], c_int, 'relationIndex' ),
              ( ['retval', 'out'], POINTER(POINTER(IAccessibleRelation)), 'relation' )),
    COMMETHOD(['propget'], HRESULT, 'relations',
              ( ['in'], c_int, 'maxRelations' ),
              ( ['out'], POINTER(POINTER(IAccessibleRelation)), 'relations' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRelations' )),
    COMMETHOD([], HRESULT, 'role',
              ( ['retval', 'out'], POINTER(c_int), 'role' )),
    COMMETHOD([], HRESULT, 'scrollTo',
              ( ['in'], IA2ScrollType, 'scrollType' )),
    COMMETHOD([], HRESULT, 'scrollToPoint',
              ( ['in'], IA2CoordinateType, 'coordinateType' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD(['propget'], HRESULT, 'groupPosition',
              ( ['out'], POINTER(c_int), 'groupLevel' ),
              ( ['out'], POINTER(c_int), 'similarItemsInGroup' ),
              ( ['retval', 'out'], POINTER(c_int), 'positionInGroup' )),
    COMMETHOD(['propget'], HRESULT, 'states',
              ( ['retval', 'out'], POINTER(c_int), 'states' )),
    COMMETHOD(['propget'], HRESULT, 'extendedRole',
              ( ['retval', 'out'], POINTER(BSTR), 'extendedRole' )),
    COMMETHOD(['propget'], HRESULT, 'localizedExtendedRole',
              ( ['retval', 'out'], POINTER(BSTR), 'localizedExtendedRole' )),
    COMMETHOD(['propget'], HRESULT, 'nExtendedStates',
              ( ['retval', 'out'], POINTER(c_int), 'nExtendedStates' )),
    COMMETHOD(['propget'], HRESULT, 'extendedStates',
              ( ['in'], c_int, 'maxExtendedStates' ),
              ( ['out'], POINTER(POINTER(BSTR)), 'extendedStates' ),
              ( ['retval', 'out'], POINTER(c_int), 'nExtendedStates' )),
    COMMETHOD(['propget'], HRESULT, 'localizedExtendedStates',
              ( ['in'], c_int, 'maxLocalizedExtendedStates' ),
              ( ['out'], POINTER(POINTER(BSTR)), 'localizedExtendedStates' ),
              ( ['retval', 'out'], POINTER(c_int), 'nLocalizedExtendedStates' )),
    COMMETHOD(['propget'], HRESULT, 'uniqueID',
              ( ['retval', 'out'], POINTER(c_int), 'uniqueID' )),
    COMMETHOD(['propget'], HRESULT, 'windowHandle',
              ( ['retval', 'out'], POINTER(wireHWND), 'windowHandle' )),
    COMMETHOD(['propget'], HRESULT, 'indexInParent',
              ( ['retval', 'out'], POINTER(c_int), 'indexInParent' )),
    COMMETHOD(['propget'], HRESULT, 'locale',
              ( ['retval', 'out'], POINTER(IA2Locale), 'locale' )),
    COMMETHOD(['propget'], HRESULT, 'attributes',
              ( ['retval', 'out'], POINTER(BSTR), 'attributes' )),
]
################################################################
## code template for IAccessible2 implementation
##class IAccessible2_Impl(object):
##    @property
##    def nRelations(self):
##        '-no docstring-'
##        #return nRelations
##
##    def scrollTo(self, scrollType):
##        '-no docstring-'
##        #return 
##
##    @property
##    def locale(self):
##        '-no docstring-'
##        #return locale
##
##    @property
##    def windowHandle(self):
##        '-no docstring-'
##        #return windowHandle
##
##    @property
##    def groupPosition(self):
##        '-no docstring-'
##        #return groupLevel, similarItemsInGroup, positionInGroup
##
##    @property
##    def relations(self, maxRelations):
##        '-no docstring-'
##        #return relations, nRelations
##
##    def scrollToPoint(self, coordinateType, x, y):
##        '-no docstring-'
##        #return 
##
##    @property
##    def states(self):
##        '-no docstring-'
##        #return states
##
##    @property
##    def localizedExtendedStates(self, maxLocalizedExtendedStates):
##        '-no docstring-'
##        #return localizedExtendedStates, nLocalizedExtendedStates
##
##    @property
##    def extendedRole(self):
##        '-no docstring-'
##        #return extendedRole
##
##    def role(self):
##        '-no docstring-'
##        #return role
##
##    @property
##    def localizedExtendedRole(self):
##        '-no docstring-'
##        #return localizedExtendedRole
##
##    @property
##    def uniqueID(self):
##        '-no docstring-'
##        #return uniqueID
##
##    @property
##    def attributes(self):
##        '-no docstring-'
##        #return attributes
##
##    @property
##    def relation(self, relationIndex):
##        '-no docstring-'
##        #return relation
##
##    @property
##    def nExtendedStates(self):
##        '-no docstring-'
##        #return nExtendedStates
##
##    @property
##    def extendedStates(self, maxExtendedStates):
##        '-no docstring-'
##        #return extendedStates, nExtendedStates
##
##    @property
##    def indexInParent(self):
##        '-no docstring-'
##        #return indexInParent
##

class IAccessibleEditableText(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A59AA09A-7011-4B65-939D-32B1FB5547E3}')
    _idlflags_ = []
IAccessibleEditableText._methods_ = [
    COMMETHOD([], HRESULT, 'copyText',
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' )),
    COMMETHOD([], HRESULT, 'deleteText',
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' )),
    COMMETHOD([], HRESULT, 'insertText',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], POINTER(BSTR), 'text' )),
    COMMETHOD([], HRESULT, 'cutText',
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' )),
    COMMETHOD([], HRESULT, 'pasteText',
              ( ['in'], c_int, 'offset' )),
    COMMETHOD([], HRESULT, 'replaceText',
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' ),
              ( ['in'], POINTER(BSTR), 'text' )),
    COMMETHOD([], HRESULT, 'setAttributes',
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' ),
              ( ['in'], POINTER(BSTR), 'attributes' )),
]
################################################################
## code template for IAccessibleEditableText implementation
##class IAccessibleEditableText_Impl(object):
##    def insertText(self, offset, text):
##        '-no docstring-'
##        #return 
##
##    def cutText(self, startOffset, endOffset):
##        '-no docstring-'
##        #return 
##
##    def pasteText(self, offset):
##        '-no docstring-'
##        #return 
##
##    def replaceText(self, startOffset, endOffset, text):
##        '-no docstring-'
##        #return 
##
##    def deleteText(self, startOffset, endOffset):
##        '-no docstring-'
##        #return 
##
##    def copyText(self, startOffset, endOffset):
##        '-no docstring-'
##        #return 
##
##    def setAttributes(self, startOffset, endOffset, attributes):
##        '-no docstring-'
##        #return 
##

class IAccessibleText(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{24FD2FFB-3AAD-4A08-8335-A3AD89C0FB4B}')
    _idlflags_ = []
class IA2TextSegment(Structure):
    pass
IAccessibleText._methods_ = [
    COMMETHOD([], HRESULT, 'addSelection',
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' )),
    COMMETHOD(['propget'], HRESULT, 'attributes',
              ( ['in'], c_int, 'offset' ),
              ( ['out'], POINTER(c_int), 'startOffset' ),
              ( ['out'], POINTER(c_int), 'endOffset' ),
              ( ['retval', 'out'], POINTER(BSTR), 'textAttributes' )),
    COMMETHOD(['propget'], HRESULT, 'caretOffset',
              ( ['retval', 'out'], POINTER(c_int), 'offset' )),
    COMMETHOD(['propget'], HRESULT, 'characterExtents',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], IA2CoordinateType, 'coordType' ),
              ( ['out'], POINTER(c_int), 'x' ),
              ( ['out'], POINTER(c_int), 'y' ),
              ( ['out'], POINTER(c_int), 'width' ),
              ( ['retval', 'out'], POINTER(c_int), 'height' )),
    COMMETHOD(['propget'], HRESULT, 'nSelections',
              ( ['retval', 'out'], POINTER(c_int), 'nSelections' )),
    COMMETHOD(['propget'], HRESULT, 'offsetAtPoint',
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' ),
              ( ['in'], IA2CoordinateType, 'coordType' ),
              ( ['retval', 'out'], POINTER(c_int), 'offset' )),
    COMMETHOD(['propget'], HRESULT, 'selection',
              ( ['in'], c_int, 'selectionIndex' ),
              ( ['out'], POINTER(c_int), 'startOffset' ),
              ( ['retval', 'out'], POINTER(c_int), 'endOffset' )),
    COMMETHOD(['propget'], HRESULT, 'text',
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' ),
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD(['propget'], HRESULT, 'textBeforeOffset',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], IA2TextBoundaryType, 'boundaryType' ),
              ( ['out'], POINTER(c_int), 'startOffset' ),
              ( ['out'], POINTER(c_int), 'endOffset' ),
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD(['propget'], HRESULT, 'textAfterOffset',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], IA2TextBoundaryType, 'boundaryType' ),
              ( ['out'], POINTER(c_int), 'startOffset' ),
              ( ['out'], POINTER(c_int), 'endOffset' ),
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD(['propget'], HRESULT, 'textAtOffset',
              ( ['in'], c_int, 'offset' ),
              ( ['in'], IA2TextBoundaryType, 'boundaryType' ),
              ( ['out'], POINTER(c_int), 'startOffset' ),
              ( ['out'], POINTER(c_int), 'endOffset' ),
              ( ['retval', 'out'], POINTER(BSTR), 'text' )),
    COMMETHOD([], HRESULT, 'removeSelection',
              ( ['in'], c_int, 'selectionIndex' )),
    COMMETHOD([], HRESULT, 'setCaretOffset',
              ( ['in'], c_int, 'offset' )),
    COMMETHOD([], HRESULT, 'setSelection',
              ( ['in'], c_int, 'selectionIndex' ),
              ( ['in'], c_int, 'startOffset' ),
              ( ['in'], c_int, 'endOffset' )),
    COMMETHOD(['propget'], HRESULT, 'nCharacters',
              ( ['retval', 'out'], POINTER(c_int), 'nCharacters' )),
    COMMETHOD([], HRESULT, 'scrollSubstringTo',
              ( ['in'], c_int, 'startIndex' ),
              ( ['in'], c_int, 'endIndex' ),
              ( ['in'], IA2ScrollType, 'scrollType' )),
    COMMETHOD([], HRESULT, 'scrollSubstringToPoint',
              ( ['in'], c_int, 'startIndex' ),
              ( ['in'], c_int, 'endIndex' ),
              ( ['in'], IA2CoordinateType, 'coordinateType' ),
              ( ['in'], c_int, 'x' ),
              ( ['in'], c_int, 'y' )),
    COMMETHOD(['propget'], HRESULT, 'newText',
              ( ['retval', 'out'], POINTER(IA2TextSegment), 'newText' )),
    COMMETHOD(['propget'], HRESULT, 'oldText',
              ( ['retval', 'out'], POINTER(IA2TextSegment), 'oldText' )),
]
################################################################
## code template for IAccessibleText implementation
##class IAccessibleText_Impl(object):
##    def setCaretOffset(self, offset):
##        '-no docstring-'
##        #return 
##
##    @property
##    def selection(self, selectionIndex):
##        '-no docstring-'
##        #return startOffset, endOffset
##
##    @property
##    def nSelections(self):
##        '-no docstring-'
##        #return nSelections
##
##    def setSelection(self, selectionIndex, startOffset, endOffset):
##        '-no docstring-'
##        #return 
##
##    @property
##    def textBeforeOffset(self, offset, boundaryType):
##        '-no docstring-'
##        #return startOffset, endOffset, text
##
##    @property
##    def caretOffset(self):
##        '-no docstring-'
##        #return offset
##
##    @property
##    def text(self, startOffset, endOffset):
##        '-no docstring-'
##        #return text
##
##    def removeSelection(self, selectionIndex):
##        '-no docstring-'
##        #return 
##
##    @property
##    def oldText(self):
##        '-no docstring-'
##        #return oldText
##
##    def addSelection(self, startOffset, endOffset):
##        '-no docstring-'
##        #return 
##
##    @property
##    def textAfterOffset(self, offset, boundaryType):
##        '-no docstring-'
##        #return startOffset, endOffset, text
##
##    @property
##    def offsetAtPoint(self, x, y, coordType):
##        '-no docstring-'
##        #return offset
##
##    def scrollSubstringTo(self, startIndex, endIndex, scrollType):
##        '-no docstring-'
##        #return 
##
##    @property
##    def newText(self):
##        '-no docstring-'
##        #return newText
##
##    @property
##    def attributes(self, offset):
##        '-no docstring-'
##        #return startOffset, endOffset, textAttributes
##
##    @property
##    def textAtOffset(self, offset, boundaryType):
##        '-no docstring-'
##        #return startOffset, endOffset, text
##
##    @property
##    def characterExtents(self, offset, coordType):
##        '-no docstring-'
##        #return x, y, width, height
##
##    def scrollSubstringToPoint(self, startIndex, endIndex, coordinateType, x, y):
##        '-no docstring-'
##        #return 
##
##    @property
##    def nCharacters(self):
##        '-no docstring-'
##        #return nCharacters
##

class IAccessibleTable2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6167F295-06F0-4CDD-A1FA-02E25153D869}')
    _idlflags_ = []
class IA2TableModelChange(Structure):
    pass
IAccessibleTable2._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'cellAt',
              ( ['in'], c_int, 'row' ),
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'cell' )),
    COMMETHOD(['propget'], HRESULT, 'caption',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'accessible' )),
    COMMETHOD(['propget'], HRESULT, 'columnDescription',
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(BSTR), 'description' )),
    COMMETHOD(['propget'], HRESULT, 'nColumns',
              ( ['retval', 'out'], POINTER(c_int), 'columnCount' )),
    COMMETHOD(['propget'], HRESULT, 'nRows',
              ( ['retval', 'out'], POINTER(c_int), 'rowCount' )),
    COMMETHOD(['propget'], HRESULT, 'nSelectedCells',
              ( ['retval', 'out'], POINTER(c_int), 'cellCount' )),
    COMMETHOD(['propget'], HRESULT, 'nSelectedColumns',
              ( ['retval', 'out'], POINTER(c_int), 'columnCount' )),
    COMMETHOD(['propget'], HRESULT, 'nSelectedRows',
              ( ['retval', 'out'], POINTER(c_int), 'rowCount' )),
    COMMETHOD(['propget'], HRESULT, 'rowDescription',
              ( ['in'], c_int, 'row' ),
              ( ['retval', 'out'], POINTER(BSTR), 'description' )),
    COMMETHOD(['propget'], HRESULT, 'selectedCells',
              ( ['out'], POINTER(POINTER(POINTER(IUnknown))), 'cells' ),
              ( ['retval', 'out'], POINTER(c_int), 'nSelectedCells' )),
    COMMETHOD(['propget'], HRESULT, 'selectedColumns',
              ( ['out'], POINTER(POINTER(c_int)), 'selectedColumns' ),
              ( ['retval', 'out'], POINTER(c_int), 'nColumns' )),
    COMMETHOD(['propget'], HRESULT, 'selectedRows',
              ( ['out'], POINTER(POINTER(c_int)), 'selectedRows' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRows' )),
    COMMETHOD(['propget'], HRESULT, 'summary',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'accessible' )),
    COMMETHOD(['propget'], HRESULT, 'isColumnSelected',
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD(['propget'], HRESULT, 'isRowSelected',
              ( ['in'], c_int, 'row' ),
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD([], HRESULT, 'selectRow',
              ( ['in'], c_int, 'row' )),
    COMMETHOD([], HRESULT, 'selectColumn',
              ( ['in'], c_int, 'column' )),
    COMMETHOD([], HRESULT, 'unselectRow',
              ( ['in'], c_int, 'row' )),
    COMMETHOD([], HRESULT, 'unselectColumn',
              ( ['in'], c_int, 'column' )),
    COMMETHOD(['propget'], HRESULT, 'modelChange',
              ( ['retval', 'out'], POINTER(IA2TableModelChange), 'modelChange' )),
]
################################################################
## code template for IAccessibleTable2 implementation
##class IAccessibleTable2_Impl(object):
##    @property
##    def nColumns(self):
##        '-no docstring-'
##        #return columnCount
##
##    @property
##    def rowDescription(self, row):
##        '-no docstring-'
##        #return description
##
##    @property
##    def cellAt(self, row, column):
##        '-no docstring-'
##        #return cell
##
##    def unselectRow(self, row):
##        '-no docstring-'
##        #return 
##
##    @property
##    def isColumnSelected(self, column):
##        '-no docstring-'
##        #return isSelected
##
##    @property
##    def nSelectedColumns(self):
##        '-no docstring-'
##        #return columnCount
##
##    @property
##    def summary(self):
##        '-no docstring-'
##        #return accessible
##
##    def unselectColumn(self, column):
##        '-no docstring-'
##        #return 
##
##    def selectColumn(self, column):
##        '-no docstring-'
##        #return 
##
##    @property
##    def selectedCells(self):
##        '-no docstring-'
##        #return cells, nSelectedCells
##
##    @property
##    def nRows(self):
##        '-no docstring-'
##        #return rowCount
##
##    @property
##    def caption(self):
##        '-no docstring-'
##        #return accessible
##
##    @property
##    def nSelectedCells(self):
##        '-no docstring-'
##        #return cellCount
##
##    @property
##    def columnDescription(self, column):
##        '-no docstring-'
##        #return description
##
##    @property
##    def nSelectedRows(self):
##        '-no docstring-'
##        #return rowCount
##
##    @property
##    def selectedRows(self):
##        '-no docstring-'
##        #return selectedRows, nRows
##
##    @property
##    def isRowSelected(self, row):
##        '-no docstring-'
##        #return isSelected
##
##    @property
##    def selectedColumns(self):
##        '-no docstring-'
##        #return selectedColumns, nColumns
##
##    @property
##    def modelChange(self):
##        '-no docstring-'
##        #return modelChange
##
##    def selectRow(self, row):
##        '-no docstring-'
##        #return 
##


# values for enumeration 'IA2TableModelChangeType'
IA2_TABLE_MODEL_CHANGE_INSERT = 0
IA2_TABLE_MODEL_CHANGE_DELETE = 1
IA2_TABLE_MODEL_CHANGE_UPDATE = 2
IA2TableModelChangeType = c_int # enum
IA2TableModelChange._fields_ = [
    ('type', IA2TableModelChangeType),
    ('firstRow', c_int),
    ('lastRow', c_int),
    ('firstColumn', c_int),
    ('lastColumn', c_int),
]
assert sizeof(IA2TableModelChange) == 20, sizeof(IA2TableModelChange)
assert alignment(IA2TableModelChange) == 4, alignment(IA2TableModelChange)
IAccessibleRelation._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'relationType',
              ( ['retval', 'out'], POINTER(BSTR), 'relationType' )),
    COMMETHOD(['propget'], HRESULT, 'localizedRelationType',
              ( ['retval', 'out'], POINTER(BSTR), 'localizedRelationType' )),
    COMMETHOD(['propget'], HRESULT, 'nTargets',
              ( ['retval', 'out'], POINTER(c_int), 'nTargets' )),
    COMMETHOD(['propget'], HRESULT, 'target',
              ( ['in'], c_int, 'targetIndex' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'target' )),
    COMMETHOD(['propget'], HRESULT, 'targets',
              ( ['in'], c_int, 'maxTargets' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'targets' ),
              ( ['retval', 'out'], POINTER(c_int), 'nTargets' )),
]
################################################################
## code template for IAccessibleRelation implementation
##class IAccessibleRelation_Impl(object):
##    @property
##    def relationType(self):
##        '-no docstring-'
##        #return relationType
##
##    @property
##    def nTargets(self):
##        '-no docstring-'
##        #return nTargets
##
##    @property
##    def target(self, targetIndex):
##        '-no docstring-'
##        #return target
##
##    @property
##    def localizedRelationType(self):
##        '-no docstring-'
##        #return localizedRelationType
##
##    @property
##    def targets(self, maxTargets):
##        '-no docstring-'
##        #return targets, nTargets
##

class IAccessibleComponent(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{1546D4B0-4C98-4BDA-89AE-9A64748BDDE4}')
    _idlflags_ = []
IAccessibleComponent._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'locationInParent',
              ( ['out'], POINTER(c_int), 'x' ),
              ( ['retval', 'out'], POINTER(c_int), 'y' )),
    COMMETHOD(['propget'], HRESULT, 'foreground',
              ( ['retval', 'out'], POINTER(c_int), 'foreground' )),
    COMMETHOD(['propget'], HRESULT, 'background',
              ( ['retval', 'out'], POINTER(c_int), 'background' )),
]
################################################################
## code template for IAccessibleComponent implementation
##class IAccessibleComponent_Impl(object):
##    @property
##    def foreground(self):
##        '-no docstring-'
##        #return foreground
##
##    @property
##    def locationInParent(self):
##        '-no docstring-'
##        #return x, y
##
##    @property
##    def background(self):
##        '-no docstring-'
##        #return background
##


# values for enumeration 'IA2EventID'
IA2_EVENT_ACTION_CHANGED = 257
IA2_EVENT_ACTIVE_DECENDENT_CHANGED = 258
IA2_EVENT_ACTIVE_DESCENDANT_CHANGED = 258
IA2_EVENT_DOCUMENT_ATTRIBUTE_CHANGED = 259
IA2_EVENT_DOCUMENT_CONTENT_CHANGED = 260
IA2_EVENT_DOCUMENT_LOAD_COMPLETE = 261
IA2_EVENT_DOCUMENT_LOAD_STOPPED = 262
IA2_EVENT_DOCUMENT_RELOAD = 263
IA2_EVENT_HYPERLINK_END_INDEX_CHANGED = 264
IA2_EVENT_HYPERLINK_NUMBER_OF_ANCHORS_CHANGED = 265
IA2_EVENT_HYPERLINK_SELECTED_LINK_CHANGED = 266
IA2_EVENT_HYPERTEXT_LINK_ACTIVATED = 267
IA2_EVENT_HYPERTEXT_LINK_SELECTED = 268
IA2_EVENT_HYPERLINK_START_INDEX_CHANGED = 269
IA2_EVENT_HYPERTEXT_CHANGED = 270
IA2_EVENT_HYPERTEXT_NLINKS_CHANGED = 271
IA2_EVENT_OBJECT_ATTRIBUTE_CHANGED = 272
IA2_EVENT_PAGE_CHANGED = 273
IA2_EVENT_SECTION_CHANGED = 274
IA2_EVENT_TABLE_CAPTION_CHANGED = 275
IA2_EVENT_TABLE_COLUMN_DESCRIPTION_CHANGED = 276
IA2_EVENT_TABLE_COLUMN_HEADER_CHANGED = 277
IA2_EVENT_TABLE_MODEL_CHANGED = 278
IA2_EVENT_TABLE_ROW_DESCRIPTION_CHANGED = 279
IA2_EVENT_TABLE_ROW_HEADER_CHANGED = 280
IA2_EVENT_TABLE_SUMMARY_CHANGED = 281
IA2_EVENT_TEXT_ATTRIBUTE_CHANGED = 282
IA2_EVENT_TEXT_CARET_MOVED = 283
IA2_EVENT_TEXT_CHANGED = 284
IA2_EVENT_TEXT_COLUMN_CHANGED = 285
IA2_EVENT_TEXT_INSERTED = 286
IA2_EVENT_TEXT_REMOVED = 287
IA2_EVENT_TEXT_UPDATED = 288
IA2_EVENT_TEXT_SELECTION_CHANGED = 289
IA2_EVENT_VISIBLE_DATA_CHANGED = 290
IA2EventID = c_int # enum
IA2TextSegment._fields_ = [
    ('text', BSTR),
    ('start', c_int),
    ('end', c_int),
]
assert sizeof(IA2TextSegment) == 12, sizeof(IA2TextSegment)
assert alignment(IA2TextSegment) == 4, alignment(IA2TextSegment)

# values for enumeration 'IA2TextSpecialOffsets'
IA2_TEXT_OFFSET_LENGTH = -1
IA2_TEXT_OFFSET_CARET = -2
IA2TextSpecialOffsets = c_int # enum
class IAccessibleImage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{FE5ABB3D-615E-4F7B-909F-5F0EDA9E8DDE}')
    _idlflags_ = []
IAccessibleImage._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'description',
              ( ['retval', 'out'], POINTER(BSTR), 'description' )),
    COMMETHOD(['propget'], HRESULT, 'imagePosition',
              ( ['in'], IA2CoordinateType, 'coordinateType' ),
              ( ['out'], POINTER(c_int), 'x' ),
              ( ['retval', 'out'], POINTER(c_int), 'y' )),
    COMMETHOD(['propget'], HRESULT, 'imageSize',
              ( ['out'], POINTER(c_int), 'height' ),
              ( ['retval', 'out'], POINTER(c_int), 'width' )),
]
################################################################
## code template for IAccessibleImage implementation
##class IAccessibleImage_Impl(object):
##    @property
##    def imagePosition(self, coordinateType):
##        '-no docstring-'
##        #return x, y
##
##    @property
##    def description(self):
##        '-no docstring-'
##        #return description
##
##    @property
##    def imageSize(self):
##        '-no docstring-'
##        #return height, width
##

class IAccessibleTableCell(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{594116B1-C99F-4847-AD06-0A7A86ECE645}')
    _idlflags_ = []
IAccessibleTableCell._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'columnExtent',
              ( ['retval', 'out'], POINTER(c_int), 'nColumnsSpanned' )),
    COMMETHOD(['propget'], HRESULT, 'columnHeaderCells',
              ( ['out'], POINTER(POINTER(POINTER(IUnknown))), 'cellAccessibles' ),
              ( ['retval', 'out'], POINTER(c_int), 'nColumnHeaderCells' )),
    COMMETHOD(['propget'], HRESULT, 'columnIndex',
              ( ['retval', 'out'], POINTER(c_int), 'columnIndex' )),
    COMMETHOD(['propget'], HRESULT, 'rowExtent',
              ( ['retval', 'out'], POINTER(c_int), 'nRowsSpanned' )),
    COMMETHOD(['propget'], HRESULT, 'rowHeaderCells',
              ( ['out'], POINTER(POINTER(POINTER(IUnknown))), 'cellAccessibles' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRowHeaderCells' )),
    COMMETHOD(['propget'], HRESULT, 'rowIndex',
              ( ['retval', 'out'], POINTER(c_int), 'rowIndex' )),
    COMMETHOD(['propget'], HRESULT, 'isSelected',
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD(['propget'], HRESULT, 'rowColumnExtents',
              ( ['out'], POINTER(c_int), 'row' ),
              ( ['out'], POINTER(c_int), 'column' ),
              ( ['out'], POINTER(c_int), 'rowExtents' ),
              ( ['out'], POINTER(c_int), 'columnExtents' ),
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD(['propget'], HRESULT, 'table',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'table' )),
]
################################################################
## code template for IAccessibleTableCell implementation
##class IAccessibleTableCell_Impl(object):
##    @property
##    def isSelected(self):
##        '-no docstring-'
##        #return isSelected
##
##    @property
##    def rowIndex(self):
##        '-no docstring-'
##        #return rowIndex
##
##    @property
##    def rowColumnExtents(self):
##        '-no docstring-'
##        #return row, column, rowExtents, columnExtents, isSelected
##
##    @property
##    def columnHeaderCells(self):
##        '-no docstring-'
##        #return cellAccessibles, nColumnHeaderCells
##
##    @property
##    def columnIndex(self):
##        '-no docstring-'
##        #return columnIndex
##
##    @property
##    def rowHeaderCells(self):
##        '-no docstring-'
##        #return cellAccessibles, nRowHeaderCells
##
##    @property
##    def table(self):
##        '-no docstring-'
##        #return table
##
##    @property
##    def rowExtent(self):
##        '-no docstring-'
##        #return nRowsSpanned
##
##    @property
##    def columnExtent(self):
##        '-no docstring-'
##        #return nColumnsSpanned
##

class _RemotableHandle(Structure):
    pass
class __MIDL_IWinTypes_0009(Union):
    pass
__MIDL_IWinTypes_0009._fields_ = [
    ('hInproc', c_int),
    ('hRemote', c_int),
]
assert sizeof(__MIDL_IWinTypes_0009) == 4, sizeof(__MIDL_IWinTypes_0009)
assert alignment(__MIDL_IWinTypes_0009) == 4, alignment(__MIDL_IWinTypes_0009)
_RemotableHandle._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0009),
]
assert sizeof(_RemotableHandle) == 8, sizeof(_RemotableHandle)
assert alignment(_RemotableHandle) == 4, alignment(_RemotableHandle)

# values for enumeration 'IA2States'
IA2_STATE_ACTIVE = 1
IA2_STATE_ARMED = 2
IA2_STATE_DEFUNCT = 4
IA2_STATE_EDITABLE = 8
IA2_STATE_HORIZONTAL = 16
IA2_STATE_ICONIFIED = 32
IA2_STATE_INVALID_ENTRY = 64
IA2_STATE_MANAGES_DESCENDANTS = 128
IA2_STATE_MODAL = 256
IA2_STATE_MULTI_LINE = 512
IA2_STATE_OPAQUE = 1024
IA2_STATE_REQUIRED = 2048
IA2_STATE_SELECTABLE_TEXT = 4096
IA2_STATE_SINGLE_LINE = 8192
IA2_STATE_STALE = 16384
IA2_STATE_SUPPORTS_AUTOCOMPLETION = 32768
IA2_STATE_TRANSIENT = 65536
IA2_STATE_VERTICAL = 131072
IA2States = c_int # enum
class IAccessibleApplication(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D49DED83-5B25-43F4-9B95-93B44595979E}')
    _idlflags_ = []
IAccessibleApplication._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'appName',
              ( ['retval', 'out'], POINTER(BSTR), 'name' )),
    COMMETHOD(['propget'], HRESULT, 'appVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'version' )),
    COMMETHOD(['propget'], HRESULT, 'toolkitName',
              ( ['retval', 'out'], POINTER(BSTR), 'name' )),
    COMMETHOD(['propget'], HRESULT, 'toolkitVersion',
              ( ['retval', 'out'], POINTER(BSTR), 'version' )),
]
################################################################
## code template for IAccessibleApplication implementation
##class IAccessibleApplication_Impl(object):
##    @property
##    def toolkitVersion(self):
##        '-no docstring-'
##        #return version
##
##    @property
##    def toolkitName(self):
##        '-no docstring-'
##        #return name
##
##    @property
##    def appVersion(self):
##        '-no docstring-'
##        #return version
##
##    @property
##    def appName(self):
##        '-no docstring-'
##        #return name
##


# values for enumeration 'IA2Role'
IA2_ROLE_UNKNOWN = 0
IA2_ROLE_CANVAS = 1025
IA2_ROLE_CAPTION = 1026
IA2_ROLE_CHECK_MENU_ITEM = 1027
IA2_ROLE_COLOR_CHOOSER = 1028
IA2_ROLE_DATE_EDITOR = 1029
IA2_ROLE_DESKTOP_ICON = 1030
IA2_ROLE_DESKTOP_PANE = 1031
IA2_ROLE_DIRECTORY_PANE = 1032
IA2_ROLE_EDITBAR = 1033
IA2_ROLE_EMBEDDED_OBJECT = 1034
IA2_ROLE_ENDNOTE = 1035
IA2_ROLE_FILE_CHOOSER = 1036
IA2_ROLE_FONT_CHOOSER = 1037
IA2_ROLE_FOOTER = 1038
IA2_ROLE_FOOTNOTE = 1039
IA2_ROLE_FORM = 1040
IA2_ROLE_FRAME = 1041
IA2_ROLE_GLASS_PANE = 1042
IA2_ROLE_HEADER = 1043
IA2_ROLE_HEADING = 1044
IA2_ROLE_ICON = 1045
IA2_ROLE_IMAGE_MAP = 1046
IA2_ROLE_INPUT_METHOD_WINDOW = 1047
IA2_ROLE_INTERNAL_FRAME = 1048
IA2_ROLE_LABEL = 1049
IA2_ROLE_LAYERED_PANE = 1050
IA2_ROLE_NOTE = 1051
IA2_ROLE_OPTION_PANE = 1052
IA2_ROLE_PAGE = 1053
IA2_ROLE_PARAGRAPH = 1054
IA2_ROLE_RADIO_MENU_ITEM = 1055
IA2_ROLE_REDUNDANT_OBJECT = 1056
IA2_ROLE_ROOT_PANE = 1057
IA2_ROLE_RULER = 1058
IA2_ROLE_SCROLL_PANE = 1059
IA2_ROLE_SECTION = 1060
IA2_ROLE_SHAPE = 1061
IA2_ROLE_SPLIT_PANE = 1062
IA2_ROLE_TEAR_OFF_MENU = 1063
IA2_ROLE_TERMINAL = 1064
IA2_ROLE_TEXT_FRAME = 1065
IA2_ROLE_TOGGLE_BUTTON = 1066
IA2_ROLE_VIEW_PORT = 1067
IA2Role = c_int # enum
class IAccessibleHypertext(IAccessibleText):
    _case_insensitive_ = True
    _iid_ = GUID('{6B4F8BBF-F1F2-418A-B35E-A195BC4103B9}')
    _idlflags_ = []
IAccessibleHypertext._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'nHyperlinks',
              ( ['retval', 'out'], POINTER(c_int), 'hyperlinkCount' )),
    COMMETHOD(['propget'], HRESULT, 'hyperlink',
              ( ['in'], c_int, 'index' ),
              ( ['retval', 'out'], POINTER(POINTER(IAccessibleHyperlink)), 'hyperlink' )),
    COMMETHOD(['propget'], HRESULT, 'hyperlinkIndex',
              ( ['in'], c_int, 'charIndex' ),
              ( ['retval', 'out'], POINTER(c_int), 'hyperlinkIndex' )),
]
################################################################
## code template for IAccessibleHypertext implementation
##class IAccessibleHypertext_Impl(object):
##    @property
##    def hyperlinkIndex(self, charIndex):
##        '-no docstring-'
##        #return hyperlinkIndex
##
##    @property
##    def nHyperlinks(self):
##        '-no docstring-'
##        #return hyperlinkCount
##
##    @property
##    def hyperlink(self, index):
##        '-no docstring-'
##        #return hyperlink
##

IA2Locale._fields_ = [
    ('language', BSTR),
    ('country', BSTR),
    ('variant', BSTR),
]
assert sizeof(IA2Locale) == 12, sizeof(IA2Locale)
assert alignment(IA2Locale) == 4, alignment(IA2Locale)
class IAccessibleTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{35AD8070-C20C-4FB4-B094-F4F7275DD469}')
    _idlflags_ = []
IAccessibleTable._methods_ = [
    COMMETHOD(['propget'], HRESULT, 'accessibleAt',
              ( ['in'], c_int, 'row' ),
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'accessible' )),
    COMMETHOD(['propget'], HRESULT, 'caption',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'accessible' )),
    COMMETHOD(['propget'], HRESULT, 'childIndex',
              ( ['in'], c_int, 'rowIndex' ),
              ( ['in'], c_int, 'columnIndex' ),
              ( ['retval', 'out'], POINTER(c_int), 'cellIndex' )),
    COMMETHOD(['propget'], HRESULT, 'columnDescription',
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(BSTR), 'description' )),
    COMMETHOD(['propget'], HRESULT, 'columnExtentAt',
              ( ['in'], c_int, 'row' ),
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(c_int), 'nColumnsSpanned' )),
    COMMETHOD(['propget'], HRESULT, 'columnHeader',
              ( ['out'], POINTER(POINTER(IAccessibleTable)), 'accessibleTable' ),
              ( ['retval', 'out'], POINTER(c_int), 'startingRowIndex' )),
    COMMETHOD(['propget'], HRESULT, 'columnIndex',
              ( ['in'], c_int, 'cellIndex' ),
              ( ['retval', 'out'], POINTER(c_int), 'columnIndex' )),
    COMMETHOD(['propget'], HRESULT, 'nColumns',
              ( ['retval', 'out'], POINTER(c_int), 'columnCount' )),
    COMMETHOD(['propget'], HRESULT, 'nRows',
              ( ['retval', 'out'], POINTER(c_int), 'rowCount' )),
    COMMETHOD(['propget'], HRESULT, 'nSelectedChildren',
              ( ['retval', 'out'], POINTER(c_int), 'cellCount' )),
    COMMETHOD(['propget'], HRESULT, 'nSelectedColumns',
              ( ['retval', 'out'], POINTER(c_int), 'columnCount' )),
    COMMETHOD(['propget'], HRESULT, 'nSelectedRows',
              ( ['retval', 'out'], POINTER(c_int), 'rowCount' )),
    COMMETHOD(['propget'], HRESULT, 'rowDescription',
              ( ['in'], c_int, 'row' ),
              ( ['retval', 'out'], POINTER(BSTR), 'description' )),
    COMMETHOD(['propget'], HRESULT, 'rowExtentAt',
              ( ['in'], c_int, 'row' ),
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRowsSpanned' )),
    COMMETHOD(['propget'], HRESULT, 'rowHeader',
              ( ['out'], POINTER(POINTER(IAccessibleTable)), 'accessibleTable' ),
              ( ['retval', 'out'], POINTER(c_int), 'startingColumnIndex' )),
    COMMETHOD(['propget'], HRESULT, 'rowIndex',
              ( ['in'], c_int, 'cellIndex' ),
              ( ['retval', 'out'], POINTER(c_int), 'rowIndex' )),
    COMMETHOD(['propget'], HRESULT, 'selectedChildren',
              ( ['in'], c_int, 'maxChildren' ),
              ( ['out'], POINTER(POINTER(c_int)), 'children' ),
              ( ['retval', 'out'], POINTER(c_int), 'nChildren' )),
    COMMETHOD(['propget'], HRESULT, 'selectedColumns',
              ( ['in'], c_int, 'maxColumns' ),
              ( ['out'], POINTER(POINTER(c_int)), 'columns' ),
              ( ['retval', 'out'], POINTER(c_int), 'nColumns' )),
    COMMETHOD(['propget'], HRESULT, 'selectedRows',
              ( ['in'], c_int, 'maxRows' ),
              ( ['out'], POINTER(POINTER(c_int)), 'rows' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRows' )),
    COMMETHOD(['propget'], HRESULT, 'summary',
              ( ['retval', 'out'], POINTER(POINTER(IUnknown)), 'accessible' )),
    COMMETHOD(['propget'], HRESULT, 'isColumnSelected',
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD(['propget'], HRESULT, 'isRowSelected',
              ( ['in'], c_int, 'row' ),
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD(['propget'], HRESULT, 'isSelected',
              ( ['in'], c_int, 'row' ),
              ( ['in'], c_int, 'column' ),
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD([], HRESULT, 'selectRow',
              ( ['in'], c_int, 'row' )),
    COMMETHOD([], HRESULT, 'selectColumn',
              ( ['in'], c_int, 'column' )),
    COMMETHOD([], HRESULT, 'unselectRow',
              ( ['in'], c_int, 'row' )),
    COMMETHOD([], HRESULT, 'unselectColumn',
              ( ['in'], c_int, 'column' )),
    COMMETHOD(['propget'], HRESULT, 'rowColumnExtentsAtIndex',
              ( ['in'], c_int, 'index' ),
              ( ['out'], POINTER(c_int), 'row' ),
              ( ['out'], POINTER(c_int), 'column' ),
              ( ['out'], POINTER(c_int), 'rowExtents' ),
              ( ['out'], POINTER(c_int), 'columnExtents' ),
              ( ['retval', 'out'], STRING, 'isSelected' )),
    COMMETHOD(['propget'], HRESULT, 'modelChange',
              ( ['retval', 'out'], POINTER(IA2TableModelChange), 'modelChange' )),
]
################################################################
## code template for IAccessibleTable implementation
##class IAccessibleTable_Impl(object):
##    @property
##    def nColumns(self):
##        '-no docstring-'
##        #return columnCount
##
##    @property
##    def isColumnSelected(self, column):
##        '-no docstring-'
##        #return isSelected
##
##    @property
##    def columnHeader(self):
##        '-no docstring-'
##        #return accessibleTable, startingRowIndex
##
##    @property
##    def selectedColumns(self, maxColumns):
##        '-no docstring-'
##        #return columns, nColumns
##
##    @property
##    def columnDescription(self, column):
##        '-no docstring-'
##        #return description
##
##    @property
##    def modelChange(self):
##        '-no docstring-'
##        #return modelChange
##
##    @property
##    def columnExtentAt(self, row, column):
##        '-no docstring-'
##        #return nColumnsSpanned
##
##    @property
##    def rowHeader(self):
##        '-no docstring-'
##        #return accessibleTable, startingColumnIndex
##
##    @property
##    def childIndex(self, rowIndex, columnIndex):
##        '-no docstring-'
##        #return cellIndex
##
##    @property
##    def accessibleAt(self, row, column):
##        '-no docstring-'
##        #return accessible
##
##    @property
##    def caption(self):
##        '-no docstring-'
##        #return accessible
##
##    @property
##    def rowIndex(self, cellIndex):
##        '-no docstring-'
##        #return rowIndex
##
##    @property
##    def nRows(self):
##        '-no docstring-'
##        #return rowCount
##
##    @property
##    def isSelected(self, row, column):
##        '-no docstring-'
##        #return isSelected
##
##    @property
##    def nSelectedChildren(self):
##        '-no docstring-'
##        #return cellCount
##
##    def unselectRow(self, row):
##        '-no docstring-'
##        #return 
##
##    @property
##    def rowDescription(self, row):
##        '-no docstring-'
##        #return description
##
##    @property
##    def rowExtentAt(self, row, column):
##        '-no docstring-'
##        #return nRowsSpanned
##
##    @property
##    def nSelectedColumns(self):
##        '-no docstring-'
##        #return columnCount
##
##    @property
##    def selectedChildren(self, maxChildren):
##        '-no docstring-'
##        #return children, nChildren
##
##    def unselectColumn(self, column):
##        '-no docstring-'
##        #return 
##
##    @property
##    def nSelectedRows(self):
##        '-no docstring-'
##        #return rowCount
##
##    def selectRow(self, row):
##        '-no docstring-'
##        #return 
##
##    def selectColumn(self, column):
##        '-no docstring-'
##        #return 
##
##    @property
##    def summary(self):
##        '-no docstring-'
##        #return accessible
##
##    @property
##    def columnIndex(self, cellIndex):
##        '-no docstring-'
##        #return columnIndex
##
##    @property
##    def selectedRows(self, maxRows):
##        '-no docstring-'
##        #return rows, nRows
##
##    @property
##    def isRowSelected(self, row):
##        '-no docstring-'
##        #return isSelected
##
##    @property
##    def rowColumnExtentsAtIndex(self, index):
##        '-no docstring-'
##        #return row, column, rowExtents, columnExtents, isSelected
##

__all__ = ['IA2_EVENT_SECTION_CHANGED', 'IAccessibleEditableText',
           'IAccessibleAction', 'IA2_ROLE_EDITBAR',
           'IA2_EVENT_TEXT_INSERTED',
           'IA2_EVENT_HYPERLINK_START_INDEX_CHANGED',
           'IA2_EVENT_TEXT_CARET_MOVED',
           'IA2_EVENT_DOCUMENT_ATTRIBUTE_CHANGED',
           'IA2_ROLE_SCROLL_PANE', 'IA2_EVENT_HYPERTEXT_CHANGED',
           'IA2_EVENT_TEXT_COLUMN_CHANGED',
           'IA2_TEXT_BOUNDARY_SENTENCE',
           'IA2_EVENT_DOCUMENT_LOAD_COMPLETE', 'IA2_ROLE_UNKNOWN',
           'IA2_COORDTYPE_PARENT_RELATIVE',
           'IA2_EVENT_DOCUMENT_CONTENT_CHANGED',
           'IA2_ROLE_RADIO_MENU_ITEM', 'IAccessibleApplication',
           '_RemotableHandle', 'IA2_STATE_STALE', 'IA2_ROLE_CAPTION',
           'IA2_EVENT_HYPERLINK_END_INDEX_CHANGED',
           'IA2_ROLE_TOGGLE_BUTTON', 'IA2_ROLE_PAGE',
           'IA2_ROLE_FOOTER', 'IA2_ROLE_DIRECTORY_PANE',
           '__MIDL_IWinTypes_0009', 'IA2TextSegment',
           'IA2_ROLE_CHECK_MENU_ITEM', 'IA2_ROLE_FILE_CHOOSER',
           'IA2_COORDTYPE_SCREEN_RELATIVE', 'IAccessibleValue',
           'IA2_ROLE_FOOTNOTE', 'IA2_ROLE_RULER',
           'IA2_EVENT_TEXT_UPDATED', 'IA2_ROLE_ROOT_PANE',
           'IA2_STATE_ACTIVE', 'IA2_EVENT_HYPERTEXT_LINK_ACTIVATED',
           'IA2_ROLE_ICON', 'IA2_STATE_MULTI_LINE', 'IA2Locale',
           'IA2_EVENT_HYPERTEXT_NLINKS_CHANGED',
           'IA2_STATE_HORIZONTAL',
           'IA2_EVENT_ACTIVE_DESCENDANT_CHANGED',
           'IA2TableModelChangeType', 'IA2_SCROLL_TYPE_TOP_EDGE',
           'IA2_TEXT_BOUNDARY_CHAR', 'IAccessibleHypertext',
           'IAccessible2', 'IA2_EVENT_TEXT_ATTRIBUTE_CHANGED',
           'IAccessible', 'IA2ScrollType', 'IA2_ROLE_LAYERED_PANE',
           'IA2_ROLE_SECTION', 'IA2_ROLE_DATE_EDITOR', 'IA2States',
           'IA2_TEXT_BOUNDARY_ALL', 'IA2_EVENT_TABLE_CAPTION_CHANGED',
           'IA2_EVENT_TABLE_COLUMN_HEADER_CHANGED', 'IA2_ROLE_FORM',
           'IA2_EVENT_OBJECT_ATTRIBUTE_CHANGED',
           'IA2_ROLE_GLASS_PANE', 'IAccessibleText',
           'IA2_ROLE_DESKTOP_PANE', 'IA2_TABLE_MODEL_CHANGE_UPDATE',
           'IA2_ROLE_FONT_CHOOSER', 'IA2_ROLE_LABEL',
           'IA2_ROLE_REDUNDANT_OBJECT', 'IA2_ROLE_TEAR_OFF_MENU',
           'IA2_TEXT_BOUNDARY_WORD', 'IA2TextBoundaryType',
           'IA2_EVENT_TEXT_SELECTION_CHANGED', 'IA2_STATE_REQUIRED',
           'IA2TableModelChange', 'IA2_ROLE_OPTION_PANE',
           'IA2_STATE_SUPPORTS_AUTOCOMPLETION',
           'IAccessibleHyperlink',
           'IA2_EVENT_TABLE_ROW_HEADER_CHANGED',
           'IA2_TEXT_BOUNDARY_LINE', 'IA2_ROLE_INPUT_METHOD_WINDOW',
           'IA2_ROLE_HEADER', 'IA2_STATE_OPAQUE',
           'IA2_EVENT_TABLE_COLUMN_DESCRIPTION_CHANGED',
           'IA2_ROLE_NOTE', 'IA2_TEXT_OFFSET_LENGTH',
           'IA2_ROLE_SHAPE', 'IAccessibleTable',
           'IA2_ROLE_SPLIT_PANE',
           'IA2_EVENT_HYPERLINK_NUMBER_OF_ANCHORS_CHANGED',
           'IA2_SCROLL_TYPE_TOP_LEFT', 'IA2_ROLE_PARAGRAPH',
           'IA2CoordinateType', 'IA2_ROLE_DESKTOP_ICON',
           'IA2_TABLE_MODEL_CHANGE_DELETE', 'IA2_STATE_INVALID_ENTRY',
           'IAccessibleImage', 'IA2_TEXT_BOUNDARY_PARAGRAPH',
           'IA2_STATE_TRANSIENT', 'IA2_STATE_MANAGES_DESCENDANTS',
           'IA2_EVENT_PAGE_CHANGED',
           'IA2_EVENT_TABLE_SUMMARY_CHANGED', 'IA2_TEXT_OFFSET_CARET',
           'IA2_SCROLL_TYPE_LEFT_EDGE', 'IA2_ROLE_TERMINAL',
           'IA2_SCROLL_TYPE_BOTTOM_EDGE',
           'IA2_EVENT_HYPERLINK_SELECTED_LINK_CHANGED',
           'IA2_EVENT_TABLE_MODEL_CHANGED', 'IA2_STATE_SINGLE_LINE',
           'IA2_STATE_ICONIFIED', 'IA2_SCROLL_TYPE_ANYWHERE',
           'IA2_TABLE_MODEL_CHANGE_INSERT', 'IA2_EVENT_TEXT_CHANGED',
           'IA2_STATE_DEFUNCT', 'IA2_EVENT_DOCUMENT_LOAD_STOPPED',
           'IAccessibleTable2', 'IA2EventID',
           'IA2_ROLE_EMBEDDED_OBJECT', 'IA2_ROLE_FRAME',
           'IA2_EVENT_ACTIVE_DECENDENT_CHANGED',
           'IA2_EVENT_HYPERTEXT_LINK_SELECTED', 'IA2_STATE_VERTICAL',
           'IA2_ROLE_VIEW_PORT', 'IA2_ROLE_COLOR_CHOOSER',
           'IA2_EVENT_ACTION_CHANGED', 'IA2_ROLE_CANVAS',
           'IA2_EVENT_TABLE_ROW_DESCRIPTION_CHANGED',
           'IAccessibleRelation', 'IA2_STATE_SELECTABLE_TEXT',
           'IA2_STATE_MODAL', 'IA2_STATE_ARMED',
           'IAccessibleTableCell', 'IA2_STATE_EDITABLE',
           'IA2_ROLE_TEXT_FRAME', 'IAccessibleComponent', 'IA2Role',
           'IA2_SCROLL_TYPE_BOTTOM_RIGHT',
           'IA2_SCROLL_TYPE_RIGHT_EDGE',
           'IA2_EVENT_VISIBLE_DATA_CHANGED', 'IA2TextSpecialOffsets',
           'IA2_EVENT_TEXT_REMOVED', 'IA2_EVENT_DOCUMENT_RELOAD',
           'IA2_ROLE_ENDNOTE', 'IA2_ROLE_INTERNAL_FRAME',
           'IA2_ROLE_HEADING', 'IA2_ROLE_IMAGE_MAP']
from comtypes import _check_version; _check_version('501')
