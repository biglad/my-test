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
    '[B][COLOR=yellow]Clubland TV[/COLOR][/B]', [ 
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistloader/?name=UK%3A+Clubland+TV&url=http%3A%2F%2Fkuchini.site%3A8080%2Fiptvepic4%2FDzbGTtATy4DzmK8c%2F144752&mode=3&iconimage=&logos=&cache=0&uuid=0")')
    return
    
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistloader/?name=UK%3A+Clubland+TV&url=http%3A%2F%2Faflaxtv.xyz%3A8080%2FGiobox2%2FaPnVqQVT6GXhu92E%2F144752&mode=3&iconimage=http%3A%2F%2Fs3.i3ns.net%2Fportal%2Fpicon%2F2021-07%2Fa36da207ab4d49bd1e3d907a2a7331b2.png&logos=&cache=0&uuid=0")')
    return



menuoptions()