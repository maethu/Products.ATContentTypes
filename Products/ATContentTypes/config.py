# -*- coding: latin-1 -*-
#  ATContentTypes http://sf.net/projects/collective/
#  Archetypes reimplementation of the CMF core types
#  Copyright (c) 2003-2004 AT Content Types development team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""AT Content Types configuration file

DO NOT CHANGE THIS FILE!

All changes will be overwritten by the next release. Use a customconfig instead.
See customconfig.py.example


"""
__author__  = ''
__docformat__ = 'restructuredtext'

from Products.CMFCore import CMFCorePermissions
import string

try:
    True
except NameError:
    True  = 1
    False = 0

###############################################################################
## user options
## The options in this section can be overwritten by customconfig

## enable mxTidy for ATDocument and ATNewsItem?
MX_TIDY_ENABLED = True

## options for mxTidy
## read http://www.egenix.com/files/python/mxTidy.html for more informations
MX_TIDY_OPTIONS= {
    'drop_font_tags'   : 1,
    'drop_empty_paras' : 1,
    'input_xml'        : 0,
    'output_xhtml'     : 1,
    'quiet'            : 1,
    'show_warnings'    : 1,
    'tab_size'         : 4,
    'wrap'             : 72,
    #'indent'           : 'auto',
    'indent_spaces'    : 1,
    'word_2000'        : 1,
    'char_encoding'    : 'raw',
    }

## enable external storage
## requires ExternalStorage from Christian Scholz
EXT_STORAGE_ENABLE = False

## use TemplateMixin?
## if enabled users can choose between different view templates for each object
ENABLE_TEMPLATE_MIXIN = True

## TemplateMixin write permission. Only if the member has this permission he
## is allowed to choose another template then the default permission
TEMPLATE_MIXIN_PERMISSION = CMFCorePermissions.ManagePortal

## use ConstrainedMixin?
## if enabled you can constrain allowed types on an ATCT Folder
ENABLE_CONSTRAIN_TYPES_MIXIN = True
CONSTRAIN_TYPES_MIXIN_PERMISSION = CMFCorePermissions.ManagePortal

## Document History view permission
HISTORY_VIEW_PERMISSION = CMFCorePermissions.ReviewPortalContent

## maximum upload size for ATImage and ATFile in MB. 0 is infinitiv
MAX_FILE_SIZE = 0.0
MAX_IMAGE_SIZE = 0.0

## Default content type for ATDocument and ATNewsItem
ATDOCUMENT_CONTENT_TYPE = 'text/html'        # html

###############################################################################
## private options

PROJECTNAME = "ATContentTypes"
TOOLNAME = "portal_atct"
SKINS_DIR = 'skins'

GLOBALS = globals()

INSTALL_LINGUA_PLONE = True

CONFIGUREABLE = ('MX_TIDY_ENABLED', 'MX_TIDY_OPTIONS', 'EXT_STORAGE_ENABLE',
                 'ENABLE_TEMPLATE_MIXIN', 'TEMPLATE_MIXIN_PERMISSION',
                 'HISTORY_VIEW_PERMISSION', 'MAX_FILE_SIZE', 'MAX_IMAGE_SIZE',
                 'ENABLE_CONSTRAIN_TYPES_MIXIN', 'CONSTRAIN_TYPES_MIXIN_PERMISSION',
                 'ATDOCUMENT_CONTENT_TYPE',
                 )

## using special plone 2 stuff?
try:
    from Products.CMFPlone.PloneFolder import ReplaceableWrapper
except ImportError:
    HAS_PLONE2 = False
else:
    HAS_PLONE2 = True
    del ReplaceableWrapper

## mxTidy available?
try:
    from mx import Tidy
except ImportError:
    HAS_MX_TIDY = False
else:
    HAS_MX_TIDY = True
    try:
        del Tidy
    except AttributeError:
        pass

## tidy only these document types
MX_TIDY_MIMETYPES = (
    'text/html',
     )

## ExternalStorage available?
try:
    from Products.ExternalStorage.ExternalStorage import ExternalStorage
except ImportError:
    HAS_EXT_STORAGE = False
else:
    HAS_EXT_STORAGE = True
    del ExternalStorage

## LinguaPlone addon?
try:
    from Products.LinguaPlone.public import registerType
except ImportError:
    HAS_LINGUA_PLONE = False
else:
    HAS_LINGUA_PLONE = True
    del registerType

## workflow mapping for the installer
WORKFLOW_DEFAULT  = '(Default)'
WORKFLOW_FOLDER   = 'folder_workflow'
WORKFLOW_TOPIC    = 'folder_workflow'
WORKFLOW_CRITERIA = ''

## icon map used for overwriting ATFile icons
ICONMAP = {'application/pdf' : 'pdf_icon.gif',
           'image'           : 'image_icon.gif'}

GOOD_CHARS = string.ascii_letters + string.digits + '._-'
CHAR_MAPPING = {
    ' ' : '_',
    '�' : 'Aa',
    '�' : 'A',
    '�' : 'A',
    '�' : 'A',
    '�' : 'A',
    '�' : 'Ae',
    '�' : 'A',
    '�' : 'Ae',
    '�' : 'C',
    '�' : 'E',
    '�' : 'E',
    '�' : 'E',
    '�' : 'E',
    '�' : 'I',
    '�' : 'I',
    '�' : 'I',
    '�' : 'I',
    '�' : 'D',
    '�' : 'N',
    '�' : 'O',
    '�' : 'O',
    '�' : 'O',
    '�' : 'O',
    '�' : 'Oe',
    '�' : 'Oe',
    '�' : 'U',
    '�' : 'U',
    '�' : 'U',
    '�' : 'Ue',
    '�' : 'Y',
    '�' : 'ss',
    '�' : 'a',
    '�' : 'a',
    '�' : 'a',
    '�' : 'a',
    '�' : 'ae',
    '�' : 'aa',
    '�' : 'ae',
    '�' : 'c',
    '�' : 'e',
    '�' : 'e',
    '�' : 'e',
    '�' : 'e',
    '�' : 'i',
    '�' : 'i',
    '�' : 'i',
    '�' : 'i',
    '�' : 'd',
    '�' : 'n',
    '�' : 'o',
    '�' : 'o',
    '�' : 'o',
    '�' : 'o',
    '�' : 'oe',
    '�' : 'oe',
    '�' : 'u',
    '�' : 'u',
    '�' : 'u',
    '�' : 'ue',
    '�' : 'y',
    '�' : 'y',
    }

MIME_ALIAS = {
    'plain' : 'text/plain',
    'stx'   : 'text/structured',
    'html'  : 'text/html',
    'rest'  : 'text/x-rst',
    'structured-text' : 'text/structured',
    'restructuredtext' : 'text/x-rst',
    }

## force enable some features for ATCT unit testing
import os
if os.environ.get('ZOPETESTCASE', False):
    ENABLE_CONSTRAIN_TYPES_MIXIN = True
    ENABLE_TEMPLATE_MIXIN = True
    EXT_STORAGE_ENABLE = True
    INSTALL_LINGUA_PLONE = True
    EXT_STORAGE_ENABLE = True
    _ATCT_UNIT_TEST_MODE = True
else:
    _ATCT_UNIT_TEST_MODE = False
