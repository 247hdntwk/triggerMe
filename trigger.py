import urllib.request
import urllib.parse
import urllib.error
import re
import http.cookiejar
import string
import os
import random
import time
import datetime
import sys
import base64
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

addon_id = 'plugin.video.247hd'
artpath = xbmc.translatePath(os.path.join(
    'special://home/addons/' + addon_id + '/resources/'))
xmlpath = xbmc.translatePath(os.path.join(
    'special://home/addons/' + addon_id + '/addon.xml'))
final = base64.b64decode
ADDON = xbmcaddon.Addon(id=final(b"cGx1Z2luLnZpZGVvLjI0N2hk").decode('utf-8'))
selfAddon = xbmcaddon.Addon(id=addon_id)
prettyName = final(b'MjQ3SEQ=').decode('utf-8')
fanart = xbmc.translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(
    'special://home/addons/' + addon_id, 'icon.jpg'))
art = xbmc.translatePath(os.path.join(final(
    b'c3BlY2lhbDovL2hvbWUvYWRkb25zL3BsdWdpbi52aWRlby4yNDdoZC9yZXNvdXJjZXMvYXJ0').decode('utf-8'), ''))
datapath = xbmc.translatePath(selfAddon.getAddonInfo('profile'))
UpdatePath = os.path.join(datapath, 'Update')
cookiedir = os.path.join(os.path.join(datapath, 'Cookies'))
cookie_file = os.path.join(os.path.join(datapath, 'Cookies'), '247hd.cookies')

logfile = open(xmlpath, 'r').read()
match = re.findall(
    final(b'bmFtZT0iMjQ3SEQudHYiIHZlcnNpb249IiguKz8pIg==').decode('utf-8'), logfile)
if match:
    for n in match:
        VERSION = n.replace('.', '')
try:
    os.makedirs(UpdatePath)
except:
    pass

try:
    os.makedirs(cookiedir)
except:
    pass


def OPENURL(url, mobile=False, q=False, verbose=True, timeout=10, cookie=None, data=None,
            cookiejar=False, log=True, headers=[], types='', ua=False, setCookie=[], raiseErrors=False, ignore_discard=True):
    import urllib.request
    import urllib.error
    import urllib.parse
    UserAgent = final(
        b'TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgNi4xOyBXT1c2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzM0LjAuMTg0Ny4xMzEgU2FmYXJpLzUzNy4zNg==').decode('utf-8')
    if ua:
        UserAgent = ua
    try:
        if log:
            print("Openurl = " + url)
        if cookie and not cookiejar:
            import http.cookiejar
            cookie_file = os.path.join(os.path.join(
                datapath, 'Cookies'), cookie+'.cookies')
            cj = http.cookiejar.LWPCookieJar()
            if os.path.exists(cookie_file):
                try:
                    cj.load(cookie_file, ignore_discard)
                    for c in setCookie:
                        cj.set_cookie(c)
                except:
                    cj.save(cookie_file, True)
            else:
                cj.save(cookie_file, True)
            opener = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(cj))
        elif cookiejar:
            import http.cookiejar
            cj = http.cookiejar.LWPCookieJar()
            opener = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(cj))
        else:
            opener = urllib.request.build_opener()
        if mobile:
            opener.addheaders = [
                ('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')]
        else:
            opener.addheaders = [('User-Agent', UserAgent)]
        for header in headers:
            opener.addheaders.append(header)
        if data:
            if types == 'json':
                import json
                data = str.encode(json.dumps(data))
                opener.addheaders.append(('Content-Type', 'application/json'))
            else:
                data = str.encode((urllib.parse.urlencode(data)))

        response = opener.open(url, data, timeout)
        if cookie and not cookiejar:
            cj.save(cookie_file, ignore_discard)
        opener.close()
        link = response.read()
        if type(link) is bytes:
            link = link.decode('utf-8', 'ignore')
        response.close()
        link = link.replace('&#39;', "'").replace('&quot;', '"').replace('&amp;', "&").replace("&#39;", "'").replace('&lt;i&gt;', '').replace("#8211;", "-").replace('&lt;/i&gt;', '').replace("&#8217;",
                                                                                                                                                                                               "'").replace('&amp;quot;', '"').replace('&#215;', 'x').replace('&#038;', '&').replace('&#8216;', '').replace('&#8211;', '').replace('&#8220;', '').replace('&#8221;', '').replace('&#8212;', '')
        link = link.replace('%3A', ':').replace('%2F', '/')
        if q:
            q.put(link)
        return link
    except Exception as e:
        if raiseErrors:
            raise
        if verbose:
            from urllib.parse import urlparse
            host = urlparse(url).hostname.replace('www.', '').partition('.')[0]
            xbmc.executebuiltin(
                "XBMC.Notification(Sorry!,"+host.title()+" Website is Down,3000,"+icon+")")
        xbmc.log('***********Website Error: '+str(e) +
                 '**************', xbmc.LOGERROR)
        xbmc.log('***********Url: '+url+' **************', xbmc.LOGERROR)
        import traceback
        traceback.print_exc()
        link = final(b'd2Vic2l0ZSBkb3du').decode('utf-8')
        if q:
            q.put(link)
        return link


