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
    '[B][COLOR=yellow]Horror Extra[/COLOR][/B]', [ 
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
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.live.streamspro/?url=http%3A%2F%2Fkuchini.site%3A8080%2Fgoogleiptvex%2F8XsdD8qVstQhcjuy%2F736&mode=12)")
    return

def function2():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=UK%3A+Horror+Channel&url=http%3A%2F%2Fkuchini.site%3A8080%2FGenIptvLast%2FcGW7qTY5txZ3DOfz%2F736&mode=3&iconimage=&logos=&cache=0&uuid=0)")
    return
    
def function3():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=%5BSD%5DHorror+Channel&url=https%3A%2F%2Fepg.pw%2Fstream%2Ff8c0b61142c4b19521b21da2a7491de296fe69e9bc18b069339056c0f063c913.ctv&mode=3&iconimage=https%3A%2F%2Fepg.pw%2Fmedia%2Fuploads%2Ftmp_logo%2F2015%2F02%2F11%2F20150211201322771605_15.jpg&logos=&cache=0&uuid=0")
    return
    
def function4():
    xbmc.executebuiltin("PlayMedia(plugin://plugin.video.playlistloader/?name=%5BSD%5DHorror+Channel%5Bgeo-blocked%5D&url=https%3A%2F%2Fepg.pw%2Fstream%2Fac1ebd65473f571cbfa7521a20c24d41074b8c29ee2ef3e9cd2bf02bfeb46e7d.ctv&mode=3&iconimage=https%3A%2F%2Fepg.pw%2Fmedia%2Fuploads%2Ftmp_logo%2F2015%2F02%2F11%2F20150211201322771605_15.jpg&logos=&cache=0&uuid=0)")
    return
    
    #PlayMedia(plugin://plugin.video.tvone/play/66/play.pvr)
    
    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')


menuoptions()