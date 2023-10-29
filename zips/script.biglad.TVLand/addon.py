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
        function2,
        function3
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]TV Land[/COLOR][/B]', [ 
    '[B][COLOR=gold]Stream 1[/COLOR][/B]' ,
    '[B][COLOR=gold]Stream 2[/COLOR][/B]',    
    '[B][COLOR=gold]Stream 3[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.daddylive/?mode=play&url=https%3A%2F%2Fdaddylivehd.sx%2F%2Fstream%2Fstream-342.php")')
    return
    
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F2364&mode=12")')
    return

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistloader/?name=US%3A+TV+Land&url=http%3A%2F%2Fkuchini.site%3A8080%2FGenIptvLast%2FcGW7qTY5txZ3DOfz%2F2364&mode=3&iconimage=&logos=&cache=0&uuid=0")')
    return
     
menuoptions()