def setFile(path, content, force=False):
    if os.path.exists(path) and not force:
        return False
    else:
        try:
            open(path, 'w+').write(content)
            return True
        except:
            pass
    return False


user = selfAddon.getSetting(final(b'MjQ3dXNlcm5hbWU=').decode('utf-8'))
passw = selfAddon.getSetting(final(b'MjQ3cGFzc3dvcmQ=').decode('utf-8'))
if user == '' or passw == '':
    if os.path.exists(cookie_file):
        try:
            os.remove(cookie_file)
        except:
            pass
    dialog = xbmcgui.Dialog()
    ret = dialog.yesno('[COLOR red]247HD[/COLOR]',
                       'Please set your 247HD credentials or register if you dont have an account at 247HD.tv', 'Cancel', 'Login')
    if ret == 1:
        keyb = xbmc.Keyboard('', 'Enter Username')
        keyb.doModal()
        if (keyb.isConfirmed()):
            search = keyb.getText()
            username = search
            keyb = xbmc.Keyboard('', 'Enter Password:')
            keyb.setHiddenInput(True)
            keyb.doModal()
            if (keyb.isConfirmed()):
                search = keyb.getText()
                password = search
                selfAddon.setSetting('247username', username)
                selfAddon.setSetting('247password', password)

user = selfAddon.getSetting('247username')
passw = selfAddon.getSetting('247password')


def CheckForAutoUpdate(force=False):
    slogo = xbmc.translatePath(
        'special://home/addons/plugin.video.247hd/icon.png')
    UpdateVerFile = 'update'
    RunningFile = 'running'
    verCheck = False
    if verCheck == True:
        import autoupdate
        import time
        try:
            print("247HD auto update - started")
            html = OPENURL(final(b'aHR0cDovL2tvZGkuMjQ3aGQudHYvdmVyc2lvbg==').decode(
                'utf-8'), mobile=True, verbose=False)
        except:
            html = ''
        try:
            newver = int(re.findall('(?sim)\d+', html)[0])
        except:
            newver = 0
        try:
            locver = int(VERSION)
        except:
            locver = 0
        RunningFilePath = os.path.join(UpdatePath, RunningFile)
        if locver < newver and (not os.path.exists(RunningFilePath) or os.stat(RunningFilePath).st_mtime + 120 < time.time()) or force:
            UpdateUrl = final(
                b'aHR0cDovL2tvZGkuMjQ3aGQudHYvcGx1Z2luLnZpZGVvLjI0N2hkLnppcA==').decode('utf-8')
            UpdateLocalName = '247hd.zip'
            UpdateLocalFile = xbmc.translatePath(
                os.path.join(UpdatePath, UpdateLocalName))
            setFile(RunningFilePath, '')
            print("auto update - new update available ("+str(newver)+")")
            xbmc.executebuiltin(
                "XBMC.Notification(247HD Update,New Update detected,3000,"+slogo+")")
            xbmc.executebuiltin(
                "XBMC.Notification(247HD Update,Updating...,3000,"+slogo+")")
            try:
                os.remove(UpdateLocalFile)
            except:
                pass
            try:
                urllib.request.urlretrieve(UpdateUrl, UpdateLocalFile)
            except:
                pass
            if os.path.isfile(UpdateLocalFile):
                extractFolder = xbmc.translatePath('special://home/addons')
                pluginsrc = xbmc.translatePath(
                    os.path.join(extractFolder, 'plugin.video.247hd'))
                if autoupdate.unzipAndMove(UpdateLocalFile, extractFolder, False):
                    print(
                        "247HD auto update - update install successful ("+str(newver)+")")
                    xbmc.executebuiltin(
                        "XBMC.Notification(247HD Update,Successful,5000,"+slogo+")")
                    xbmc.executebuiltin("XBMC.Container.Refresh")

                else:
                    print("247HD auto update - update install failed ("+str(newver)+")")
                    xbmc.executebuiltin(
                        "XBMC.Notification(247HD Update,Failed,3000,"+slogo+")")

            else:
                print(
                    "247HD auto update - cannot find downloaded update ("+str(newver)+")")
                xbmc.executebuiltin(
                    "XBMC.Notification(247HD Update,Failed,3000,"+slogo+")")
            try:
                os.remove(RunningFilePath)
            except:
                pass
        else:
            if force:
                xbmc.executebuiltin(
                    "XBMC.Notification(247HD Update,247HD is up-to-date,3000,"+slogo+")")
            print("247HD auto update - 247HD is up-to-date ("+str(locver)+")")
        return


