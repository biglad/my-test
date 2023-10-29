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
    '[B][COLOR=yellow]Sky 1 / Showcase[/COLOR][/B]', [ 
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
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F1080&mode=12)")
    return
    
def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone/play/189/play.pvr)")
    return
    
def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=UK%7C+SKY+SHOWCASE+FHD&url=http%3A%2F%2Fline.rs6ott.com%3A80%2FAndreas%2FAndreas%2F741952&mode=3&iconimage=http%3A%2F%2Flogo.protv.cc%2Fpicons%2Flogos%2FSKY-SHOWCASE.png&logos=&cache=0&uuid=0)")
    return
 
def function4():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.daddylive/?mode=play&url=https%3A%2F%2Fdaddylivehd.sx%2F%2Fstream%2Fstream-682.php)")
    return


    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()