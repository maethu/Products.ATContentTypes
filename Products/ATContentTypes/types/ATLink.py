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
"""

$Id: ATLink.py,v 1.1 2004/03/08 10:48:41 tiran Exp $
""" 
__author__  = ''
__docformat__ = 'restructuredtext'

from Products.Archetypes.public import BaseContent, registerType
from Products.CMFCore import CMFCorePermissions
from AccessControl import ClassSecurityInfo
from Products.ATContentTypes.config import *
from Products.ATContentTypes.interfaces.IATContentType import IATContentType
from schemata import ATLinkSchema


class ATLink(BaseContent):
    """An Archetypes derived version of CMFDefault's Link"""

    schema         =  ATLinkSchema

    content_icon   = 'link_icon.gif'
    meta_type      = 'ATLink'
    archetype_name = 'AT Link'
    newTypeFor     = 'Link'
    TypeDescription= ''

    __implements__ = BaseContent.__implements__, IATContentType

    security       = ClassSecurityInfo()

    actions = ({
       'id'          : 'view',
       'name'        : 'View',
       'action'      : 'string:${object_url}/link_view',
       'permissions' : (CMFCorePermissions.View,)
        },
       {
       'id'          : 'edit',
       'name'        : 'Edit',
       'action'      : 'string:${object_url}/atct_edit',
       'permissions' : (CMFCorePermissions.ModifyPortalContent,),
        },
       )

    security.declareProtected(CMFCorePermissions.View, 'remote_url')
    def remote_url(self):
        """backward compatibility with std cmf types"""
        return self.getRemoteUrl()

registerType(ATLink, PROJECTNAME)