def setCookie():
    cookieExpired = False
    if os.path.exists(cookie_file):
        try:
            import time
            import datetime
            cookie = open(cookie_file).read()
            matches = re.finditer('(?i)expires="(.*?)"', cookie)
            for expire in matches:
                if expire:
                    expire = str(expire.group(1))
                    if time.time() > time.mktime(time.strptime(expire, '%Y-%m-%d %H:%M:%SZ')):
                        cookieExpired = True
            if time.mktime(datetime.date.yesterday().timetuple()) > os.stat(cookie_file).st_mtime:
                cookieExpired = True
        except:
            cookieExpired = True
    if not os.path.exists(cookie_file) or cookieExpired or (not loggedin and user != '' and passw != '') or not apifile:
        data = {}
        data['vb_login_username'] = user
        data['vb_login_password'] = passw
        data['Referer'] = final(
            b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL3ZpZXcucGhwP3BnPXdlYnRlbXBsYXRlIw==').decode('utf-8')

        import hashlib
        m = hashlib.md5()
        m.update(str.encode(passw))
        md5 = m.hexdigest()
        data['vb_login_md5password'] = md5
        data['vb_login_md5password_utf'] = md5
        data['s'] = ''
        data['securitytoken'] = 'guest'
        data['cookieuser'] = '1'
        data['do'] = 'login'
        OPENURL(final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL2xvZ2luLnBocD9kbz1sb2dpbg==').decode(
            'utf-8'), data=data, cookie='247hd')


def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x":
            return chr(int(text[3:-1], 16))
        else:
            return chr(int(text[2:-1]))
    if type(text) is str:
        return re.sub("(?i)&#\w+;", fixup, text)
    else:
        return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))


