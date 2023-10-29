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
    '[B][COLOR=yellow]CTV Sci-Fi Canada[/COLOR][/B]', [ 
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



    
def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=CA%3A+CTV+sci-fi&url=http%3A%2F%2Fwww.premiumiptvmk.com%3A8080%2Fsilversatcom%2FJ662bwtY7Tev877u%2F60157&mode=3&iconimage=http%3A%2F%2Fs3.i3ns.net%2Fportal%2Fpicon%2F2021-05%2Fb0de99132f443e1a81aa2b565cd58243.png&logos=&cache=0&uuid=0)")
    return

def function5():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=CA%3A+CTV+sci-fi&url=http%3A%2F%2Fkuchini.site%3A8080%2FGenIptvLast%2FcGW7qTY5txZ3DOfz%2F60157&mode=3&iconimage=&logos=&cache=0&uuid=0)")
    return
    
def function4():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=%7CCA%7C+CTV+sci-fi&url=http%3A%2F%2Fpro.xviptv.com%3A25443%2Flive%2FHAJG6%2Fk7bKPqg05y%2F141161.ts&mode=3&iconimage=&logos=&cache=0&uuid=0)")
    return
    
def function1():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone112/play/145/2397/play.pvr)")
    return
    
def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.tvone1112/play/1933/play.pvr)")
    return
    
    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()