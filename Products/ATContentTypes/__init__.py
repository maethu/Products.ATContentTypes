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

$Id: __init__.py,v 1.1 2004/03/08 10:48:40 tiran Exp $
""" 
__author__  = ''
__docformat__ = 'restructuredtext'

from Globals import package_home
from Products.CMFCore import utils
from Products.CMFCore import CMFCorePermissions
from Products.Archetypes.public import *
from Products.CMFCore.DirectoryView import registerDirectory

from config import *
import migration
import Validators
from interfaces.IATTopic import IATTopic, IATTopicCriterion

registerDirectory(SKINS_DIR,GLOBALS)

def initialize(context):
    # process our custom types
    import ATContentTypes
    
    listOfTypes = listTypes(PROJECTNAME)
    
    content_types, constructors, ftis = process_types(
        listOfTypes,
        PROJECTNAME)

    # A brief explanation for the following code:
    #
    # We want to have another add permission for the topic and criteria because
    # topics shouldn't be addable by non managers. The following code iterats
    # over all content types and seperates the content_types using the
    # interfaces. At last it initializes topic/criteria and the rest with two
    # different permissions.

    topic_content_types = []
    topic_constructors  = []
    other_content_types = []
    other_constructors  = []

    for i in range(len(listOfTypes)):
        aType = listOfTypes[i]
        if IATTopic.isImplementedByInstancesOf(aType['klass']) or \
          IATTopicCriterion.isImplementedByInstancesOf(aType['klass']):
            topic_content_types.append(content_types[i])
            topic_constructors.append(constructors[i])
        else:
            other_content_types.append(content_types[i])
            other_constructors.append(constructors[i])

    # other
    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types = tuple(other_content_types),
        permission = ADD_CONTENT_PERMISSION,
        extra_constructors = tuple(other_constructors),
        fti = ftis,
        ).initialize(context)

    # topics
    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types = tuple(topic_content_types),
        permission = ADD_TOPIC_PERMISSION,
        extra_constructors = tuple(topic_constructors),
        fti = ftis,
        ).initialize(context)