"""Skeleton ATContentTypes tests

Use this file as a skeleton for your own tests

$Id: testATFolder.py,v 1.4 2004/06/13 21:49:19 tiran Exp $
"""

__author__ = 'Christian Heimes'
__docformat__ = 'restructuredtext'

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from common import *

def editCMF(obj):
    dcEdit(obj)

def editATCT(obj):
    dcEdit(obj)

tests = []

class TestSiteATFolder(ATCTSiteTestCase):

    klass = ATFolder.ATFolder
    portal_type = 'ATFolder'
    title = 'AT Folder'
    meta_type = 'ATFolder'
    icon = 'folder_icon.gif'

    def test_edit(self):
        old = self._cmf
        new = self._ATCT
        editCMF(old)
        editATCT(new)
        self.failUnless(old.Title() == new.Title(), 'Title mismatch: %s / %s' \
                        % (old.Title(), new.Title()))
        self.failUnless(old.Description() == new.Description(), 'Description mismatch: %s / %s' \
                        % (old.Description(), new.Description()))

    def test_migration(self):
        old = self._cmf
        id  = old.getId()
        
        # edit
        editCMF(old)
        title       = old.Title()
        description = old.Description()
        mod         = old.ModificationDate()
        created     = old.CreationDate()

        # migrated (needs subtransaction to work)
        get_transaction().commit(1)
        m = FolderMigrator(old)
        m(unittest=1)

        migrated = getattr(self._portal, id)

        self.compareAfterMigration(migrated)
        self.compareDC(migrated, title=title, description=description, mod=mod,
                       created=created)
                       
        # XXX more


    def beforeTearDown(self):
        del self._ATCT
        del self._cmf
        ATCTSiteTestCase.beforeTearDown(self)

tests.append(TestSiteATFolder)

class TestATFolderFields(ATCTFieldTestCase):

    def afterSetUp(self):
        ATCTFieldTestCase.afterSetUp(self)
        self._dummy = ATFolder.ATFolder(oid='dummy')
        self._dummy.initializeArchetype()
        # wrap dummy object in the acquisition context of the site
        site = self.getPortal()
        self._dummy = self._dummy.__of__(site)
        # more

    def test_somefield(self):
        # Test a field
        dummy = self._dummy
        field = dummy.getField('somefield')
        self.failUnless(1==1)

    def beforeTearDown(self):
        # more
        ATCTFieldTestCase.beforeTearDown(self)

tests.append(TestATFolderFields)

if __name__ == '__main__':
    framework()
else:
    # While framework.py provides its own test_suite()
    # method the testrunner utility does not.
    import unittest
    def test_suite():
        suite = unittest.TestSuite()
        for test in tests:
            suite.addTest(unittest.makeSuite(test))
        return suite
