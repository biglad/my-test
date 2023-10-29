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
        function7
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]Comedy Central USA[/COLOR][/B]', [ 
    '[B][COLOR=gold]Stream 1[/COLOR][/B]' ,   
    '[B][COLOR=gold]Stream 2[/COLOR][/B]',
    '[B][COLOR=gold]Stream 3[/COLOR][/B]',
    '[B][COLOR=gold]Stream 4[/COLOR][/B]',
    '[B][COLOR=gold]Stream 5[/COLOR][/B]',
    '[B][COLOR=gold]Stream 6[/COLOR][/B]',
    '[B][COLOR=gold]Stream 7[/COLOR][/B]',
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-7]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone111/play/1272/play.pvr)")
    return

def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.thetvapp/?mode=playvideo&url=https%3A%2F%2Fthetvapp.to%2Ftv%2Fcomedy-central-live-stream%2F&page=1&title=Comedy+Central&image=C%3A%5CUsers%5Ckhanb%5CAppData%5CRoaming%5CKodi%5Caddons%5Cplugin.video.thetvapp%5C%2Fresources%2F..%2Ficon.png)")
    return
    
def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=%5BHD%5DCOMEDY+CENTRAL+USA%5Bgeo-blocked%5D&url=https%3A%2F%2Fepg.pw%2Fstream%2Ff32690de3da317a9feb2e67250e1eea5d1d43eaa01f60edbf9f04be6759a7713.ctv&mode=3&iconimage=https%3A%2F%2Fepg.pw%2Fmedia%2Fimages%2Fchannel%2F2019%2F01%2F21%2Flarge%2F20190121235737341364_51.jpg&logos=&cache=0&uuid=0)")
    return
    
def function4():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F754&mode=12)")
    return
    
def function5():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone/play/85/play.pvr)")
    return
    
def function6():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.daddylive/?mode=play&url=https%3A%2F%2Fdaddylivehd.sx%2F%2Fstream%2Fstream-310.php)")
    return
    
def function7():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone1112/play/267/play.pvr)")
    return
    
    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()