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

$Id: ATTopic.py,v 1.2 2004/03/13 19:14:03 tiran Exp $
""" 
__author__  = ''
__docformat__ = 'restructuredtext'

from Products.Archetypes.public import *
from Products.Archetypes.BaseFolder import BaseFolderMixin
from Products.CMFCore import CMFCorePermissions
from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName

from Products.ATContentTypes.types.criteria import CriterionRegistry
from Products.ATContentTypes.Permissions import ChangeTopics, AddTopics
from Products.ATContentTypes.config import *
from Products.ATContentTypes.interfaces.IATContentType import IATContentType
from Products.ATContentTypes.interfaces.IATTopic import IATTopic
from schemata import ATTopicSchema

from types import ListType, TupleType, StringType


class ATTopic(BaseFolderMixin):
    """A topic folder"""

    schema         =  ATTopicSchema

    content_icon   = 'topic_icon.gif'
    meta_type      = 'ATTopic'
    archetype_name = 'AT Topic'
    newTypeFor     = 'Topic'
    TypeDescription= 'A topic is a pre-defined search, showing all items matching\n' \
                     'criteria you specify. Topics may also contain sub-topics.'
    filter_content_types  = 1
    allowed_content_types = 'ATTopic'

    __implements__ = BaseFolderMixin.__implements__, IATContentType, IATTopic

    security       = ClassSecurityInfo()

    actions = ({
       'id'          : 'view',
       'name'        : 'View',
       'action'      : 'string:${object_url}/topic_view',
       'permissions' : (CMFCorePermissions.View,)
        },
       {
       'id'          : 'edit',
       'name'        : 'Edit',
       'action'      : 'string:${object_url}/atct_edit',
       'permissions' : (CMFCorePermissions.ModifyPortalContent,),
        },
       {
       'id'          : 'criteria', 
       'name'        : 'Criteria',
       'action'      : 'string:${object_url}/criterion_edit_form',
       'permissions' : (ChangeTopics,)
        },
       {
       'id'          : 'subtopics',
       'name'        : 'Subtopics',
       'action'      : 'string:${object_url}/topic_subtopics_form',
       'permissions' : (ChangeTopics,)
       }
       )

    security.declareProtected(ChangeTopics, 'listCriteriaTypes')
    def listCriteriaTypes(self):
        """
        """
        return [ {'name': ctype} for ctype in self.listCriteriaMetaTypes() ]

    security.declareProtected(ChangeTopics, 'listCriteriaMetaTypes')
    def listCriteriaMetaTypes(self):
        """
        """
        val = CriterionRegistry.listTypes()
        val.sort()
        return val

    security.declareProtected(ChangeTopics, 'listCriteria')
    def listCriteria( self ):
        """Return a list of our criteria objects.
        """
        val = self.objectValues(self.listCriteriaMetaTypes())
        val.sort()
        return val

    security.declareProtected(ChangeTopics, 'listAvailableFields')
    def listAvailableFields(self):
        """Return a list of available fields for new criteria.
        """
        pcatalog = getToolByName( self, 'portal_catalog' )
        current   = [ crit.Field() for crit in self.listCriteria() ]
        available = pcatalog.indexes()
        val = [ field
                 for field in available
                 if field not in current
               ]
        val.sort()
        return val

    security.declareProtected(ChangeTopics, 'listSubtopics')
    def listSubtopics(self):
        """Return a list of our subtopics.
        """
        val = self.objectValues(self.meta_type)
        val.sort()
        return val

    security.declareProtected(CMFCorePermissions.View, 'buildQuery')
    def buildQuery(self):
        """Construct a catalog query using our criterion objects.
        """
        result = {}
        criteria = self.listCriteria()
        if not criteria:
            # no criteria found
            return None

        if self.getAcquireCriteria():
            try:
                # Tracker 290 asks to allow combinations, like this:
                # parent = aq_parent( self )
                parent = aq_parent( aq_inner( self ) )
                result.update( parent.buildQuery() )
            except: # oh well, can't find parent, or it isn't a Topic.
                pass

        for criterion in criteria:
            for key, value in criterion.getCriteriaItems():
                result[key] = value
        return result

    security.declareProtected(CMFCorePermissions.View, 'queryCatalog')
    def queryCatalog(self, REQUEST=None, **kw):
        """Invoke the catalog using our criteria to augment any passed
            in query before calling the catalog.
        """
        q = self.buildQuery()
        if q is None:
            # empty query - do not show anything
            return []
        kw.update( q )
        print kw
        pcatalog = getToolByName( self, 'portal_catalog' )
        return pcatalog.searchResults(REQUEST, **kw)

    security.declareProtected(ChangeTopics, 'addCriterion')
    def addCriterion(self, field, criterion_type):
        """Add a new search criterion.
        """
        newid = 'crit__%s' % field
        ct    = CriterionRegistry[criterion_type]
        crit  = ct(newid, field)

        self._setObject( newid, crit )

    security.declareProtected(ChangeTopics, 'deleteCriterion')
    def deleteCriterion(self, criterion_id):
        """Delete selected criterion.
        """
        if type(criterion_id) is StringType:
            self._delObject(criterion_id)
        elif type(criterion_id) in (ListType, TupleType):
            for cid in criterion_id:
                self._delObject(cid)

    security.declareProtected(CMFCorePermissions.View, 'getCriterion')
    def getCriterion(self, criterion_id):
        """Get the criterion object.
        """
        try:
            return self._getOb('crit__%s' % criterion_id)
        except AttributeError:
            return self._getOb(criterion_id)

    security.declareProtected(AddTopics, 'addSubtopic')
    def addSubtopic(self, id):
        """Add a new subtopic.
        """
        ti = self.getTypeInfo()
        ti.constructInstance(self, id)
        return self._getOb( id )

registerType(ATTopic)