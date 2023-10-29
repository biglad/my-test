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
        function6,
        function7,
        function8,
        function9
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]VH1 US[/COLOR][/B]', [ 
    '[B][COLOR=gold]Stream 1[/COLOR][/B]' ,
    '[B][COLOR=gold]Stream 2[/COLOR][/B]',    
    '[B][COLOR=gold]Stream 3[/COLOR][/B]',
    '[B][COLOR=gold]Stream 4[/COLOR][/B]',
    '[B][COLOR=gold]Stream 5[/COLOR][/B]',
    '[B][COLOR=gold]Stream 6[/COLOR][/B]',
    '[B][COLOR=gold]Stream 7[/COLOR][/B]',
    '[B][COLOR=gold]Stream 8[/COLOR][/B]',
    '[B][COLOR=gold]Stream 9[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-9]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.daddylive/?mode=play&url=https%3A%2F%2Fdaddylivehd.sx%2F%2Fstream%2Fstream-344.php")')
    return
    
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.thetvapp/?mode=playvideo&url=https%3A%2F%2Fthetvapp.to%2Ftv%2Fvh1-live-stream%2F&page=1&title=VH1&image=C%3A%5CUsers%5Ckhanb%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.thetvapp%5C%2Fresources%2F..%2Ficon.png")')
    return

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F2370&mode=12")')
    return
    
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.lntv/play/394/play.pvr")')
    return
    
def function5():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.taptv/play/607/play.pvr")')
    return
    
def function6():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone/play/607/play.pvr")')
    return
    
def function7():
    xbmc.executebuiltin('PlayMedia("lugin://plugin.video.tvone1112/play/394/play.pvr")')
    return
    
def function8():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.rbtv/play/1289/play.pvr")')
    return
    
def function9():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone111/play/1289/play.pvr")')
    return
    
menuoptions()