def MAINSA():
    import datetime
    date = datetime.date.today()
    setCookie()
    urllist = []
    namelist = []
    link = OPENURL(final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL3ZpZXcucGhwP3BnPXdlYnRlbXBsYXRlIw==').decode(
        'utf-8'), cookie='247hd')
    link2 = OPENURL(final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL2NhbGVuZGFyLnBocD9kbz1nZXRpbmZvJmRheT0=').decode(
        'utf-8')+str(date)+'&c=1', cookie='247hd')
    link = cleanHex(link)
    link = link.replace('\r', '').replace('\n', '').replace(
        '\t', '').replace('&nbsp;', '').replace('  ', '')
    link2 = cleanHex(link2)
    link2 = link2.replace('\r', '').replace('\n', '').replace(
        '\t', '').replace('&nbsp;', '').replace('  ', '')
    if '<a href="#" class="user-name">'+user+'</a>' in link:
        matchlist = re.compile(
            '<ul class="inner-ul">(.+?)</ul></a>').findall(link)
        for urls in matchlist:
            urllist.append(urls)
        addLink('[COLOR red][I]VIP Member[/I][/COLOR]',
                artpath+'empty.png', '')
        addLink2('[I][COLOR red]Refresh Links[/COLOR][/I]  (Click Here if Videos are not playing)',
                 'url', 555, artpath+'empty.png', fanart)
        addDir('[COLOR blue]All Channels[/COLOR] (Click Here)',
               'test', 477, artpath+'channels.png')
        addDir('[COLOR blue]VOD[/COLOR] (Click Here)', final(
            b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL3ZpZXcucGhwP3BnPWNidm9kIw==').decode('utf-8'), 478, artpath+'vod.png')
        addDir('[COLOR blue]Schedule[/COLOR] (Click Here)',
               'test', 476, artpath+'schedule.png')

        match = re.compile(
            '<span class="time">([^<]+)</span> to <span class="time">([^<]+)</span>.+?<h2 class="title">([^<]+)</h2>').findall(link2)
        for time1, time2, title in match:
            try:
                ch = re.findall('(?sim)channel\s(\d+)', title)[0]
            except:
                ch = re.findall('(?sim)Channel\s(\d+)', title)[0]
            title = re.sub("(Channel \d+)", "", title)
            num = int(ch)-1
            addPlay('[COLOR ffde251d]'+time1+' - '+time2+'[/COLOR] '+title +
                    ' [COLOR orange]Channel: '+str(ch)+'[/COLOR]', urllist[num], 411, art+ch+'.png')

    else:
        addLink('Login Failed Clear Cookies and try again', '', '')
        addLink2('[B][COLOR red]Clear Cookies[/B][/COLOR]',
                 'url', 358, artpath+'empty.png', fanart)

    if '<a href="#" class="user-name">'+user+'</a>' in link:
        addLink(' ', '', '')
        addLink2('[B][COLOR red]Clear Cookies[/B][/COLOR]',
                 'url', 358, artpath+'empty.png', fanart)
        addLink('[B][COLOR blue]Twitter[/B][/COLOR] [COLOR white]@Plus1HD[/COLOR]',
                '', artpath+'empty.png')
        addLink2(final(b'W0NPTE9SIGdyZXldW0ldRm9yIHN1cHBvcnQgdmlzaXQgaHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL2ZvcnVtLnBocFsvSV1bL0NPTE9SXQ==').decode(
            'utf-8'), 'url', '', artpath+'empty.png', fanart)


def FullChannel(murls):
    setCookie()
    i = 1
    link = OPENURL(final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL3ZpZXcucGhwP3BnPXdlYnRlbXBsYXRlIw==').decode(
        'utf-8'), cookie='247hd')
    link = cleanHex(link)
    link = link.replace('\r', '').replace('\n', '').replace(
        '\t', '').replace('&nbsp;', '').replace('  ', '')
    addLink2('[I][COLOR red]Refresh Links[/COLOR][/I]  (Click Here if Videos are not playing)',
             'url', 555, artpath+'empty.png', fanart)
    if '<a href="#" class="user-name">'+user+'</a>' in link:
        matchlist = re.compile(
            '<li>([^<]+)</li><ul class="inner-ul">(.+?)</ul></a>').findall(link)
        for name, urls in matchlist:
            addPlay(name, urls, 411, art+str(i)+'.png')
            i = i+1


def VOD(murl):
    if final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL3ZpZXcucGhwP3BnPWNidm9kIw==').decode('utf-8') in murl:
        setCookie()
        link = OPENURL(murl, cookie='247hd')
        link = cleanHex(link)
        link = link.replace('\r', '').replace('\n', '').replace(
            '\t', '').replace('&nbsp;', '').replace('  ', '')
        match = re.compile(
            '<li>([^<]+)</li><ul class="inner-ul">(.+?)</ul></a>').findall(link)
        for name, urls in match:
            addDir(name, urls, 478, '')
    else:
        match = re.compile(
            '<a href="(.+?)" target=".+?">(.+?)</a>').findall(murl)
        for url, name in match:
            url = final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zLw==').decode(
                'utf-8')+url
            addPlay(name, url, 413, '')


def Set(id=addon_id):
    xbmc.executebuiltin('Addon.OpenSettings(%s)' % id)


def Fresh():
    xbmc.executebuiltin("XBMC.Container.Refresh")


def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(500)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(500)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass


def clearCookies():
    dialog = xbmcgui.Dialog()
    if dialog.yesno('247HD', 'Are you sure you want to clear Cookies?', 'No', 'Yes'):
        import os
        cookie_file = os.path.join(datapath, 'Cookies')
        ClearDir(xbmc.translatePath(cookie_file), True)
        xbmc.executebuiltin(
            "XBMC.Notification(Clear Cookies,Successful,5000,"")")


def ClearDir(dir, clearNested=False):
    for the_file in os.listdir(dir):
        file_path = os.path.join(dir, the_file)
        if clearNested and os.path.isdir(file_path):
            ClearDir(file_path, clearNested)
            try:
                os.rmdir(file_path)
            except Exception as e:
                print(str(e))
        else:
            try:
                os.unlink(file_path)
            except Exception as e:
                print(str(e))


