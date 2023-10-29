import time
import xbmc
import xbmcvfs
import os
import xbmcgui
#import urllib2
import utils
import sfile

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3
        )
        
    call = dialog.select(
    '[B][COLOR=yellow]Exit[/COLOR][/B]', [ 
    '[B][COLOR=gold]Close Kodi[/COLOR][/B]' ,   
    '[B][COLOR=gold]Close & Run House Keeper.[/COLOR][/B]',
    '[B][COLOR=gold]Remove "inputstream.adaptive" and close[/COLOR][/B]',

    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-3]
        return func()
    else:
        func = funcs[call]
        return func()
    return 



    
def function1():
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    os._exit(1)
    exit()
        
def function3():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR gold]House Keeper[/COLOR]","Working.....")
    xbmc.sleep(1000)
    dp.update(10)
    CACHE    = xbmcvfs.translatePath('special://home/cache/')
    thumbs     = xbmcvfs.translatePath('special://home/userdata/Thumbnails/')
    TEMP = xbmcvfs.translatePath('special://home/addons/Thumbnails/temp/')
    PACKS = xbmcvfs.translatePath('special://home/addons/Thumbnails/packages/')
    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/inputstream.adaptive/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    xbmc.sleep(1000)
    dp.update(20)
    try: sfile.rmtree(CACHE)
    except: pass
    xbmc.sleep(1000)
    dp.update(30)
    try: sfile.rmtree(thumbs)
    except: pass
    xbmc.sleep(1000)
    dp.update(40)
    try: sfile.rmtree(TEMP)
    except: pass
    xbmc.sleep(1000)
    dp.update(50)
    try: sfile.rmtree(PACKS)
    except: pass
    xbmc.sleep(1000)
    dp.update(60)
    xbmc.sleep(1000)
    dp.create("[COLOR gold]House Keeper[/COLOR]","DONE, CLOSING KODI.....")
    xbmc.sleep(1000)
    xbmc.executebuiltin("Action(Close)")
    os._exit(1)
    exit()
    
def function2():



    import os
    import xbmc,xbmcaddon,subprocess
    #import urlparse
    import xbmcgui
    import sfile
    dp = xbmcgui.DialogProgress()
    dialog = xbmcgui.Dialog()
    dp.create("[COLOR gold]House Keeper[/COLOR]","Removing temp /old files")
    xbmc.sleep(2000)
    dp.update(10)




    #CACHE
    CACHE    = xbmcvfs.translatePath('special://home/cache/')
    #FILES
    MZip     = xbmcvfs.translatePath('special://home/_mega_temp.zip')
    MZip2     = xbmcvfs.translatePath('special://home/userdata/install.zip')
    MZip3     = xbmcvfs.translatePath('special://home/userdata/install2.zip')
    MZip4     = xbmcvfs.translatePath('special://home/userdata/install3.zip')
    MZip5     = xbmcvfs.translatePath('special://home/menu.zip')
    MZip6     = xbmcvfs.translatePath('special://home/uk.zip')
    MZip9     = xbmcvfs.translatePath('special://home/userdata/Database/Epg12.db')
    #THUMBS
    thumbs     = xbmcvfs.translatePath('special://home/userdata/Thumbnails/')




    try: sfile.rmtree(CACHE)
    except: pass
    try: sfile.rmtree(thumbs)
    except: pass

    #TV GUIDE DATA
    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatv/vistatv.xml"))
    except: pass
    dp.update(20)
    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatv/source.db"))
    except: pass

    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatvusa/vistatvusa.xml"))
    except: pass
    dp.update(25)
    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatvusa/source.db"))
    except: pass

    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatvkids/vistatvkids.xml"))
    except: pass
    dp.update(30)
    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatvkids/source.db"))
    except: pass

    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatvsport/vistatvsport.xml"))
    except: pass
    dp.update(35)
    try: os.remove(xbmcvfs.translatePath("special://userdata/addon_data/script.tvguide.vistatvsport/source.db"))
    except: pass


    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/plugin.video.cattv.tva/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(40)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.module.theunjudged/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(41)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.module.theunjudged.iptv/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(42)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.module.theunjudged.live.nettv/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(43)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.module.theunjudged.scraper/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(44)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.module.theunjudged.uktv.now/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(45)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.module.underdogscrapers/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(46)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.tvguide.vistatvkids/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(49)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.tvguide.vistatvsport/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(51)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/script.tvguide.vistatvusa/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(55)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/cache/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(60)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.jesusboxtv/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(61)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.pluto/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(62)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.vista/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(63)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.ukturk/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(64)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.PureRepo/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(65)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.zt/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(66)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.maverickrepo/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(67)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.steptoes/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(68)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.wod/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(69)

    oldordeadaddon     = xbmcvfs.translatePath('special://home/addons/repository.x-odi.nl/')
    try: sfile.rmtree(oldordeadaddon)
    except: pass
    dp.update(70)
    


    try: os.remove(MZip9)
    except: pass
    try: os.remove(MZip)
    except: pass
    dp.update(72)
    try: os.remove(MZip2)
    except: pass
    dp.update(73)
    try: os.remove(MZip3)
    except: pass
    dp.update(75)
    try: os.remove(MZip4)
    except: pass
    dp.update(77)
    try: os.remove(MZip5)
    except: pass
    try: os.remove(MZip6)
    except: pass
    dp.update(80)


    origfolder = (xbmcvfs.translatePath("special://home/addons"))      
    def CleanPYO():
        count = 0
        for (dirname, dirs, files) in os.walk(origfolder):
           for filename in files:
               if filename.endswith('.pyo') :
                   os.remove(os.path.join(dirname, filename))


     
    CleanPYO() 
    
    
    origfolder = (xbmcvfs.translatePath("special://home/"))      
    def CleanPYO2():
        count = 0
        for (dirname, dirs, files) in os.walk(origfolder):
           for filename in files:
               if filename.endswith('.strm') :
                   os.remove(os.path.join(dirname, filename))


     
    CleanPYO2() 
    
    
    
    
    
    
    



    #update = xbmcgui.Dialog().yesno("[COLOR tomato]CerebroTV House Keeper[/COLOR]","[COLOR yellow]All none needed files have been removed[/COLOR]","[COLOR turquoise]This will speed up your box[/COLOR]" ,"[COLOR turquoise]A ReStart is now needed[/COLOR]")
    #if update:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    #else:
    #    xbmc.executebuiltin('RunAddon(script.program.exitkodi)')
    dp.update(80)
    xbmc.sleep(1000)
    dp.update(100)
    dp.close()
    dp.create("[COLOR gold]House Keeper[/COLOR]","Closing Kodi")
    dp.update(100)
    xbmc.sleep(3000)
    os._exit(1)









          
menuoptions()