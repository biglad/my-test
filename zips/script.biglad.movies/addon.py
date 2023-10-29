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
    '[B][COLOR=yellow]Movies[/COLOR][/B]', [ 
    '[B][COLOR=gold]The Promise[/COLOR][/B]' ,
    '[B][COLOR=gold]The Crew[/COLOR][/B]',    
    '[B][COLOR=gold]Shadow[/COLOR][/B]',
    '[B][COLOR=gold]Dynasty[/COLOR][/B]',
    '[B][COLOR=gold]Artemis[/COLOR][/B]',
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



    
def function1():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.thepromise/?action=movieNavigator",return)')
    return
    
def function2():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.thecrew/?action=movieNavigator",return))')
    return

def function3():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.shadow/?all_w=%7b%7d&data=%20&dates=%20&description=Movies&eng_name=%20&episode=%20&fanart=https%3a%2f%2ftownsquare.media%2fsite%2f295%2ffiles%2f2019%2f12%2f2020-movies-collage.jpg%3fw%3d980%26q%3d75&fav_status=false&heb_name=%20&iconimage=C%3a%5cUsers%5ckhanb%5cAppData%5cRoaming%5cKodi%5caddons%5cplugin.video.shadow%5cresources%5cartwork%2fmovies.png&id=%20&image_master&isr=0&last_id&mode=2&mypass&name=Movie%20World&original_title=%20&search_db&season=%20&show_original_year=%20&tmdbid=%20&url=www&video_data=%7b%22title%22%3a%20%22Movie%20World%22%2c%20%22mediatype%22%3a%20%22movie%22%2c%20%22TVshowtitle%22%3a%20%22%22%2c%20%22season%22%3a%200%2c%20%22episode%22%3a%200%2c%20%22OriginalTitle%22%3a%20%22%20%22%2c%20%22rating%22%3a%20%220%22%2c%20%22plot%22%3a%20%22Movies%22%2c%20%22Tag%22%3a%20%22None%22%2c%20%22id%22%3a%20%22%20%22%7d",return)')
    return
    
def function5():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.artemis/?action=movieNavigator",return))')
    return
    
def function4():
    xbmc.executebuiltin('ActivateWindow(10025,"plugin://plugin.video.dynasty/?action=movieNavigator",return))')
    return
    
menuoptions()