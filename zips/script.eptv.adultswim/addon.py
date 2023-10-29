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
    '[B][COLOR=yellow]Adult Swim[/COLOR][/B]', [ 
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
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.daddylive/?mode=play&url=https%3A%2F%2Fdaddylivehd.sx%2F%2Fstream%2Fstream-295.php)")
    return
    
def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fmyserveriptv.com%3A2082%2F7wOd6fH332c1%2F8Skfy98Fd74f%2F135310&mode=12)")
    return

def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=CA%3A+Adult+Swim&url=http%3A%2F%2Fwww.premiumiptvmk.com%3A8080%2Fsilversatcom%2FJ662bwtY7Tev877u%2F9218&mode=3&iconimage=http%3A%2F%2Fs3.i3ns.net%2Fportal%2Fpicon%2F2021-05%2Fd5c58112babfd62f5385d2340fbea818.png&logos=&cache=0&uuid=0)")
    return
    
def function4():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=%7CCA%7C+Adult+Swim&url=http%3A%2F%2Fpro.xviptv.com%3A25443%2Flive%2FHAJG6%2Fk7bKPqg05y%2F141115.ts&mode=3&iconimage=&logos=&cache=0&uuid=0)")
    return
    
def function5():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fnew-pro.tv%3A8080%2F99622282%2FetbVXafU6f%2F302914&mode=12)")
    return
    
def function6():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F9218&mode=12)")
    return
    
    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()