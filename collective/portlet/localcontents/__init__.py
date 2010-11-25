# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
LocalContentsMessageFactory = MessageFactory('collective.portlet.localcontents')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
