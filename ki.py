# -*- coding: utf-8 -*-
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import ast,re,time,random,sys,json,codecs,threading,glob
from time import sleep
import os,six, urllib, urllib2, wikipedia, requests
from bs4 import BeautifulSoup

cl = LINETCR.LINE()
cl.login(toker="")
cl.loginResult()

kk = LINETCR.LINE()
kk.login(toker="")
kk.loginResult()

ka = LINETCR.LINE()
ka.login(token="")
ka.loginResult()

print "──────┅═ই۝ई═┅────── ล็อคอิน🔥BY:ᴛᴇᴀᴍᴍᴏᴅᴅᴀʀᴋsᴇʟғʙᴏᴛ🔥สำเร็จ ──────┅═ই۝ई═┅──────\n✥===========================================================================================✥"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
  ╔•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱ •═•╗
  ║       [ສ̲̲̅][٦̲̲̅][છ̲̲̅̅][ஏ̲̲̅̅][٦̲̲̅][ई̲̲̅̅][π̲̲̅̅]        ║
  ╚•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱ •═•╝
     ↬ [ระบบป้องกันในกลุ่ม] ↫
🌟purge:(on/off)➠ ยกเลิก+ห้ามเชิญ
🌟qr:(on/off)      ➠ ป้องกันลิ้งกลุ่ม
🌟blockinvite:(on/off)➠ กันเชิญคน
🌟protection:(on/off) ➠ เปิดป้องกัน
🌟protectmax: ➠ เปิดป้องกันพิเศษ
🌟set view    ➠ ดูการตั้งค่าป้องกัน
              👣 [ ระบบเตะ  ] 👣
👹Fuck (@แทค) ➠สั่งคิกผีเข้ามาเตะ
👹kick (@แทค) ➠แทคชื่อเตะเยอะ
👹kill➠ เตะ+ดึง+ยกเลิก(เตะลบแชท)
👹*fuck off ➠ เตะล้างกลุ่ม
👹kill ban➠สั่งบอทเตะแบนทุกกลุ่ม
              👀[ระบบก่อกวน]👀
👻Spam:(ชื่อกลุ่ม)@(mid)➠รันกลุ่ม
👻spam chat:(ข้อความ)➠รันแชท
👻Spam contact (@) ➠บอทแสปม
👻Spam on (เลข) (ข้อความ)➠ฟลัด
👻Spam off (เลข) (ข้อความ)➠ฟลัด
              👑[ตั้งค่าทั่วไป]👑
🃏autoadd: (on/off) ➠รับเพื่อน
🃏autojoin: [wl/on/off] ➠เข้ากลุ่ม
🃏autolike: (on/off) ➠ ไลค์TL
🃏block (@ แทค) ➠ลบเพื่อน
🃏blocklist ➠ รายการเพื่อนที่ลบ
🃏all status(ข้อความ)➠statusคิก
🃏rejectinvite:(on/off) ➠กันรัน
🃏ลบรัน ➠ ล้างรัน+คิก
🃏*kicker      ➠  เรียกคิกเข้ากลุ่ม
🃏Check:on ➠  เปิดเช็คคนอ่าน
🃏Check:off➠  ปิดเช็คคนอ่าน
🃏Check      ➠  รายงานคนอ่าน
🃏my groups➠ เช็คกลุ่มของเรา
🃏show:(mid)➠ ดูคอนแทค
🃏search(@แทค)➠ ตามล่าคน
🃏ourl          ➠ เปิดลิ้งกลุ่ม
🃏curl          ➠ ปิดลิ้งกลุ่ม
🃏gid           ➠ ดูรหัสกลุ่ม
🃏*kicker @bye➠ สั่งบอทออก
🃏wl add:➠ เพิ่มรายการขาว
🃏del wl: ➠ ลบรายการขาว
🃏join      ➠ มุดลิ้งจู่โจม
🃏ban:     ➠ แบน
🃏unban:➠  ลบแบน
🃏wl add (@แทค)➠ เพิ่มขาว
🃏wl del (@แทค) ➠ ลบขาว
🃏ban add (@แทค)➠ แบน
🃏ban del (@แทค)➠ ลบแบน
🃏banlist   ➠ ดูรายการแบน
🃏cek ban ➠ เช็ครายการแบน
🃏whitelist ➠ ดูรายการขาว
🃏me      ➠ ส่งคอนแทคเรา
🃏cancel ➠ ยกเลิกเชิญ
🃏clear whitelist➠ลบขาวหมด
🃏ลบดำ ➠ ลบรายการแบน
🃏message  ➠ ข้อความออโต้
🃏Follow (@แทค)➠ เลียนแบบ
🃏restore ➠ กลับคืน
🃏gift ➠ ของขวัญ
🃏Tag ➠ แทคทั้งกลุ่ม
🃏Bc in group:➠ บรอดเเคสหาในกลุ่ม
🃏Bc all group:➠ บรอดแคสทุกกลุ่ม
🃏Bc friend:➠ บรอสแคสหาส่วนตัว
🃏Say➠ สั่งบอทพูดตาม
🃏ping➠ เล่นกับบอท
🃏get mid (@แทค)➠ ดูMid
🃏get status (@แทค)➠ ดูสถานะ
🃏get name (@แทค)➠ ดูชื่อ
🃏reboot   ➠ ตั้งค่าเริ่มต้น
🃏Sc:(mid)➠ ดู
🃏Leave: (ชื่อกลุ่ม)➠ ออกจากกลุ่ม
🃏Translate➠ แปลภาษา
🃏cn:(ชื่อ)➠ เปลี่ยนชื่อ
🃏cs:(สถานะ)➠ เปลี่ยนstatus
🃏all status:(สถานะ)➠ เปลี่ยนหมด
🃏all rename:(ชื่อ)➠ เปลี่ยนหมด
🃏kicker status:(ชื่อ)➠บอทเปลี่ยน
🃏kicker rename:(ชื่อ)➠บอท
🃏kicker copy @➠คิกปลอมตัว
🃏*1-*10(bye bots)➠สั่งบอทออก
🃏Gn (name)➠ เปลี่ยนชื่อกลุ่ม
🃏mc add @➠ เพิ่มพูดตาม
🃏mc del @➠ ลบพูดตาม
🃏mc:➠ พูดตาม
🃏mc list➠เช็ครายการ
🃏Yutube ➠ ค้นหายูทูป
🃏Google ➠ ค้นหากูเกิ้ล
🃏Wikipedia➠ค้นหาวิกิพีเดีย
🃏steal pict @➠ ดึงรูปโปร
🃏steal cover@➠ ดึงรูปcover
🃏Message ➠ ออโต้ข้อความ
🃏Contact(on/off) ➠ อ่านแทค
🃏restore ➠ แบ็คอัพ+กู้คืนชื่อ
🃏Yutube ➠ ค้นหายูทูป
🃏welcome ➠ ต้อนรับ
      🔥 โหมดตอบรับ 🔥