def Calendar(murl, addday=0):
    import time
    import datetime
    setCookie()
    urllist = []
    data = {}
    data['category'] = 0
    data['timezone'] = "America/New_York"
    now = datetime.datetime.now()
    if now.hour >= 6:
        begin = datetime.datetime(now.year, now.month, now.day, 6, 0, 0)
    else:
        yesterday = now - datetime.timedelta(days=1)
        begin = datetime.datetime(
            yesterday.year, yesterday.month, yesterday.day, 6, 0, 0)
    if addday > 0:
        begin = begin + datetime.timedelta(days=addday)
    data['day'] = int(begin.timestamp())
    link = OPENURL(final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvc2NoZWR1bGUvaW5kZXhfZGF0YS5waHA=').decode(
        'utf-8'), data=data, cookie='247hd')
    link2 = OPENURL(final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL3ZpZXcucGhwP3BnPXdlYnRlbXBsYXRlIw==').decode(
        'utf-8'), cookie='247hd')
    link = cleanHex(link)
    link2 = link2.replace('\r', '').replace('\n', '').replace(
        '\t', '').replace('&nbsp;', '').replace('  ', '')
    link = link.replace('\r', '').replace('\n', '').replace(
        '\t', '').replace('&nbsp;', '').replace('  ', '')
    if '<a href="#" class="user-name">'+user+'</a>' in link2:
        matchlist = re.compile(
            '<ul class="inner-ul">(.+?)</ul></a>').findall(link2)
        for urls in matchlist:
            urllist.append(urls)
    for line in link.split("</tr>"):
        lines = re.findall(
            '.*<tr.*>.*<td.*">(.*)</td>.*<td.*>.*</td>.*<td.*>.*</td>.*<td.*">(.*)</td>.*<td>(.*)</td>.*', line)
        for day, ch, title in lines:
            title = title.split("<")[0]
            if title.find("Offline") == -1:
                num = int(ch)-1
                if num >= 0 and num < len(urllist):
                    addPlay('[COLOR ffde251d]'+day+'[/COLOR] ' +
                            title, urllist[num], 411, art+ch+'.png')
    while addday < 2:
        addday = addday + 1
        Calendar(murl, addday)


