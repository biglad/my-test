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
        function5,
        function6
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]FreeForm[/COLOR][/B]', [ 
    '[B][COLOR=gold]Stream 1[/COLOR][/B]' ,
    '[B][COLOR=gold]Stream 2[/COLOR][/B]',    
    '[B][COLOR=gold]Stream 3[/COLOR][/B]',
    '[B][COLOR=gold]Stream 4[/COLOR][/B]',
    '[B][COLOR=gold]Stream 5[/COLOR][/B]',
    '[B][COLOR=gold]Stream 6[/COLOR][/B]',

    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-6]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone1112/play/1305/play.pvr")')
    return
    
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone111/play/1293/play.pvr")')
    return

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone/play/675/play.pvr")')
    return
    
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.daddylive/?mode=play&amp;url=https%3A%2F%2Fdaddylivehd.sx%2F%2Fstream%2Fstream-301.php")')
    return
    
def function5():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.thetvapp/?mode=playvideo&amp;url=https%3A%2F%2Fthetvapp.to%2Ftv%2Ffreeform-live-stream%2F&amp;page=1&amp;title=Freeform&amp;image=C%3A%5CUsers%5Ckhanb%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.thetvapp%5C%2Fresources%2F..%2Ficon.png")')
    return
    
def function6():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F2329&amp;mode=12")')
    return
    
    
menuoptions()