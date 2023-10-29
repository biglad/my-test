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
        function4
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]FXX[/COLOR][/B]', [ 
    '[B][COLOR=gold]Stream 1[/COLOR][/B]' ,   
    '[B][COLOR=gold]Stream 2[/COLOR][/B]',
    '[B][COLOR=gold]Stream 3[/COLOR][/B]',
    '[B][COLOR=gold]Stream 4[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.thetvapp/?mode=playvideo&url=https%3A%2F%2Fthetvapp.to%2Ftv%2Ffxx-live-stream%2F&page=1&title=FXX&image=C%3A%5CUsers%5Ckhanb%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.thetvapp%5C%2Fresources%2F..%2Ficon.png)")
    return

def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.daddylive/?mode=play&url=https://daddylivehd.sx//stream/stream-298.php)")
    return
    
def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone111/play/1287/play.pvr)")
    return
    
def function4():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=US%3A+FXX&url=http%3A%2F%2Fiptvch.com%3A2082%2F7wOd6fH332c1%2F8Skfy98Fd74f%2F32309&mode=3&iconimage=&logos=&cache=0&uuid=0)")
    return
    
menuoptions()