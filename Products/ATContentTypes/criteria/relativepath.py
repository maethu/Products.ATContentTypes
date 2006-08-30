#  ATContentTypes http://sf.net/projects/collective/
#  Archetypes reimplementation of the CMF core types
#  Copyright (c) 2003-2005 AT Content Types development team
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
""" Topic:

"""

__author__  = 'Alec Mitchell'
__docformat__ = 'restructuredtext'
# __old_name__ = 'Products.ATContentTypes.types.criteria.ATPathCriterion'

from Products.CMFCore.permissions import View
from AccessControl import ClassSecurityInfo

from Products.Archetypes.public import Schema, DisplayList
from Products.Archetypes.public import BooleanField, StringField
from Products.Archetypes.public import BooleanWidget, SelectionWidget, StringWidget
from Products.Archetypes.Referenceable import Referenceable

from Products.ATContentTypes.criteria import registerCriterion
from Products.ATContentTypes.criteria import PATH_INDICES
from Products.ATContentTypes.interfaces import IATTopicSearchCriterion
from Products.ATContentTypes.permission import ChangeTopics
from Products.ATContentTypes.criteria.base import ATBaseCriterion
from Products.ATContentTypes.criteria.schemata import ATBaseCriterionSchema

ATRelativePathCriterionSchema = ATBaseCriterionSchema + Schema((
    StringField('relativePath',
                vocabulary=DisplayList( (('currentfolder', 'Current folder'), ('parentfolder','Parent folder'), ('custompath','Custom relative path'))),
                widget=SelectionWidget(label='Relative path', 
                                       label_msgid="label_relativepath_criteria_relativepath",
                                       description_msgid="help_relativepath_criteria_relativepath",
                                       i18n_domain="plone",
                                       description=''),
                default='currentfolder'),
    StringField('customRelativePath',
                widget=StringWidget(label='Custom relative path', 
                                    label_msgid="label_relativepath_criteria_customrelativepath",
                                    description_msgid="help_relativepath_criteria_customrelativepath",
                                    i18n_domain="plone",
                                    description='Enter a relative path, relative to the current location e.g. ../../somefolder')),
    BooleanField('recurse',
                mode="rw",
                write_permission=ChangeTopics,
                accessor="Recurse",
                default=False,
                widget=BooleanWidget(
                    label="Search Sub-Folders",
                    label_msgid="label_path_criteria_recurse",
                    description="",
                    description_msgid="help_path_criteria_recurse",
                    i18n_domain="plone"),
                ),
    ))

class ATRelativePathCriterion(ATBaseCriterion):
    """A path criterion"""

    __implements__ = ATBaseCriterion.__implements__ + (IATTopicSearchCriterion, )
    security       = ClassSecurityInfo()
    schema         = ATRelativePathCriterionSchema
    meta_type      = 'ATRelativePathCriterion'
    archetype_name = 'Relative Path Criterion'
    typeDescription= ''
    typeDescMsgId  = ''

    shortDesc      = 'Relative Location in site'

    def getNavTypes(self):
        ptool = self.plone_utils
        nav_types = ptool.typesToList()
        return nav_types

    security.declareProtected(View, 'getCriteriaItems')
    def getCriteriaItems(self):
        #result = []
        #depth = (not self.Recurse() and 1) or -1
        #paths = ['/'.join(o.getPhysicalPath()) for o in self.Value()]

        #if paths is not '':
            #result.append((self.Field(), {'query': paths, 'depth': depth}))

        #return tuple( result )
        return 


registerCriterion(ATRelativePathCriterion, PATH_INDICES)