♥ข้อความต้อนรับ:(ข้อความ)
♥wc ➠ เช็คข้อความ
♥welcome:(on/off)➠ปิด/เปิด
♥allpict ➠ ดึงรูปโปรยกกลุ่ม
♥wban ➠ แบนคำพูด
♥wunban➠ ลบแบนคำพูด
♥wbanlist ➠ รายการคำแบน

      Ҩఖণಖஇ↭ধัюӄՁ่গს
                   ⭐️by ⭐️
  ╔•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱ •═•╗
  ║       [ສ̲̲̅][٦̲̲̅][છ̲̲̅̅][ஏ̲̲̅̅][٦̲̲̅][ई̲̲̅̅][π̲̲̅̅]        ║
  ╚•═•-⊰❉⊱•═•⊰❉⊱•═•⊰❉⊱ •═•╝
        ᴛ̶̢̡̨̛̦̣̲̯͔̹̠̮̄́͂͋͗̽̃̇̏̚͝ͅᴇ̷̡̢̨͉͖̗̮͎̗̭̣̠̊͗̔̂̈͌̅̇̿̚͠͝ᴀ̴̢͍̪̻͓̰̗̪̲̰̠̏̈́͌̆̽͗̀͌̌͛̋͜͠ᴍ̵̛̛̞͓̟̗̤͎̥̠̤͖̈́̈́̓̂̂͆͋̇͐̕͜͜ᴍ̴̮̣̖̲͉̪̰̹̼̮͇̈́̈́́̈͐̄̀͆͗̕͝͝ͅᴏ̵̨̬͉̗̙̘̙͈̳͖̞̻̏̏̓̈́̂̈́̇͗̓̋̕͝ᴅ̵̧̛̦̘͔͚̦͇̦̰͙͓͆̀͛͌́͂̃͒̊̈̚͜ᴅ̷̨̡̛̦̠̫̥̤̰͎͕̼̻̆̍͂̅͊͐͗̔́̕͝ᴀ̵̡̡̢͚̯̰̞̱͕͉͈͒̇̃́͌͑̔͂̽̀̎̐ͅʀ̷̥̻̞̖̖̩̠͙͚̻͉̀́̔͐̄̔̏̚͜͝͝͠͝ᴋ̶̧̱̝̥̥͈͎̱̖̣̥̈́͑̒̔͗̒̈́́͛͝͝͝ͅs̸̢̛̖̼̺͙̣̦̰̘͖̘̼͋͛̇̉͂́̕͘̚̚͝ᴇ̵̭͓̜͔̜̖̭̼͓̳̺̺̌́͌̏͒̔̾̒̕͘̕͝ʟ̷̠̰̩̬̩̮̰̠͍͇̈̀͒̀̈́̌̇̽͆̏̔̂͜ͅғ̷̞̲̥̞̳͖̘̭̥̦̖̺̊͂̒̀͒̐͑̃̿̊͘̚ʙ̷͇̙̞̠͍͕͇̗̥̮̳͗̾́̐͒̅̎͌̏͐͝͝ͅᴏ̶̨̢̨̡̛̤̭̼͙͎͖̼̤́̄͛͊̐͗̍̾̏̀͝ᴛ̸̨͙͍̜͖̘͖̯͙̱̼̊͑̄́͗̆̊̅͐́͜͝͝
