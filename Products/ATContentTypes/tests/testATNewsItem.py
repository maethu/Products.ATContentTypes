"""Skeleton ATContentTypes tests

Use this file as a skeleton for your own tests

$Id: testATNewsItem.py,v 1.1 2004/03/08 10:48:41 tiran Exp $
"""

__author__ = 'Christian Heimes'
__docformat__ = 'restructuredtext'

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from common import *

tests = []

class TestATNewsItem(ATCTTestCase):

    def afterSetUp(self):
        ATCTTestCase.afterSetUp(self)
        self._dummy = ATNewsItem.ATNewsItem(oid='dummy')
        self._dummy.initializeArchetype()

    def testSomething(self):
        # Test something
        self.failUnless(1==1)

    def beforeTearDown(self):
        del self._dummy
        ATCTTestCase.beforeTearDown(self)

tests.append(TestATNewsItem)

class TestSiteATNewsItem(ATCTSiteTestCase):

    def afterSetUp(self):
        ATCTSiteTestCase.afterSetUp(self)
        self._portal = self.app.portal
        ATCT = ATNewsItem.ATNewsItem(oid='ATCT')
        ATCT.initializeArchetype()
        self._portal._setObject('ATCT', ATCT)
        self._ATCT = getattr(self._portal, 'ATCT')

        cmf = NewsItem.NewsItem(id='cmf')
        self._portal._setObject('cmf', cmf)
        self._cmf = getattr(self._portal, 'cmf')

    def testTypeInfo(self):
        ti = self._ATCT.getTypeInfo()
        self.failUnless(ti.getId() == 'ATNewsItem', ti.getId())
        self.failUnless(ti.Title() == 'AT News Item', ti.Title())
        #self.failUnless(ti.getIcon() == 'newsitem_icon.gif', ti.getIcon())
        self.failUnless(ti.Metatype() == 'ATNewsItem', ti.Metatype())

    def beforeTearDown(self):
        del self._ATCT
        del self._cmf
        ATCTSiteTestCase.beforeTearDown(self)

tests.append(TestSiteATNewsItem)

class TestATNewsItemFields(ATCTFieldTestCase):

    def afterSetUp(self):
        ATCTTestCase.afterSetUp(self)
        self._dummy = ATNewsItem.ATNewsItem(oid='dummy')
        self._dummy.initializeArchetype()
        # more

    def test_textField(self):
        dummy = self._dummy
        field = dummy.getField('text')

        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.required == 0, 'Value is %s' % field.required)
        self.failUnless(field.default == '', 'Value is %s' % str(field.default))
        self.failUnless(field.searchable == 1, 'Value is %s' % field.searchable)
        self.failUnless(field.vocabulary == (), 
                        'Value is %s' % str(field.vocabulary))
        self.failUnless(field.enforceVocabulary == 0, 
                        'Value is %s' % field.enforceVocabulary)
        self.failUnless(field.multiValued == 0,
                        'Value is %s' % field.multiValued)
        self.failUnless(field.isMetadata == 0, 'Value is %s' % field.isMetadata)
        self.failUnless(field.accessor == 'getText',
                        'Value is %s' % field.accessor)
        self.failUnless(field.mutator == 'setText',
                        'Value is %s' % field.mutator)
        self.failUnless(field.read_permission == CMFCorePermissions.View,
                        'Value is %s' % field.read_permission)
        self.failUnless(field.write_permission ==
                        CMFCorePermissions.ModifyPortalContent,
                        'Value is %s' % field.write_permission)
        self.failUnless(field.generateMode == 'veVc',
                        'Value is %s' % field.generateMode)
        self.failUnless(field.force == '', 'Value is %s' % field.force)
        self.failUnless(field.type == 'text', 'Value is %s' % field.type)
        self.failUnless(isinstance(field.storage, AttributeStorage),
                        'Value is %s' % type(field.storage))
        self.failUnless(field.getLayerImpl('storage') == AttributeStorage(),
                        'Value is %s' % field.getLayerImpl('storage'))
        self.failUnless(ILayerContainer.isImplementedBy(field))
        self.failUnless(field.validators == (),
                        'Value is %s' % str(field.validators))
        self.failUnless(isinstance(field.widget, RichWidget),
                        'Value is %s' % id(field.widget))
        vocab = field.Vocabulary(dummy)
        self.failUnless(isinstance(vocab, DisplayList),
                        'Value is %s' % type(vocab))
        self.failUnless(tuple(vocab) == (), 'Value is %s' % str(tuple(vocab)))
        
        self.failUnless(field.primary == 1, 'Value is %s' % field.primary)
        self.failUnless(field.default_content_type == 'text/structured',
                        'Value is %s' % field.default_content_type)
        self.failUnless(field.default_output_type == 'text/html',
                        'Value is %s' % field.default_output_type)
        self.failUnless(field.allowable_content_types == ('text/structured',
                        'text/restructured', 'text/html', 'text/plain'),
                        'Value is %s' % str(field.allowable_content_types))

    def beforeTearDown(self):
        # more
        del self._dummy
        ATCTTestCase.beforeTearDown(self)

tests.append(TestATNewsItemFields)

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