def LISTCONTENT(murl, thumb):
    urllist = []
    namelist = []
    match = re.compile(
        '<li><a href="([^"]+)".+?arget=".+?">([^<]+)</a></li>').findall(murl)
    for url, name in match:
        urllist.append(
            final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zLw==').decode('utf-8')+url)
        namelist.append(name)
    dialog = xbmcgui.Dialog()
    ret = dialog.select('Select Source', namelist)
    if ret == -1:
        return
    else:
        ans = urllist[ret]
        PLAYLINK(namelist[ret], ans, '')


def get_link(murl):
    setCookie()
    link = OPENURL(murl, cookie='247hd')
    link = cleanHex(link)
    link = link.replace('\r', '').replace('\n', '').replace(
        '\t', '').replace('&nbsp;', '').replace('  ', '')
    m3u8 = re.findall("""'file': "([^"]+?)",""", link)
    m3u8B = re.findall("{file:'([^']+?.m3u8)'}", link)
    iframe = re.findall(
        '<iframe src="(https://admin.livestreamingcdn.com[^"]+?)"', link)
    if m3u8:
        return m3u8[0]
    elif final(b'aHR0cHM6Ly93d3cuMjQ3aGQudHYvZm9ydW1zL3ZpZXcucGhwP3Bn').decode('utf-8') in murl:
        swf = re.findall('src="([^<]+).swf"', link)[0]
        file = re.findall("file=(.+?)&", link)[0]
        file = file.replace('.flv', '')
        streamer = re.findall("streamer=(.+?)&", link)[0]
        if '.mp4' in file and 'vod' in streamer:
            file = 'mp4:'+file
            return streamer.replace('redirect', 'live')+' playpath='+file+' swfUrl='+swf+'.swf pageUrl='+murl
        else:
            return streamer.replace('redirect', 'live')+' playpath='+file+' swfUrl='+swf+'.swf pageUrl='+murl+' live=true timeout=20'
    elif m3u8B:
        return m3u8B[0]
    elif 'euplayer' or 'usplayer' in murl:
        vlink = re.findall("""'file': "([^"]+)",""", link)
        return vlink[0]
    elif iframe:
        with urlopen(iframe[0]) as response:
            link = response.read()
            link = cleanHex(link)
            link = link.replace('\r', '').replace('\n', '').replace(
                '\t', '').replace('&nbsp;', '').replace('  ', '')
            vlink = re.findall('file: "([^"]+?.m3u8)"', link)
            return vlink[0]

    else:
        swf = re.findall("src='([^<]+).swf'", link)[0]
        file = re.findall("file=(.+?)&", link)[0]
        file = file.replace('.flv', '')
        streamer = re.findall("streamer=(.+?)&", link)[0]
        if '.mp4' in file and 'vod' in streamer:
            file = 'mp4:'+file
            return streamer.replace('redirect', 'live')+' playpath='+file+' swfUrl='+swf+'.swf pageUrl='+murl
        else:
            return streamer.replace('redirect', 'live')+' playpath='+file+' swfUrl='+swf+'.swf pageUrl='+murl+' live=true timeout=20'


def PLAYLINK(mname, murl, thumb):
    ok = True
    stream_url = get_link(murl)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    playlist.clear()
    listitem = xbmcgui.ListItem(mname)
    listitem.setArt({'thumb': thumb})
    playlist.add(stream_url, listitem)
    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(playlist)
    return ok


def addPlay(name, url, mode, iconimage):
    u = sys.argv[0]+"?url="+urllib.parse.quote_plus(url)+"&mode="+str(
        mode)+"&name="+urllib.parse.quote_plus(name)+"&iconimage=" + urllib.parse.quote_plus(iconimage)
    ok = True
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': '', 'thumb': iconimage})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty('fanart_image', fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok


def addLink2(name, url, mode, iconimage, fanart, description=''):
    u = sys.argv[0]+"?url="+urllib.parse.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.parse.quote_plus(name)+"&iconimage="+urllib.parse.quote_plus(
        iconimage)+"&fanart="+urllib.parse.quote_plus(fanart)+"&description="+urllib.parse.quote_plus(description)
    ok = True
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': "DefaultFolder.png", 'thumb': iconimage})
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
    liz.setProperty("Fanart_Image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=False)
    return ok


def addLink(name, url, iconimage):
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': art+'/empty.png', 'thumb': iconimage})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty('fanart_image', fanart)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz)


def addDir2(name, url, mode, iconimage, fanart, description=''):
    u = sys.argv[0]+"?url="+urllib.parse.quote_plus(url)+"&mode="+str(
        mode)+"&name="+urllib.parse.quote_plus(name)+"&description="+str(description)
    ok = True
    liz = xbmcgui.ListItem(
        name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, 'plot': description})
    liz.setProperty('fanart_image', fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok


def addDir(name, url, mode, iconimage):

    u = sys.argv[0]

    u += "?url=" + urllib.parse.quote_plus(url)
    u += "&mode=" + str(mode)
    u += "&name=" + urllib.parse.quote_plus(name)
    u += "&iconimage=" + urllib.parse.quote_plus(iconimage)

    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': '', 'thumb': iconimage})
    liz.setInfo(type="Video", infoLabels={"Title": name})
    liz.setProperty('fanart_image', fanart)

    xbmcplugin.addDirectoryItem(handle=int(
        sys.argv[1]), url=u, listitem=liz, isFolder=True)


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params)-1] == '/'):
            params = params[0:len(params)-2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param


params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
    url = urllib.parse.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.parse.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    iconimage = urllib.parse.unquote_plus(params["iconimage"])
    iconimage = iconimage.replace(' ', '%20')
except:
    pass

print("Mode: "+str(mode))
print("Name: "+str(name))
print("Thumb: "+str(iconimage))


if mode == None or url == None:
    import threading
    threading.Thread(target=CheckForAutoUpdate).start()
    MAINSA()


elif mode == 411:
    LISTCONTENT(url, iconimage)
elif mode == 413:
    PLAYLINK(name, url, iconimage)
elif mode == 476:
    Calendar(url)
elif mode == 477:
    FullChannel(url)
elif mode == 478:
    VOD(url)
elif mode == 358:
    clearCookies()
elif mode == 239:
    Set()
elif mode == 555:
    Fresh()
elif mode == 240:
    if selfAddon.getSetting("server-location") == "true":
        selfAddon.setSetting('server-location', 'false')
        print('false')
    else:
        selfAddon.setSetting('server-location', 'true')
        print('true')
    xbmc.executebuiltin("XBMC.Container.Refresh")

xbmcplugin.endOfDirectory(int(sys.argv[1]))
