# -*- coding: UTF-8 -*-
from Plugins.Plugin import PluginDescriptor
from importlib import reload
from . import zdf


def main(session, **kwargs):
	reload(zdf)
	session.open(zdf.ZDFMediathek)


def Plugins(**kwargs):
	return PluginDescriptor(name="ZDF Mediathek", description="ZDF Mediathek Plugin für Enigma2", where=[PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU], icon="logo.png", fnc=main)
