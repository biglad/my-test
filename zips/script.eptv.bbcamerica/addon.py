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
    '[B][COLOR=yellow]BBC America[/COLOR][/B]', [ 
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
        func = funcs[call-2]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.thetvapp/?mode=playvideo&url=https%3A%2F%2Fthetvapp.to%2Ftv%2Fbbc-america-live-stream%2F&page=1&title=BBC+America&image=C%3A%5CUsers%5Ckhanb%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.thetvapp%5C%2Fresources%2F..%2Ficon.png)")
    return

def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.thetvapp/?mode=playvideo&url=https%3A%2F%2Fthetvapp.to%2Ftv%2Fbbc-america-live-stream%2F&page=1&title=BBC+America&image=C%3A%5CUsers%5Ckhanb%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.thetvapp%5C%2Fresources%2F..%2Ficon.png)")
    return
    
def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.live.streamspro/?url=https%3A%2F%2Fbcovlive-a.akamaihd.net%2Fc9bf201b06694453bb29282f97191f58%2Fus-east-1%2F6240731308001%2Fplaylist.m3u8&mode=12&iconimage=https%3A%2F%2Fi.imgur.com%2FpTiiPz0.png)")
    return
    
    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()