"""
KAC=[kk,cl,ka]
#KFC=[kk,ka]
mid = cl.getProfile().mid
#Bmid = kk.getProfile().mid
#Wmid = ka.getProfile().mid

Bots=[mid]
wbanlist = []
inviting = False
backup = cl.getProfile()
#backup1 = kk.getProfile()
#backup2 = ka.getProfile()
strt = datetime.now()
periksa = {
        'autojoin':"off",
        'addbanmode':{},
        'delbanmode':{},
        'banlist':{},
        'addfriend':{},
        'autocancel':{},
        'autopurge':{},
        'lockqr':{},
        'liketl':{},
        'wl':{},
        'addwl':{},
        'delwl':{},
        'undang':{},
        'tmimic':{},
        'welcomeN':{},
        'welcomeM':'',
        'mimic':False,
        'message':"",
        'autolike':False,
        'autoadd':False,
        'autorejc':True
}
sider = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
setTime = {}
setTime = sider['setTime']

wait = {
    'contact':False, 
    'autoJoin':False, 
    "detectMention":True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    "lang":"JP",
    "commentOn":True,
    "tag1":"\nสนใจXทอย ยาอึด ยาปลุกหญิงทักแชทนะคะ",
    "tag2":"\nตอบช้าใจเย็นๆกันนะค่ะ", 
    "commentBlack":{},
    }


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

agent = {'user-Agent': "Mozilla/4.0(compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50/27; .NET CLR 3.0.04506.0)"} 

def translate(to_translate, to_language="auto", language="auto"):
    base_link="http://translate.google.com/m?hl=%s&sl=%s&q=%s"
    if(six.PY2):
        link = base_link % (to_language, language, urllib.pathname2url(to_translate))
        request = urllib2.Request(link, headers=agent)
        page = urllib2.urlopen(request).read()
    else:
        link = base_link % (to_language, language, urllib.parse.quote(to_translate))
        request = urllib.request.Request(link, headers=agent)
        page = urllib.request.urlopen(request).read().decode('utf-8')
    expr = r'class="t0">(.*?)<'
    result = re.findall(expr,page)
    if(len(result)==0):
        return("")
    return(result[0])

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def bot(op):
    try:
        
        if op.type == 0:
            return
        if op.type == 5:
            if periksa['autoadd'] == True:
                cl.findAndAddContactsByMid(op.param1)
                ka.findAndAddContactsByMid(op.param1)
                kk.findAndAddContactsByMid(op.param1)
                if (periksa["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(periksa["message"]))
                    ka.sendText(op.param1,str(periksa["message"]))
                    kk.sendText(op.param1,str(periksa["message"]))
            else:
                pass
	if op.type == 11:
          if op.param1 in periksa["lockqr"]:
             if op.param2 not in Bots and op.param2 not in periksa["wl"]:
                X = cl.getGroup(op.param1)
                if X.preventJoinByTicket == False:
                  X.preventJoinByTicket = True
                  cl.updateGroup(X)
		  if op.param2 in periksa["banlist"]:
		    try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kicker=random.choice(KAC)
                            kicker.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kicker=random.choice(KAC)
                                kicker.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                cl.kickoutFromGroup(op.param1,[op.param2])
		  else:
		    periksa["banlist"][op.param2] = True
                    with open('settingan.json', 'w') as fp:
                      json.dump(periksa, fp, sort_keys=True, indent=4) 
        if op.type == 17:
          if op.param1 in periksa["autopurge"]:
            G = cl.getGroup(op.param1)
            if G is None:
                pass
            else:
                gMembMids = [contact.mid for contact in G.members]
                matched_list = []
                for tag in periksa["banlist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                if matched_list == []:
                        pass
                for jj in matched_list:
                    try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(op.param1,[jj])
                    except:
                        try:
                            kicker=random.choice(KAC)
                            kicker.kickoutFromGroup(op.param1,[jj])
                        except:
                            try:
                                kicker=random.choice(KAC)
                                kicker.kickoutFromGroup(op.param1,[jj])
                            except:
                                cl.kickoutFromGroup(op.param1,[jj])
          if op.param1 in periksa['welcomeN']:
              cl.sendText(op.param1,str(periksa["welcomeM"]))
              with open('settingan.json', 'w') as fp:
                      json.dump(periksa, fp, sort_keys=True, indent=4)                  

        if op.type == 13:
            if mid in op.param3:
	      if periksa["autojoin"] == "wl":
                if op.param2 in periksa["wl"]:
		    cl.acceptGroupInvitation(op.param1)
		else:
		    if periksa['autorejc'] == True:
                        cl.rejectGroupInvitation(op.param1)
                    else:
                        pass
              elif periksa["autojoin"] == "all":
		   cl.acceptGroupInvitation(op.param1)
	      else:
                  if periksa['autorejc'] == True:
                        cl.rejectGroupInvitation(op.param1)
                  else:
                        pass
			
            else:
                if op.param2 not in Bots and op.param2 not in periksa["wl"]:
                  group_id=op.param1
                  if group_id in periksa["autocancel"]:
                    group = cl.getGroup(op.param1)
                    if group.invitee is None:
                       pass
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        try:
                            kicker=random.choice(KAC)
                            kicker.cancelGroupInvitation(op.param1, gInviMids)
                        except:
                            try:
                                kicker=random.choice(KAC)
                                kicker.cancelGroupInvitation(op.param1, gInviMids)
                            except:
                                try:
                                    kicker=random.choice(KAC)
                                    kicker.cancelGroupInvitation(op.param1, gInviMids)
                                except:
                                    cl.cancelGroupInvitation(op.param1, gInviMids)
                                
                if op.param1 in periksa["autopurge"]:        
                    Inviter = op.param3.replace("",',')
                    InviterX = Inviter.split(",")
                    matched_list = []
                    for tag in periksa["banlist"]:
                        matched_list+=filter(lambda str: str == tag, InviterX)
                    if matched_list == []:
                        pass
                    else:
                        try:
                            kicker=random.choice(KAC)
                            kicker.cancelGroupInvitation(op.param1, matched_list)
                        except:
                            try:
                                kicker=random.choice(KAC)
                                kicker.cancelGroupInvitation(op.param1, matched_list)
                            except:
                                try:
                                    kicker=random.choice(KAC)
                                    kicker.cancelGroupInvitation(op.param1, matched_list)
                                except:
                                    cl.cancelGroupInvitation(op.param1, matched_list)
                        
		    
        if op.type == 19:
            if op.param1 in periksa["protect"]:
                if op.param2 not in Bots and op.param2 not in periksa['wl']:
                    try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
			if op.param2 in periksa["banlist"]:
                          pass
			else:
                          kicker=random.choice(KAC)
			  kicker.inviteIntoGroup(op.param1,[op.param3])
		    except:
                      try:
                            kicker=random.choice(KAC)
                            kicker.kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 in periksa["banlist"]:
		              pass
                            else:
			      kicker=random.choice(KAC)
                              kicker.inviteIntoGroup(op.param1,[op.param3])
                      except:
                            try:
                              G = cl.getGroup(op.param1)
                            except:
                              G = kk.getGroup(op.param1)
                            if op.param2 in G.members:
                              try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                if op.param2 in periksa["banlist"]:
                                  pass
                                else:
                                  cl.inviteIntoGroup(op.param1,[op.param3])
                              except:
                                  pass
                            else:
                                print "Target sudah tidak ada"
                if op.param2 in periksa["banlist"]:
                        pass
		elif op.param2 in periksa["wl"]:
			 pass
		elif op.param2 in Bots:
			 pass
                else:
                        periksa["banlist"][op.param2] = True
                        with open('settingan.json', 'w') as fp:
    			   json.dump(periksa, fp, sort_keys=True, indent=4)
    			   
            if mid in op.param3:
                     try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                     except:
                        try:
                          kicker=random.choice(KAC)
                          kicker.kickoutFromGroup(op.param1,[op.param2])
                        except:
                          kk.kickoutFromGroup(op.param1,[op.param2])
                     try:
                         G = kk.getGroup(op.param1)
                     except:
                         try:
                             G = ka.getGroup(op.param1)
                         except:
                             try:
                                 G = kb.getGroup(op.param1)
                             except:
                                 try:
                                     G = wb.getGroup(op.param1)
                                 except:
                                     pass
                     G.preventJoinByTicket = False
                     try:
                         kk.updateGroup(G)
                         Ti = kk.reissueGroupTicket(op.param1)
                     except:
                         try:
                             ka.updateGroup(G)
                             Ti = ka.reissueGroupTicket(op.param1)
                         except:
                            pass
                     cl.acceptGroupInvitationByTicket(op.param1,Ti)
                     X = cl.getGroup(op.param1)
                     X.preventJoinByTicket = True
                     cl.updateGroup(X)
                     Ti = cl.reissueGroupTicket(op.param1)
                     if op.param2 in periksa["banlist"]:
                        pass
                     elif op.param2 in periksa["wl"]:
			pass
		     elif op.param2 in Bots:
			pass
                     else:
                        periksa["banlist"][op.param2] = True
            if Bmid in op.param3:
                     try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                     except:
                        try:
                          kicker=random.choice(KAC)
                          kicker.kickoutFromGroup(op.param1,[op.param2])
                        except:
                          cl.kickoutFromGroup(op.param1,[op.param2])
                     try:
                      kicker=random.choice(KAC)
                      G = kicker.getGroup(op.param1)
                     except:
                      G = kv.getGroup(op.param1)
                      G.preventJoinByTicket = False
                     try:
                      kicker=random.choice(KAC)
                      kicker.updateGroup(G)
                      Ti = kicker.reissueGroupTicket(op.param1)
                     except:
                      cl.updateGroup(G)
                      Ti = cl.reissueGroupTicket(op.param1)
                     kk.acceptGroupInvitationByTicket(op.param1,Ti)
                     G = kk.getGroup(op.param1)
                     G.preventJoinByTicket = True
                     kk.updateGroup(G)
                     Ticket = kk.reissueGroupTicket(op.param1)
                     if op.param2 in periksa["banlist"]:
                        pass
		     elif op.param2 in periksa["wl"]:
			 pass
		     elif op.param2 in Bots:
			pass
                     else:
                        periksa["banlist"][op.param2] = True
                        with open('settingan.json', 'w') as fp:
    			   json.dump(periksa, fp, sort_keys=True, indent=4)
    	    if Wmid in op.param3:
                     try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                     except:
                        try:
                          kicker=random.choice(KAC)
                          kicker.kickoutFromGroup(op.param1,[op.param2])
                        except:
                          cl.kickoutFromGroup(op.param1,[op.param2])
                     try:
                      kicker=random.choice(KAC)
                      G = kicker.getGroup(op.param1)
                     except:
                      G = kv.getGroup(op.param1)
                      G.preventJoinByTicket = False
                     try:
                      kicker=random.choice(KAC)
                      kicker.updateGroup(G)
                      Ti = kicker.reissueGroupTicket(op.param1)
                     except:
                      cl.updateGroup(G)
                      Ti = cl.reissueGroupTicket(op.param1)
                     ka.acceptGroupInvitationByTicket(op.param1,Ti)
                     G = ka.getGroup(op.param1)
                     G.preventJoinByTicket = True
                     ka.updateGroup(G)
                     Ticket = ka.reissueGroupTicket(op.param1)
                     if op.param2 in periksa["banlist"]:
                        pass
		     elif op.param2 in periksa["wl"]:
			 pass
		     elif op.param2 in Bots:
			pass
                     else:
                        periksa["banlist"][op.param2] = True
                        with open('settingan.json', 'w') as fp:
    			   json.dump(periksa, fp, sort_keys=True, indent=4)
	if op.type == 55:
            try:
                if op.param1 in sider['readPoint']:
		    
                    if op.param2 in sider['readMember'][op.param1]:
                        pass
                    else:
                        sider['readMember'][op.param1] += op.param2
                	sider['ROM'][op.param1][op.param2] = op.param2
                	with open('sider.json', 'w') as fp:
    			   json.dump(sider, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
        if op.type == 26:
            msg = op.message
            if msg.text:
                if msg.text.lower().lstrip().rstrip() in wbanlist:
                    try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(msg.to,[msg.from_])
                    except:
                        cl.kickoutFromGroup(msg.to,[msg.from_])                 
        if op.type == 26:
            msg = op.message
            if periksa['mimic'] == True:
                if msg.from_ in periksa['tmimic']:
                    if msg.text.lower() not in ['help','mimic','kill','kick','@bye','say','lurk','autolike','autojoin','qr on','qr off']:
                        cl.sendMessage(msg)
                else:
                    pass
            else:
                pass
            if 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["detectMention"] == True:
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = [cName + "\n" + str(wait["tag1"]) , cName + "\n" + str(wait["tag2"])]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in Bots:
                            cl.sendText(msg.to,ret_)
                            break
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '1',
                                                            'STKTXT': '[]',
                                                            'STKVER': '16',
                                                            'STKID':'10'
                                                        }
                                  cl.sendMessage(msg)
                                  break
	if op.type == 25: #disini :v
            msg = op.message
            pesan = msg.text
            
            if msg.contentType == 13:
               global inviting
               if inviting:
                    inviting = False
                    try:
                        kicker=random.choice(KAC)
                        kicker.findAndAddContactsByMid(msg.contentMetadata["mid"])
                        kicker.inviteIntoGroup(msg.to,[msg.contentMetadata["mid"]])
                    except:
                        cl.inviteIntoGroup(msg.to,[msg.contentMetadata["mid"]])           
	    
            if msg.contentType == 13:
               if msg.to in periksa["addbanmode"]:
		  if msg.contentMetadata["mid"] in periksa["banlist"]:
			cl.sendText(msg.to, "Succes")
		  elif msg.contentMetadata["mid"] in periksa["wl"]:
                            cl.sendText(msg.to,"failed, can't ban whitelist")
		  else:
                        periksa["banlist"][msg.contentMetadata["mid"]] = True
                        with open('settingan.json', 'w') as fp:
    			   json.dump(periksa, fp, sort_keys=True, indent=4)
			cl.sendText(msg.to, "Succes")
	       elif msg.to in periksa["delbanmode"]:
                   if msg.contentMetadata["mid"] in periksa["banlist"]:
                        del periksa["banlist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"succes deleted")
                        with open('settingan.json', 'w') as fp:
    			   json.dump(periksa, fp, sort_keys=True, indent=4)
                   else:
                        cl.sendText(msg.to,"Tidak ada dalam banlist\nKirim kontak lagi atau matikan")
              
               elif msg.to in periksa["addwl"]:
		  if msg.contentMetadata["mid"] in periksa["wl"]:
			cl.sendText(msg.to, "Contact is ready in whitelist")
		  else:
                        periksa["wl"][msg.contentMetadata["mid"]] = True
                        with open('settingan.json', 'w') as fp:
    			   json.dump(periksa, fp, sort_keys=True, indent=4)
			cl.sendText(msg.to, "Succes add to whitelist")
	       elif msg.to in periksa["delwl"]:
                   if msg.contentMetadata["mid"] in periksa["wl"]:
                        del periksa["wl"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted succes")
                        with open('settingan.json', 'w') as fp:
    			   json.dump(periksa, fp, sort_keys=True, indent=4)
                   else:
                        cl.sendText(msg.to,"Contact not found")
               elif msg.to in periksa["addtarget"]:
                   if msg.contentMetadata["mid"] in periksa["target"]:
                      cl.sendText(msg.to, "Contact already in list")
                   else:
                        periksa["target"][msg.contentMetadata["mid"]] = True
                        with open('settingan.json', 'w') as fp:
                              json.dump(periksa, fp, sort_keys=True, indent=4)
                        cl.sendText(msg.to, "Added 􀜁􀄯ok􏿿")
               elif msg.to in periksa["deltarget"]:
                   if msg.contentMetadata["mid"] in periksa["target"]:
                        del periksa["target"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted 􀜁􀄯ok􏿿")
                        with open('settingan.json', 'w') as fp:
                             json.dump(periksa, fp, sort_keys=True, indent=4)
                   else:
                        cl.sendText(msg.to,"Contact not in list")                        
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["Timeline:"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return                         
               
            
            elif pesan is None:
                return
            if "help" == pesan.lower():
                    cl.sendText(msg.to,helpMessage)
            elif "autojoin:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("autojoin:","")
                if xres == "off":
                    periksa['autojoin'] = "off"
                    cl.sendText(msg.to,"Auto Join OFF")
                elif xres == "on":
                    periksa['autojoin'] = "all"
                    cl.sendText(msg.to,"Auto Join Everyone")
                elif xres == "wl":
                    periksa['autojoin'] = "wl"
                    cl.sendText(msg.to,"Auto Join Whitelist Only")
            elif "autolike:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("autolike:","")
                if xres == "off":
                    periksa['autolike'] = False
                    cl.sendText(msg.to,"Already off")
                elif xres == "on":
                    periksa['autolike'] = True
                    cl.sendText(msg.to,"Already on")
            elif "autoadd:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("autoadd:","")
                if xres == "off":
                    periksa['autoadd'] = False
                    cl.sendText(msg.to,"already off")
                elif xres == "on":
                    periksa['autoadd'] = True
                    cl.sendText(msg.to,"already on")
            elif "purge:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("purge:","")
                if xres == "off":
                    del periksa['autopurge'][msg.to]
                    cl.sendText(msg.to,"Auto Purge OFF")
                elif xres == "on":
                    periksa['autopurge'][msg.to] = True
                    cl.sendText(msg.to,"Auto Purge ON")
          #  elif "mimic:" in pesan.lower():
          #      xpesan = pesan.lower()
           #     xres = xpesan.replace("mimic:","")
            #    if xres == "0":
           #         periksa['mimic'] = False
          #          cl.sendText(msg.to,"Mimic off")
            #    elif xres == "1":
          #          periksa['mimic'] = True
           #         cl.sendText(msg.to,"Mimic ON")
            elif "qr:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("qr:","")
                if xres == "off":
                    del periksa['lockqr'][msg.to]
                    cl.sendText(msg.to,"Lock QR OFF")
                elif xres == "on":
                    periksa['lockqr'][msg.to] = True
                    cl.sendText(msg.to,"Lock QR ON")
            elif "cancelall:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("cancelall:","")
                if xres == "off":
                    del periksa['autocancel'][msg.to]
                    cl.sendText(msg.to,"Normal invite succesful")
                elif xres == "on":
                    periksa['autocancel'][msg.to] = True
                    cl.sendText(msg.to,"Just you can invite")
            elif "protection:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("protection:","")
                if xres == "off":
                    del periksa['protect'][msg.to]
                    del periksa['lockqr'][msg.to]
                    del periksa['autopurge'][msg.to]
                    del periksa['autocancel'][msg.to]
                    cl.sendText(msg.to,"Already off")
                elif xres == "on":
                    periksa['protect'][msg.to] = True
                    periksa['autocancel'][msg.to] = True
                    periksa['lockqr'][msg.to] = True
                    periksa['autopurge'][msg.to] = True
                    cl.sendText(msg.to,"Already on")
            elif "set view" in pesan.lower():
                if msg.to in periksa['protect']:
                    protect = "ON"
                else:
                    protect = "OFF"
                if msg.to in periksa['autopurge']:
                    autopurge = "ON"
                else:
                    autopurge = "OFF"
                if msg.to in periksa['lockqr']:
                    lockqr = "ON"
                else:
                    lockqr = "OFF"
                if msg.to in periksa['autocancel']:
                    autocancel = "ON"
                else:
                    autocancel = "OFF"
                if periksa['autolike'] == True:
                    autolike = "ON"
                else:
                     autolike = "OFF"
                if periksa['autoadd'] == True:
                    autoadd = "ON"
                else:
                     autoadd = "OFF"
                if periksa['autorejc'] == True:
                    autorejc = "ON"
                else:
                     autorejc = "OFF"
                if periksa['autojoin'] == "all":
                    autojoin = "Everyone"
                elif periksa['autojoin'] == "wl":
                     autojoin = "Whitelist Only"
                else:
                    autojoin = "OFF"
                cl.sendText(msg.to," \n  THE STATUS BOT  \n         Settings      \n\n\n Protect: %s\n cancel: %s\n Purge: %s\n Lock QR: %s\n YOUR SELF\n Autolike: %s\n Autoadd: %s\n Rejectinvite: %s\n Autojoin: %s"%(protect,autocancel,autopurge,lockqr,autolike,autoadd,autorejc,autojoin))
 
          #  elif "mimic add @" in pesan.lower():
            #    if 'MENTION' in msg.contentMetadata.keys() != None:
         #           names = re.findall(r'@(\w+)', msg.text)
           #         mention = ast.literal_eval(msg.contentMetadata['MENTION'])
          #          mentionees = mention['MENTIONEES']
            #        G = cl.getGroupIdsJoined()
         #           cgroup = cl.getGroups(G)
             #       ngroup = ""
            #        for mention in mentionees:
             #           periksa['tmimic'][mention['M']] = True
             #           cl.sendText(msg.to,"Target Mimic has been Added")
              #          with open('settingan.json', 'w') as fp:
               #             json.dump(periksa, fp, sort_keys=True, indent=4)
         #   elif "mimic del @" in pesan.lower():
          #      if 'MENTION' in msg.contentMetadata.keys() != None:
        #            names = re.findall(r'@(\w+)', msg.text)
          #          mention = ast.literal_eval(msg.contentMetadata['MENTION'])
        #            mentionees = mention['MENTIONEES']
           #         G = cl.getGroupIdsJoined()
          #          cgroup = cl.getGroups(G)
          #          ngroup = ""
         #           for mention in mentionees:
           #             del periksa['tmimic'][mention['M']]
          #              cl.sendText(msg.to,"Target Mimic has been Removed")
          #              with open('settingan.json', 'w') as fp:
         #                   json.dump(periksa, fp, sort_keys=True, indent=4)
            elif "rejectinvite:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("rejectinvite:","")
                if xres == "off":
                    periksa['autorejc'] = False
                    cl.sendText(msg.to,"Already off")
                elif xres == "on":
                    periksa['autorejc'] = True
                    cl.sendText(msg.to,"Already on")
            elif "reject all invite" in pesan.lower():
                cl.sendText(msg.to,"Waiting....")
                g1 = cl.getGroupIdsInvited()
                kk.sendText(msg.to,"Waiting....")
                g2 = kk.getGroupIdsInvited()
                ka.sendText(msg.to,"Waiting....")
                g3 = ka.getGroupIdsInvited()
                for x in g1:
                    cl.rejectGroupInvitation(x)
                pass
                cl.sendText(msg.to,"Succes")
                for x in g2:
                    kk.rejectGroupInvitation(x)
                pass
                kk.sendText(msg.to,"Succes")
                for x in g3:
                    ka.rejectGroupInvitation(x)
                pass
                ka.sendText(msg.to,"Succes")
            elif "*kicker" == pesan.lower():
                     G = cl.getGroup(msg.to)
                     G.preventJoinByTicket = False
                     cl.updateGroup(G)
                     Ti = cl.reissueGroupTicket(msg.to)
                     kk.acceptGroupInvitationByTicket(msg.to,Ti)
                     ka.acceptGroupInvitationByTicket(msg.to,Ti)
                     X = kk.getGroup(msg.to)
                     X.preventJoinByTicket = True
                     kk.updateGroup(X) 
	    elif "lurking:on" == pesan.lower():
                if msg.to in sider['readPoint']:
                    try:
                        del sider['readPoint'][msg.to]
                        del sider['readMember'][msg.to]
			del sider['setTime'][msg.to]
                    except:
                        pass
                    sider['readPoint'][msg.to] = msg.id
                    sider['readMember'][msg.to] = ""
		    sider['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    sider['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
    			   json.dump(sider, fp, sort_keys=True, indent=4)
    		    cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                        del sider['readPoint'][msg.to]
                        del sider['readMember'][msg.to]
			del sider['setTime'][msg.to]
                    except:
                        pass
                    sider['readPoint'][msg.to] = msg.id
                    sider['readMember'][msg.to] = ""
		    sider['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    sider['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
    			   json.dump(sider, fp, sort_keys=True, indent=4)
		    cl.sendText(msg.to,"Lurking On")
                    print sider
            elif "lurking:off" == pesan.lower():
                if msg.to not in sider['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                       del sider['readPoint'][msg.to]
                       del sider['readMember'][msg.to]
                       del sider['setTime'][msg.to]
                    except:
                       pass
                    cl.sendText(msg.to,"Lurking off")
            elif "lurkers" == pesan.lower():
                    if msg.to in sider['readPoint']:
                        if sider["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in sider["ROM"][msg.to].items():
                                chiya.append(rom[1])
                                
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
			    xpesan = 'Lurkers:\n'
                            for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                            msg.contentType = 0
		    
                            print zxc
                            msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(sider['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                            lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            print lol
                            msg.contentMetadata = lol
                            try:
                              cl.sendMessage(msg)
                            except Exception as error:
                                  print error
                            pass
			    
			
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
            elif "my groups" == pesan.lower():
                    G = cl.getGroupIdsJoined()
                    cgroup = cl.getGroups(G)
                    ngroup = ""
                    for x in range(len(cgroup)):
                       ngroup += "\n["+ str(x) +"] " + cgroup[x].name + " | Members: " + str(len(cgroup[x].members))
                    pass
                    cl.sendText(msg.to,"List Group:\n%s\n\nTotal Group: %s"%(ngroup,str(len(cgroup))))
	    elif "lookup:" in pesan:
                   umid = pesan.replace(bname+' lookup:','')
		   msg.contentType = 13
                   msg.text = None
                   msg.contentMetadata = {'mid': umid}
                   cl.sendMessage(msg)
	    elif "search @" in pesan.lower():
                   if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    G = cl.getGroupIdsJoined()
                    cgroup = cl.getGroups(G)
                    ngroup = ""
                    for mention in mentionees:
                      for x in range(len(cgroup)):
                        gMembMids = [contact.mid for contact in cgroup[x].members]
                        if mention['M'] in gMembMids:
                            ngroup += "\n" + cgroup[x].name + " | Members: " + str(len(cgroup[x].members))    
		      if ngroup == "":
		        cl.sendText(msg.to, "Tidak ditemukan")
		      else:
                        cl.sendText(msg.to,"Ada di Group:\n%s\n"%(ngroup))
            elif "ourl" == pesan.lower():
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Link This Group http://line.me/R/ti/g/"+gurl)
                else:
                    pass
                    
            elif "curl" == pesan.lower():
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Qr closed ✓")
                else:
                    pass
            elif "gid" == pesan.lower():
                cl.sendText(msg.to,msg.to)
            elif "mymid" == pesan.lower():
                cl.sendText(msg.to,msg.from_)
            elif pesan.lower() in ["sp","speed","speed","Stest","stest"]:
                start = time.time()
                cl.sendText(msg.to, "Wait for a sec....")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s second" % (elapsed_time))
                kk.sendText(msg.to, "%s second" % (elapsed_time))
                ka.sendText(msg.to, "%s second" % (elapsed_time))
            elif "*kicker @bye" == pesan.lower():
                ka.leaveGroup(msg.to)
                kk.leaveGroup(msg.to)
            elif "wl add:on" == pesan.lower():
                periksa["addwl"][msg.to] = True
                cl.sendText(msg.to,"Send contact")
            elif "wl add:off" == pesan.lower():
                del periksa["addwl"][msg.to]
                cl.sendText(msg.to,"Stoped send contact")
            elif "del wl:on" == pesan.lower():
                periksa["delwl"][msg.to] = True
                cl.sendText(msg.to,"Send contact")
            elif "del wl:off" == pesan.lower():
                del periksa["delwl"][msg.to]
                cl.sendText(msg.to,"Stoped send contact")
            elif msg.text in ["Tag on"]:
                if wait["detectMention"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["detectMention"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Tag off"]:
                if wait["detectMention"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["detectMention"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif "join " in pesan:
                 xlink = msg.text.replace("join ","")
                 ticket = xlink.split("/ti/g/")
                 try:
                   group = cl.findGroupByTicket(ticket[1])
                   cl.acceptGroupInvitationByTicket(group.id,ticket[1])
                   kk.acceptGroupInvitationByTicket(group.id,ticket[1])
                   ka.acceptGroupInvitationByTicket(group.id,ticket[1])
                   cl.sendText(msg.to,"Succes Join to %s"%(group.name))
                   kk.sendText(msg.to,"Succes Join to %s"%(group.name))
                   ka.sendText(msg.to,"Succes Join to %s"%(group.name))
                 except Exception as error:
                   cl.sendText(msg.to,"Failed\n %s"%(error))
                   kk.sendText(msg.to,"Failed\n %s"%(error))
            elif "ban:on" == pesan.lower():
                periksa["addbanmode"][msg.to] = True
                cl.sendText(msg.to,"Send contact for add to banlist")
            elif "ban:off" == pesan.lower():
                del periksa["addbanmode"][msg.to]
                cl.sendText(msg.to,"Stoped send contact")
            elif "unban:on" == pesan.lower():
                periksa["delbanmode"][msg.to] = True
                cl.sendText(msg.to,"Send contact for delete banlist")
            elif "unban:off" == pesan.lower():
                del periksa["delbanmode"][msg.to]
                cl.sendText(msg.to,"Stoped send contact")
            elif "wl add @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in periksa["wl"]:
                            cl.sendText(msg.to,"The contact is ready in whitelist")
                        else:
                            periksa["wl"][mention['M']] = True
                            with open('settingan.json', 'w') as fp:
                                json.dump(periksa, fp, sort_keys=True, indent=4)
                            cl.sendText(msg.to,"Succes add to whitelist")
            elif "wl del @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in periksa["wl"]:
                            del periksa["wl"][mention['M']]
                            with open('settingan.json', 'w') as fp:
                                json.dump(periksa, fp, sort_keys=True, indent=4)
                            cl.sendText(msg.to,"Deleted")
                        else:
                            cl.sendText(msg.to,"User not in whitleist")
            elif "ban add @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in periksa["banlist"]:
                            cl.sendText(msg.to,"User added to banlist")
                        elif mention['M'] in Bots or mention['M'] in periksa["wl"]:
                            cl.sendText(msg.to,"Can't ban whitelist -_-")
                        else:
                            periksa["banlist"][mention['M']] = True
                            with open('settingan.json', 'w') as fp:
                                json.dump(periksa, fp, sort_keys=True, indent=4)
                            cl.sendText(msg.to,"")
            elif "ban del @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in periksa["banlist"]:
                            del periksa["banlist"][mention['M']]
                            with open('settingan.json', 'w') as fp:
                                json.dump(periksa, fp, sort_keys=True, indent=4)
                            cl.sendText(msg.to,"Deleted")
                        else:
                            cl.sendText(msg.to,"User not in banlist")
            elif "banlist" == pesan.lower():
                if periksa["banlist"] == {}:
                    cl.sendText(msg.to,"Nothing")
                else:
                    mc = []
                    for mi_d in periksa["banlist"]:
                        mc.append(mi_d)
                    pass
                    cban = cl.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n☠ ".join(str(i) for i in nban)
                    cl.sendText(msg.to,"😂Banlist😂\n\n😎 %s\n\nAll Banlist: %s"%(jo,str(len(cban))))
            elif "cek ban" == pesan.lower():
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in periksa["banlist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = []
                    for mm in matched_list:
                        cocoa.append(mm)
                    pass
                    cban = cl.getContacts(cocoa)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n☠ ".join(str(i) for i in nban)
                    if cocoa != []:
                        cl.sendText(msg.to,"😁Banlist in Groups😁 \n 😎 %s\n\nAll banlist: %s"%(jo,str(len(cban))))
                    else:
                        cl.sendText(msg.to,"Nothing")
            elif "whitelist" == pesan.lower():
                if periksa["wl"] == {}:
                    cl.sendText(msg.to,"Nothing")
                else:
                    mc = []
                    for mi_d in periksa["wl"]:
                        mc.append(mi_d)
                    pass
                    cban = cl.getContacts(mc)
                    nban = []
                    for x in range(len(cban)):
                        nban.append(cban[x].displayName)
                    pass
                    jo = "\n✧ ".join(str(i) for i in nban)
                    cl.sendText(msg.to,"😚whitelist\n\n√ %s\n\nAll Whitelist: %s"%(jo,str(len(cban))))
         #   elif "mimic target" == pesan.lower():
          #      if periksa["tmimic"] == {}:
        #            cl.sendText(msg.to,"Tidak ada")
         #       else:
      #              mc = []
        #            for mi_d in periksa["tmimic"]:
        #                mc.append(mi_d)
     #               pass
      #              cban = cl.getContacts(mc)
      #              nban = []
       #             for x in range(len(cban)):
       #                 nban.append(cban[x].displayName)
        #            pass
        #            jo = "\n✧ ".join(str(i) for i in nban)
         #           cl.sendText(msg.to,"✧ Mimic Target List: ✧\n\n✧ %s\n\nTotal: %s"%(jo,str(len(cban))))
	    elif "me" == pesan.lower():
                      msg.contentType = 13
                      msg.text = None
                      msg.contentMetadata = {'mid': msg.from_}
                      cl.sendMessage(msg)
	    elif "Cancel" == pesan.lower():
                    group = cl.getGroup(msg.to)
                    if group.invitee is None:
                        cl.sendText(op.message.to, "Nothing invite pending")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to, "Berhasil membatalkan " + str(len(group.invitee)) + " undangan" )
	    elif "kick " in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            kicker=random.choice(KAC)
                            kicker.kickoutFromGroup(msg.to, [mention['M']])
                        except:
                            try:
                                kicker=random.choice(KAC)
                                kicker.kickoutFromGroup(msg.to, [mention['M']])
                            except:
                                cl.kickoutFromGroup(msg.to, [mention['M']])
            elif "kill " in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
			    cl.findAndAddContactsByMid(mention['M'])
                            cl.kickoutFromGroup(msg.to, [mention['M']])
                            cl.inviteIntoGroup(msg.to, [mention['M']])
                            cl.cancelGroupInvitation(msg.to, [mention['M']])
                        except Exception as error:
			    print error
                            try:
				kk.findAndAddContactsByMid(mention['M'])
                                kk.kickoutFromGroup(msg.to, [mention['M']])
                                kk.inviteIntoGroup(msg.to, mention['M'])
                                kk.cancelGroupInvitation(msg.to, [mention['M']])
                            except:
                                  ka.findAndAddContactsByMid(mention['M'])
                                  ka.kickoutFromGroup(msg.to, mention['M'])
                                  ka.inviteIntoGroup(msg.to, [mention['M']])
                                  ka.cancelGroupInvitation(msg.to, [mention['M']])
            elif "fuck off" == pesan.lower():
                if msg.toType == 2:
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if g.mid not in Bots:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Target not found")
                    else:
                        for target in targets:
                            try:
                                kicker=random.choice(KAC)
                                kicker.kickoutFromGroup(msg.to, [target])
                            except:
                                try:
                                    kicker=random.choice(KAC)
                                    kicker.kickoutFromGroup(msg.to, [target])
                                except:
                                    kicker=random.choice(KAC)
                                    kicker.kickoutFromGroup(msg.to, [target])
                                
            elif "kill ban" == pesan.lower():
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in periksa["banlist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Noting banlist in this groups")
                        return
                    for jj in matched_list:
                      try:
                        kicker=random.choice(KAC)
                        kicker.kickoutFromGroup(msg.to,[jj])
                      except:
                         try:
                            kicker=random.choice(KAC)
                            kicker.kickoutFromGroup(msg.to,[jj])
                         except:
                            cl.kickoutFromGroup(msg.to,[jj])
                    kk.sendText(msg.to,"Fuck off")
            elif "ล้างดำ" == pesan.lower():
                periksa['banlist'] = {}
                with open('settingan.json', 'w') as fp:
                    json.dump(periksa, fp, sort_keys=True, indent=4)
                cl.sendText(msg.to,"Waiting......")
                cl.sendText(msg.to,"Succesfull")
            elif "clear whitelist" in pesan.lower():
                periksa['wl'] = {}
                with open('settingan.json', 'w') as fp:
                    json.dump(periksa, fp, sort_keys=True, indent=4)
                cl.sendText(msg.to,"Waiting......")
                cl.sendText(msg.to,"succesfull")
            elif "Ginfo" == pesan:
              if msg.toType == 2:
                g = cl.getGroup(msg.to)
                gc = g.creator.mid
                gn = g.creator.displayName
                msg.contentType = 13
                msg.contentMetadata = {'mid': gc}
                try:
                    kk.sendText(msg.to,"This group has been created by "+str(gn))
                    kk.sendMessage(msg)
                except:
                    try:
                        ka.sendText(msg.to,"This group has been created by "+str(gn))
                        ka.sendMessage(msg)
                    except:                       
                       cl.sendText(msg.to,"Assists must exist in the group")
            elif "msg " in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("msg ","")
                periksa['message'] = xres
                cl.sendText(msg.to,"Message Change to "+xres)
            elif "msg chek" in pesan.lower():
                if periksa['message'] == "":
                    cl.sendText(msg.to,"None")
                else:
                    cl.sendText(msg.to,"Message : \n"+str(periksa['message']))
            elif "Follow @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            cl.cloneContactProfile(mention['M'])
			    cl.sendText(msg.to,"Succesfull")
                        except Exception as error:
                            print error
            elif "gift" == pesan.lower():
                msg.contentType = 9
                msg.contentMetadata = { 'STKPKGID':'2821',
                                        'PRDTYPE':'STICKER',
                                        'MSGTPL':'4'}
                msg.text = None
                cl.sendMessage(msg)
            elif "gift2" == pesan.lower():
                msg.contentType = 9
                msg.contentMetadata = { 'STKPKGID':'3172',
                                        'PRDTYPE':'STICKER',
                                        'MSGTPL':'2'}
                msg.text = None
                cl.sendMessage(msg)
            elif "gift3" == pesan.lower():
                msg.contentType = 9
                msg.contentMetadata = { 'STKPKGID':'4333',
                                        'PRDTYPE':'STICKER',
                                        'MSGTPL':'3'}
                msg.text = None
                cl.sendMessage(msg)
            elif "gift4" == pesan.lower():
                msg.contentType = 9
                msg.contentMetadata = { 'STKPKGID':'3002',
                                        'PRDTYPE':'STICKER',
                                        'MSGTPL':'4'}
                msg.text = None
                cl.sendMessage(msg)
            elif "gift5" == pesan.lower():
                msg.contentType = 9
                msg.contentMetadata = { 'STKPKGID':'6083',
                                        'PRDTYPE':'STICKER',
                                        'MSGTPL':'1'}
                msg.text = None
                cl.sendMessage(msg)
#---------------------------------------------------------					
            elif "runing time" in pesan.lower():
                elpsd = datetime.now() - strt
                cl.sendText(msg.to,'Duration : %s'%(elpsd))
            elif "restore" in pesan.lower():
                cl.updateDisplayPicture(backup.pictureStatus)
                cl.updateProfile(backup)
            elif "copas @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = cl.getProfile()
                            backup.displayName = profile.displayName
                            backup.statusMessage = profile.statusMessage
                            backup.pictureStatus = profile.pictureStatus
                            cl.cloneContactProfile(mention['M'])
                            cl.sendText(msg.to,"Done")
                        except Exception as error:
                            pass
#======================================================#
            elif msg.text in ["Tag1","Tag1"]:
                cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ\n\n" + str(wait["tag1"]))
            elif msg.text in ["Tag2","Tag2"]:
                cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ\n\n" + str(wait["tag2"]))
            elif "Tag1: " in msg.text:
                    wait["tag1"] = msg.text.replace("Tag1: ","")
                    cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ")
            elif "Tag2: " in msg.text:
                    wait["tag2"] = msg.text.replace("Tag2: ","")
                    cl.sendText(msg.to,"ข้อความแทคล่าสุดคือ")
#----------------------------------------------------------------------------
#-------------Fungsi Tagall User Start---------------#
            elif "Tag" in msg.text :
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Neobots\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg)
            elif "allpict" == pesan.lower():
                if msg.toType == 2:
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if g.mid not in Bots:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Target not found")
                    else:
                        for target in targets:
                            try:
                                profile = cl.getContact(target)
                                cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                            except:
                                pass                    
#=========อ่านแทค================
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","Contact:on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact is already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact is already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","Contact:off"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact is already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact is already off")
                    else:
                        cl.sendText(msg.to,"done")                               
            elif "gift on:" in pesan.lower():
                xpesan = pesan.lower()
                xres = xpesan.replace("gift on:","")
                jumlah = int(xres)
                if jumlah >= 10000:
                    cl.sendText(msg.to,"Out of range, Baka!!!!!!! ")
                else:
                  periksa["gift2jumlah"] = jumlah
                  periksa["gift2"][msg.to] = True
                  cl.sendText(msg.to,"send contact") 
            elif "Spam " in pesan:
                   txt = pesan.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                  #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "ARE YOU FUCKING KIDDING ME? ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "ARE YOU FUCKING KIDDING ME? ")                  
            elif "Group member bc:" in pesan:
		xres = pesan.replace("Group member bc:","")
		group = cl.getGroup(msg.to)
		mem = [contact.mid for contact in group.members]
		cmem = cl.getContacts(mem)
		nc = ""
		for x in range(len(cmem)):
		  try:
                    cl.sendText(cmem[x].mid,xres)
                    nc += "\n" + cmem[x].displayName
		  except:
		   pass
                pass
                cl.sendText(msg.to,"Success BC to :\n%s\n\nTotal Members: %s"%(nc,str(len(cmem))))
            elif "Say " in pesan:
                xres = pesan.replace("Say ","")
                cl.sendText(msg.to,xres)
                ka.sendText(msg.to,xres)
                kk.sendText(msg.to,xres)
            elif "Group bc:" in pesan:
                xres = pesan.replace("Group bc:","")
                G = cl.getGroupIdsJoined()
                cgroup = cl.getGroups(G)
                ngroup = ""
                for x in range(len(cgroup)):
                    cl.sendText(cgroup[x].id,xres)
                    ngroup += "\n" + cgroup[x].name
                pass
                cl.sendText(msg.to,"Success BC to :\n%s\n\nTotal Group: %s"%(ngroup,str(len(cgroup))))
            elif "Kontak bc:" in pesan:
                xres = pesan.replace("Kontak bc:","")
                C = cl.getAllContactIds()
                cmem = cl.getContacts(C)
                nc = ""
                for x in range(len(cmem)):
                    cl.sendText(cmem[x].mid,xres)
                    nc += "\n" + cmem[x].displayName
                pass
                cl.sendText(msg.to,"Success BC to :\n%s\n\nAll Contact: %s"%(nc,str(len(cmem))))
            elif "Fuck " in pesan:
                       ulti0 = pesan.replace("Fuck ","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       kicker=random.choice(KFC)
                       kicker.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.0001)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kicker.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)                
            elif "ping" == pesan:
                try:
                    wb.findAndAddContactsByMid(msg.to)
                    kk.findAndAddContactsByMid(msg.to)
                except:
                    pass
                cl.sendText(msg.to,"pong")
                kk.sendText(msg.to,"pong")
                ka.sendText(msg.to,"pong")
    #        elif "Hmmm" == pesan:
    #            try:
    #                wb.findAndAddContactsByMid(msg.to)
 #                   kk.findAndAddContactsByMid(msg.to)
    #            except:
    #                pass
    #            cl.sendText(msg.to,"(︶︹︺)")
    #            kk.sendText(msg.to,"(︶︹︺)")
  #              ka.sendText(msg.to,"(︶︹︺)")
    #            kb.sendText(msg.to,"(︶︹︺)")
    #           wb.sendText(msg.to,"(︶︹︺)")
    #            wa.sendText(msg.to,"(︶︹︺)")
     #       elif "FUCK" == pesan:
   #             try:
  #                  wb.findAndAddContactsByMid(msg.to)
   #                 kk.findAndAddContactsByMid(msg.to)
      #          except:
  #                  pass
      #          cl.sendText(msg.to,"┌∩┐(◣_◢)┌∩┐")
     #           kk.sendText(msg.to,"┌∩┐(◣_◢)┌∩┐")
      #          ka.sendText(msg.to,"┌∩┐(◣_◢)┌∩┐")
      #          kb.sendText(msg.to,"┌∩┐(◣_◢)┌∩┐")
      #          wb.sendText(msg.to,"┌∩┐(◣_◢)┌∩┐")
      #          wa.sendText(msg.to,"┌∩┐(◣_◢)┌∩┐")
	    elif "get mid @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                           cl.sendText(msg.to,str(mention['M']))
                        except Exception as e:
                            print e
	    elif "get status @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = cl.getContact(mention['M'])
                            cl.sendText(msg.to,str(profile.statusMessage))
                        except Exception as e:
                            print e
	    elif "get name @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = cl.getContact(mention['M'])
                            cl.sendText(msg.to,str(profile.displayName))
                        except Exception as e:
                            print e
	    elif "steal pict @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            profile = cl.getContact(mention['M'])
                            cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                        except Exception as e:
                            print e
	    elif "steal cover @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            cu = cl.channel.getCover(mention['M'])
                            cl.sendImageWithURL(msg.to,cu)
                        except Exception as e:
                            print e
	    elif "reboot" == pesan.lower():
                cl.sendText(msg.to,"Restarted")
                restart_program()
                print "Restart"
            elif "Lookup" in pesan:
                   umid = pesan.replace('Lookup','')
		   msg.contentType = 13
                   msg.text = None
                   msg.contentMetadata = {'mid': umid}
                   cl.sendMessage(msg)
            elif "Spam:" in pesan:
                   lol = pesan.replace('Spam:','')
                   hehe = lol.split("@")
                   cl.sendText(msg.to,"Spamming >> "+str(hehe[1])+"\nGroups Name:"+str(hehe[0]))
                   kk.findAndAddContactsByMid(hehe[1])
                   ka.findAndAddContactsByMid(hehe[1])
                   for zx in range(0,400):
                       cl.createGroup(str(hehe[0]),[hehe[1]])
                       kk.createGroup(str(hehe[0]),[hehe[1]])
                       ka.createGroup(str(hehe[0]),[hehe[1]])
                   cl.sendText(msg.to,"Done")

            elif "Leave:" in pesan:
                group_name = pesan.replace('Leave:','')
                G = cl.getGroupIdsJoined()
                cgroup = cl.getGroups(G)
                for x in range(len(cgroup)):
                  if group_name == cgroup[x].name:
                      try:
                         cl.leaveGroup(cgroup[x].id)
                      except:
                          pass
                      try:
                         kk.leaveGroup(cgroup[x].id)
                      except:
                          pass
                      try:
                         ka.leaveGroup(cgroup[x].id)
                      except:
                          pass
                cl.sendText(msg.to,"Succes")
                
            elif "Wikipedia:" in pesan:
                cari = pesan.replace('Wikipedia:','')
                wikipedia.set_lang("id")
                try:
                   ny = wikipedia.summary(cari)
                except Exception as ny:
                  print ny
                cl.sendText(msg.to,"%s"%(ny))
            elif pesan.lower() == '!เชิญคน':
                inviting = True
                kk.sendText(msg.to,"Send a contact to invite.")
            elif "restore" in pesan.lower():
                cl.updateDisplayPicture(backup.pictureStatus)
                cl.updateProfile(backup)                
				
#---------------------------------------------------------
            elif msg.text.lower() == 'welcome':
                ginfo = cl.getGroup(msg.to)
                cl.sendImageWithURL(msg.to,"http://www.imgion.com/images/01/Kids-are-welcoming-you.jpeg")
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :" )
                try:
                    group = cl.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    cl.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    cl.sendMessage(M)
            elif "play " in pesan.lower():
                xpesan = pesan.lower()
                songname = xpesan.replace("play ","")
                params = {'songname':songname}
                r=requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.parse.urlencode(params))
                data = r.text
                data=json.loads(data)
                for song in data:
                    cl.sendAudioWithURL(msg.to,song[4])
            elif "music " in pesan.lower():
                xpesan = pesan.lower()
                songname = xpesan.replace("music ","")
                params = {'songname':songname}
                r=requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.parse.urlencode(params))
                data = r.text
                data=json.loads(data)
                
                for song in data:
                    cl.sendText(msg.to,"Music\n\n%s (%s)\nDownload: %s"%(song[0],song[1],song[4]))
            elif "lirik " in pesan.lower():
                xpesan = pesan.lower()
                songname = xpesan.replace("lirik ","")
                params = {'songname':songname}
                r=requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.parse.urlencode(params))
                data = r.text
                data=json.loads(data)
                for song in data:
                    cl.sendText(msg.to,"%s \n\n %s"%(song[0],song[5]))                    
                                   
#===============[Tranlate Command]====================
            elif "Translate" == pesan:
                try:
                  kk.sendText(msg.to,"Command Translate:\n\n Tr-id to Indonesia \n Tr-th to Thai \n Tr-en to English \n Tr-ja to Japan \n Tr-ms to Malay \n Tr-jw to Jawa \n Tr-it to Italia \n Tr-my to Myanmar \n Tr-fr to French \n Tr-ar to Arabic")
                except:
                   try:
                      ka.sendText(msg.to,"Command Translate:\n\n Tr-id to Indonesia \n Tr-th to Thai \n Tr-en to English \n Tr-ja to Japan \n Tr-ms to Malay \n Tr-jw to Jawa \n Tr-it to Italia \n Tr-my to Myanmar \n Tr-fr to French \n Tr-ar to Arabic")
                   except:
                     cl.sendText(msg.to,"Your kicker must exist in the group")  
            elif "Tr-id" in pesan:
                 xres = pesan.replace("Tr-id","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'id')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-en" in pesan:
                 xres = pesan.replace("Tr-en","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'en')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-ja" in pesan:
                 xres = pesan.replace("Tr-ja","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'ja')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-th" in pesan:
                 xres = pesan.replace("Tr-th","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'th')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-jw" in pesan:
                 xres = pesan.replace("Tr-jw","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'jw')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-ar" in pesan:
                 xres = pesan.replace("Tr-ar","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'ar')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-ms" in pesan:
                 xres = pesan.replace("Tr-ms","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'ms')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-my" in pesan:
                 xres = pesan.replace("Tr-my","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'my')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-it" in pesan:
                 xres = pesan.replace("Tr-it","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'it')
                 cl.sendText(msg.to,str(trans))
            elif "Tr-fr" in pesan:
                 xres = pesan.replace("Tr-fr","")
                 xres1 = xres.lstrip()
                 xres2 = xres1.replace("","")
                 xres3 = xres2.rstrip()
                 _text = xres3
                 trans = translate(_text,'fr')
                 cl.sendText(msg.to,str(trans))
                 
                 

#===============[Assist Command]====================
            elif "Kicker1 status:" in pesan:  
              xres = pesan.replace("Kicker1 status:","")
	      if len(xres.decode('utf-8')) <= 500:
                profile = kk.getProfile()
                profile.statusMessage = xres
                kk.updateProfile(profile)
                kk.sendText(msg.to,"Succes")
            elif "Kicker2 status:" in pesan:
              xres = pesan.replace("Kicker2 status:","")
	      if len(xres.decode('utf-8')) <= 500:
                profile = wb.getProfile()
                profile.statusMessage = xres
                ka.updateProfile(profile)
                ka.sendText(msg.to,"Succes")
                
            elif "Kicker1 rename:" in pesan:
              xres = pesan.replace("Kicker1 rename:","")
	      if len(xres.decode('utf-8')) <= 20:
                profile = kk.getProfile()
                profile.displayName = xres
                kk.updateProfile(profile)
                kk.sendText(msg.to,"Succes")
            elif "Kicker2 rename:" in pesan:
              xres = pesan.replace("Kicker2 rename:","")
	      if len(xres.decode('utf-8')) <= 20:
                profile = wb.getProfile()
                profile.displayName = xres
                ka.updateProfile(profile)
                ka.sendText(msg.to,"Succes")
                
            elif "kicker1 copy @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            kk.cloneContactProfile(mention['M'])
			    kk.sendText(msg.to,"Done")
                        except Exception as error:
                            print error
            elif "kicker2 copy @" in pesan.lower():
                if 'MENTION' in msg.contentMetadata.keys() != None:
                    names = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        try:
                            wb.cloneContactProfile(mention['M'])
			    wb.sendText(msg.to,"Succes")
                        except Exception as error:
                            print error
        if op.type == 59:
            print op

            elif msg.text in ["/อยู่ป่าว"]:
                        cl.sendText(msg.to,"ยังอยู่ๆ")

    except Exception as error:
        print error


def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by •VIP♕ҨัՁਙุЮℓℓ丂ს• \nรับทำSelfbotกันรัน\n line.me/ti/p/~xaonxaou69.")
            kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by •VIP♕ҨัՁਙุЮℓℓ丂ს• \nรับทำSelfbotกันรัน\n line.me/ti/p/~xaonxaou69.")
            ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by •VIP♕ҨัՁਙุЮℓℓ丂ს• \nรับทำSelfbotกันรัน\n line.me/ti/p/~xaonxaou69.")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
def resetchat():
    while True:
        try:
            if periksa['autolike'] == True:
	      autolike()
	      time.sleep(300)
	      autolike()
              time.sleep(300)
	      autolike()
              time.sleep(300)
	      autolike()
              time.sleep(300)
	      autolike()
              time.sleep(200)
            else:
                pass
            kk.removeAllMessages(mid)
            ka.removeAllMessages(Bmid)
            print "reset"
            time.sleep(4040)
        except:
            pass
thread2 = threading.Thread(target=resetchat)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
