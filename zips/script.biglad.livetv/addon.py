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
    '[B][COLOR=gold]Open TV Guide[/COLOR][/B]' ,
    '[B][COLOR=green]UK Freeview[/COLOR][/B]',    
    '[B][COLOR=green]UK Freeview 2[/COLOR][/B]',
    '[B][COLOR=green]UK Freeview 3[/COLOR][/B]',
    '[B][COLOR=green]CA IPTV[/COLOR][/B]',
    '[B][COLOR=green]US IPTV (TAP)[/COLOR][/B]',
    '[B][COLOR=green]US IPTV (DL)[/COLOR][/B]',
    '[B][COLOR=green]US IPTV[/COLOR][/B]',
    '[B][COLOR=green]GLOBAL IPTV[/COLOR][/B]',
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
    xbmc.executebuiltin('RunAddon("script.ivueguide")')
    return
    
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.catchuptvandmore/resources/lib/main/tv_guide_menu/?_pickle_=80049540000000000000007d94288c075f7469746c655f948c0e556e69746564204b696e67646f6d948c08786d6c74765f6964944e8c076974656d5f6964948c07756b5f6c69766594752e",return)')
    return

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=UK%20FREEVIEW&url=https%3a%2f%2fraw.githubusercontent.com%2fbiglad%2ftvsetup%2fmain%2fconfig.m3u",return)')
    return
    
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=GITHUB&url=https%3a%2f%2fexperiencersinternational.github.io%2ftvsetup%2fconfig.m3u",return)')
    return
    
def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=CA%20IPTV%20-%20PLEX&url=https%3a%2f%2fi.mjh.nz%2fPlex%2fca.m3u8",return)')
    return
    
def function6():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.thetvapp/?image=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.thetvapp%5c%2fresources%2f..%2ficon.png&mode=listmovies&page=1&title=Live%20TV&url=https%3a%2f%2fthetvapp.to%2ftv",return)')
    return
    
def function7():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.daddylive/?mode=menu&serv_type=live_tv",return)')
    return
    
def function8():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=US%20IPTV%20-%20PLEX&url=https%3a%2f%2fi.mjh.nz%2fPlex%2fus.m3u8",return)')
    return
    
def function9():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.live.streamspro/?fanart=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.live.streamspro%5cfanart.jpg&mode=1&name=ENG&url=http%3a%2f%2fmgawow.ddns.net%2fm3u%2feng.m3u",return)')
    return
    

    
    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()