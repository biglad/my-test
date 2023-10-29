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
        function3,
        function4,
        function5
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]SyFy US[/COLOR][/B]', [ 
    '[B][COLOR=gold]Stream 1[/COLOR][/B]' ,   
    '[B][COLOR=gold]Stream 2[/COLOR][/B]',
    '[B][COLOR=gold]Stream 3[/COLOR][/B]',
    '[B][COLOR=gold]Stream 4[/COLOR][/B]',
    '[B][COLOR=gold]Stream 5[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-5]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone/play/221/play.pvr)")
    return

def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone111/play/1247/play.pvr)")
    return
    
def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.daddylive/?mode=play&url=https%3A%2F%2Fdaddylivehd.sx%2F%2Fstream%2Fstream-373.php)")
    return
    
def function4():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.taptv/play/221/play.pvr)")
    return
    
def function5():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.rbtv/play/1247/play.pvr)")
    return
    
    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()