import time
import xbmc
import xbmcvfs
import os
import xbmcgui
import xbmcplugin
import urllib3
import utils
import sfile
import sys
import urllib
import requests
import xbmcaddon
import xbmcvfs
import re

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]MTV Music UK[/COLOR][/B]', [ 
    '[B][COLOR=gold]Stream 1[/COLOR][/B]' ,
    '[B][COLOR=gold]Stream 2[/COLOR][/B]',    
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-2]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistloader/?name=US%3A+MTV+Music&url=http%3A%2F%2Fkuchini.site%3A8080%2FGenIptvLast%2FcGW7qTY5txZ3DOfz%2F282262&mode=3&iconimage=&logos=&cache=0&uuid=0")')
    return
    
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F282262&mode=12")')
    return
    
menuoptions()