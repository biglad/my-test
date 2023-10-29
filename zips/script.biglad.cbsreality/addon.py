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
    '[B][COLOR=yellow]Live TV[/COLOR][/B]', [ 
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
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F1121&mode=12")')
    return
    
def function2():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone111/play/1359/play.pvr")')
    return

def function3():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.tvone1112/play/242/play.pvr")')
    return
    
def function4():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fwww.premiumiptvmk.com%3A8080%2Fmyhdosama%2FcjydA4ncmMqx55pf%2F1121&mode=12")')
    return
    
def function5():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.rbtv/play/1325/play.pvr")')
    return
    
def function6():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.lntv/play/242/play.pvr")')
    return
    
def function7():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistloader/?name=UK%3A+CBS+Reality&url=http%3A%2F%2Fwww.premiumiptvmk.com%3A8080%2Fmyhdosama%2FcjydA4ncmMqx55pf%2F1121&mode=3&iconimage=&logos=&cache=0&uuid=0")')
    return
    
def function8():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistloader/?name=%7C.UK.%7C+CBS+REALITY&url=http%3A%2F%2Fpro.xviptv.com%3A25443%2Flive%2FHAJG6%2Fk7bKPqg05y%2F30910.ts&mode=3&iconimage=&logos=&cache=0&uuid=0")')
    return
    
def function9():
    xbmc.executebuiltin('PlayMedia("plugin://plugin.video.playlistloader/?name=UK%3A+CBS+Reality&amp;url=http%3A%2F%2Fkuchini.site%3A8080%2FGenIptvLast%2FcGW7qTY5txZ3DOfz%2F1121&amp;mode=3&amp;iconimage=&amp;logos=&amp;cache=0&amp;uuid=0")')
    return
    
menuoptions()