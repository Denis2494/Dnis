#~~ Made By - Famz Botz ~~
#~~ New Lib - 2021 ~~
#~~ Creator - Bardiansyah ~~
from function import *

class Bardian_syah(object):
    def __init__(self, myToken="", myApp="", type=None):
        self.famz = Famz_botz(myToken, myApp)
        print('success login bot '+str(type))
        self.mid = self.famz.getProfile().mid
        self.myToken = myToken
        self.myApp = myApp
        self.creator = ["ua19b7ef5349d083d65a82f92f8ed596d","uda02187337ba3b0fdf369bde4a1ff498","uef55be133e16cb3a65747006e0ca77cf"]
        self.dataku = livejson.File("newdata.json")
        self.owner = self.dataku["owner"]
        self.admin = self.dataku["admin"]
        self.staff = self.dataku["staff"]
        self.bots = self.dataku["bots"]
        self.asist = self.dataku["asist"]
        self.antijs = self.dataku["ajs"]
        self.groupcontrol = self.dataku["gid"]
        self.induk = [self.mid]
        self.kick = self.dataku["kicker"]
        for a in self.creator:
            if a not in self.dataku["owner"]:
                self.owner.append(a)
            if a not in self.dataku["admin"]:
                self.admin.append(a)
            if a not in self.dataku["staff"]:
                self.staff.append(a)
        for a in self.induk:
            if a not in self.dataku["kicker"]:
                self.kick.append(a)
        if type != None: 
            self.type = type
        else:
            self.type = type
        if str(self.type) not in self.asist:
            self.asist[str(self.type)] = self.mid
        if self.mid not in self.bots:
            self.bots[self.mid] = self.type
        if self.type == 100:
            for i in self.induk:
                if i in self.bots:
                    del self.dataku["bots"][self.mid]
                if i not in self.dataku["ajs"]:
                    self.dataku["ajs"].append(i)
        self.countKick = 0
        self.countInvite = 0
        self.countCancel = 0
        self.wait = {
            'famzFoto': {},
            "keyCommand": "",
            'addadmin': False,
            'addstaff': False,
            'addblacklist': False,
            'delladmin': False,
            'dellstaff': False,
            'dellblacklist': False,
            'autoJoin': True
        }
        self.read = {
            "readPoint":{},
            "readMember":{},
            "readTime":{},
            "ROM":{}
        }
        self.cctv = {
            "sider":"I can see you,,\nCome here chat with me",
            "cyduk":{},
            "point":{},
            "sidermem":{}
        }
        self.protectqr = self.dataku["protectqr"]
        self.protectjoin = self.dataku["protectjoin"]
        self.protectinvite = self.dataku["protectinvite"]
        self.protectkick = self.dataku["protectkick"]
        self.protectcancel = self.dataku["protectcancel"]
        self.protectname = self.dataku["protectname"]
        self.proantijs = self.dataku["Proantijs"]
        self.HelpMessage = """    ===[[🎓Drack__Angel🎓]]===
╔═══════════════════╗
╠🇮🇩● help
╠🇮🇩● restart
╠🇮🇩● cekbot
╠🇮🇩● cek count
╠🇮🇩● cekmid
╠🇮🇩● mid
╠🇮🇩● ping
╠🇮🇩● absen
╠🇮🇩● remove chat
╠🇮🇩● in
╠🇮🇩● out
╠🇮🇩● outall:grup
╠🇮🇩● outfrom [number]
╠🇮🇩● (type)outfrom [number]
╠🇮🇩● stay
╠🇮🇩● js out
╠🇮🇩● set:control
╠🇮🇩● sp
╠🇮🇩● status
╠🇮🇩● allpro on/off
╠🇮🇩● projoin on/off
╠🇮🇩● allproon [number]
╠🇮🇩● allprooff [number]
╠🇮🇩● proall:grup
╠🇮🇩● inviteme [number]
╠🇮🇩● banlist
╠🇮🇩● cbl [number]
╠🇮🇩● ceban
╠🇮🇩● contact bot
╠🇮🇩● listadmin
╠🇮🇩● listprotect
╠🇮🇩● gruplist
╠🇮🇩● (type)gruplist
╠🇮🇩● (type)cek pending
╠🇮🇩● (type)joinke [num]
╠🇮🇩● listbot
╠🇮🇩● tagall(type)
╠🇮🇩● kick(type) @
╠🇮🇩● hajar [name]
╠🇮🇩● mid @
╠🇮🇩● addowner @
╠🇮🇩● dellowner @
╠🇮🇩● addadmin @
╠🇮🇩● delladmin @
╠🇮🇩● addstaff @
╠🇮🇩● dellstaff @
╠🇮🇩● addbots @
╠🇮🇩● dellbots @
╠🇮🇩● add(type)
╠🇮🇩● addfriend(type) @
╠🇮🇩● (type)name: [name]
╠🇮🇩● jsname: [name]
╠🇮🇩● (type)clonefoto
╠🇮🇩● (type)upfoto
╠🇮🇩● setkey [text]
╠🇮🇩● resetkey
╠🇮🇩● admin:on/off
╠🇮🇩● staff:on/off
╠🇮🇩● ban:on/off
╚═══════════════════╝"""
    def cek(self, mid):
        if mid not in self.creator and mid not in self.owner and mid not in self.admin and mid not in  self.staff and mid not in self.bots and mid not in self.antijs:
            return True
        else:
            return False
    def black(self, mid):
        if mid not in self.dataku["blacklist"]:
            self.dataku['blacklist'][mid] = True
        else:
            pass
    def command(self, text):
        pesan = text.lower()
        if pesan.startswith(self.wait["keyCommand"]):
            cmd = pesan.replace(self.wait["keyCommand"],"")
        else:
            cmd = "command"
        return cmd
    
    def upfoto(self, myToken, myApp):
        file = open("cfoto.py", "w")
        file.write("from upfoto import *\nfrom datetime import datetime, timedelta\nimport time, random, sys, json, codecs, threading, asyncio, glob, re, string, os, six, ast, pytz, atexit, traceback,requests\npub = LINE('{}',appName='{}')\na = 'img.jpg'\ntry:pub.updateProfilePicture(a)\nexcept:pub.updateProfilePicture(a)".format(myToken, myApp))
        file.close()
        time.sleep(1)
        os.system('python3 cfoto.py')

    def receive_message(self, op):
        try:
            if op.type in [12, 123]:
                self.countInvite += 1
            if op.type in [18, 132]:
                self.countKick += 1
            if op.type in [31, 125]:
                self.countCancel += 1
            if op.type in [55]:
                if op.param2 in self.dataku["blacklist"]:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.famz.deleteOtherFromChat(op.param1, [op.param2])
            if op.type in [5]:
                if op.param1 in self.creator and op.param1 in self.owner:
                    try:
                        self.famz.findAndAddContactsByMid(op.param1)
                    except:
                        pass
                else:
                    data = """Auto Add By - Famz__Botz
╔═══════════════════╗
╠> Thanks For Add Me
╠═══════════════════
╠> Open Order
╠═══════════════════
╠> Bots Protect
╠> Self Bot
╠> Vps
╠> Primery Token
╠═══════════════════
╠> Pm My-creator
╠> castello_bardian
╚═══════════════════╝
Id Line > https://line.me/ti/p/~castello_bardian"""
                    self.famz.sendMessage(op.param1, data)
            if op.type in [25, 26]:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 2:
                    if msg.toType == 0:
                        to = receiver
                    if msg.toType == 2:
                        to = receiver
                    if msg.contentType == 1:
                        if msg._from in self.owner:
                            if self.wait["famzFoto"][self.mid] == True:
                                if self.type == 0:
                                    path = self.famz.downloadMsg(msg_id, "img.jpg")
                                self.wait["famzFoto"][self.mid] = False
                                self.upfoto(self.myToken, self.myApp)
                                self.famz.sendMessage(to,"Succes Change Picture Bots")
#=======ADD Admin=====================
                if msg.contentType == 13:
                    if msg._from in self.owner:
                        if self.wait["addadmin"] == True:
                            if msg.contentMetadata["mid"] in self.admin:
                                self.famz.sendMessage(to,"Contact itu sudah jadi admin")
                                self.wait["addadmin"] = False
                            else:
                                self.admin.append(msg.contentMetadata["mid"])
                                self.wait["addadmin"] = False
                                self.famz.sendMessage(to,"Berhasil menambahkan ke admin")
                        if self.wait["delladmin"] == True:
                            if msg.contentMetadata["mid"] in self.admin:
                                self.admin.remove(msg.contentMetadata["mid"])
                                self.famz.sendMessage(to,"Berhasil menghapus Admin")
                            else:
                                self.wait["delladmin"] = False
                                self.famz.sendMessage(to,"Contact itu bukan Admin")
#=======ADD Staaff=====================
                if msg.contentType == 13:
                    if msg._from in self.admin:
                        if self.wait["addadmin"] == True:
                            if msg.contentMetadata["mid"] in self.staff:
                                self.famz.sendMessage(to,"Contact itu sudah jadi staff")
                                self.wait["addstaff"] = False
                            else:
                                self.staff.append(msg.contentMetadata["mid"])
                                self.wait["addstaff"] = False
                                self.famz.sendMessage(to,"Berhasil menambahkan ke staff")
                        if self.wait["dellstaff"] == True:
                            if msg.contentMetadata["mid"] in self.staff:
                                self.staff.remove(msg.contentMetadata["mid"])
                                self.famz.sendMessage(to,"Berhasil menghapus staff")
                            else:
                                self.wait["dellstaff"] = False
                                self.famz.sendMessage(to,"Contact itu bukan staff")
#=======ADD Blacklist=====================
                if msg.contentType == 13:
                    if msg._from in self.admin:
                        if self.wait["addblacklist"] == True:
                            if msg.contentMetadata["mid"] in self.dataku["blacklist"]:
                                self.famz.sendMessage(to,"Contact itu sudah jadi blacklist")
                                self.wait["addblacklist"] = False
                            else:
                                self.dataku['blacklist'][msg.contentMetadata["mid"]] = True
                                self.wait["addblacklist"] = False
                                self.famz.sendMessage(to,"Berhasil menambahkan ke blacklist")
                        if self.wait["dellblacklist"] == True:
                            if msg.contentMetadata["mid"] in self.dataku["blacklist"]:
                                del self.dataku['blacklist'][msg.contentMetadata["mid"]]
                                self.famz.sendMessage(to,"Berhasil menghapus blacklist")
                            else:
                                self.wait["dellblacklist"] = False
                                self.famz.sendMessage(to,"Contact itu bukan blacklist")
#=======================================
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        cmd = self.command(text)
                        if cmd == str(self.type)+"upfoto":
                            if msg._from in self.admin:
                                self.wait["famzFoto"][self.mid] = True
                                self.famz.sendMessage(to,"Please Send New Photo.....")

                        elif cmd.startswith(str(self.type)+"name: "):
                            if msg._from in self.admin:
                                separate = msg.text.split(" ")
                                string = msg.text.replace(separate[0] + " ","")
                                if len(string) <= 10000000000:
                                    profile = self.famz.getProfile()
                                    profile.displayName = string
                                    self.famz.updateProfile(profile)
                                    self.famz.sendMessage(to,"Succes Change Name to " + string + "")

                        if cmd.startswith(str(self.type)+'clonefoto '):
                            if msg._from in self.admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for y in targets:
                                    self.famz.cloneContactPoto(y)
                                    self.famz.sendMessage(to, "Succes clone foto")

                        elif cmd.startswith("mykey"):
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.famz.sendMessage(to, "「Mykey」\nSetkey bot mu「 " + str(self.wait["keyCommand"]) + " 」")

                        elif cmd.startswith("setkey "):
                            if msg._from in self.admin:
                                if self.type == 0:
                                    sep = text.split(" ")
                                    key = text.replace(sep[0] + " ","")
                                    if key in [""," ","\n",None]:
                                        self.famz.sendMessage(msg.to, "Gagal mengganti key")
                                    else:
                                        self.wait["keyCommand"] = str(key).lower()
                                        self.famz.sendMessage(to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif cmd.startswith("resetkey"):
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.wait["keyCommand"] = ""
                                    self.famz.sendMessage(to, "「Setkey」\nSetkey mu kembali ke awal")

                        if cmd == "help":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.famz.sendMessage(to, self.HelpMessage)

                        if cmd == "mid":
                                self.famz.sendMessage(to, msg._from)

                        if cmd == "ping":
                            if msg._from in self.admin:
                                    self.famz.sendMessage(to,'pong')

                        elif ("Mid " in msg.text):
                            if msg._from in self.admin:
                                if self.type == 0:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    mi = self.famz.getContact(key1)
                                    self.famz.sendMessage(to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                                    self.famz.sendMessage(to, None, contentMetadata={'mid': key1}, contentType=13)

                        if cmd == "cekmid":
                            if msg._from in self.admin:
                                self.famz.sendMessage(to, self.mid)

                        if cmd == "restart":
                            if msg._from in self.creator:
                                if self.type == 0:
                                    self.famz.sendMessage(to,'wait 3 minutes')
                                    python = sys.executable
                                    os.execl(python, python, *sys.argv)

                        if cmd == "tagall"+str(self.type):
                            if msg._from in self.admin:
                                group = self.famz.getChats([to])
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    self.famz.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        if cmd == "sp":
                            if msg._from in self.admin:
                                start = time.time()
                                self.famz.getGroupIdsJoined()
                                total = time.time() - start
                                self.famz.sendMessage(to,"%.10f" % (total/3))

                        if cmd == "absen":
                            if msg._from in self.admin:
                                self.famz.sendMessage(to, self.dataku["absen"])

                        if cmd == "cekbot":
                            if msg._from in self.admin:
                                try:self.famz.deleteOtherFromChat(to, ["u6fa1f3f543b597933b6f7f9f47edb3e4"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has1 == "OK":sil1 = "✓ strong"
                                else:sil1 = "✘ down"
                                try:self.famz.cancelChatInvitation(to, ["u6fa1f3f543b597933b6f7f9f47edb3e4"]);has2 = "OK"
                                except:has2 = "NOT"
                                if has2 == "OK":sil2 = "✓ strong"
                                else:sil2 = "✘ down"
                                try:self.famz.inviteIntoChat(to, [self.mid]);has3 = "OK"
                                except:has3 = "NOT"
                                if has3 == "OK":sil3 = "✓ strong"
                                else:sil3 = "✘ down"
                                try:self.famz.findAndAddContactsByMid("ua19b7ef5349d083d65a82f92f8ed596d");has4 = "OK"
                                except:has4 = "NOT"
                                if has4 == "OK":sil4 = "✓ strong"
                                else:sil4 = "✘ down"
                                data = """Creator - By >Famz__Botz
>status kick       : {}
>status cancel  : {}
>status invite    : {}
>status add       : {}""".format(sil1,sil2,sil3,sil4)
                                self.famz.sendMessage(to, data)

                        if cmd == "in":
                            if msg._from in self.owner:
                                if self.type == 0:
                                    Ticket = self.famz.reissueChatTicket(to).ticketId
                                    chat = self.famz.getChats([to])
                                    chat.chats[0].extra.groupExtra.preventedJoinByTicket = False
                                    self.famz.updateChat(chat.chats[0],4)
                                    for zzz in self.groupcontrol:
                                        try:
                                            self.famz.sendMessage(zzz,'http://line.me/R/ti/g/'+Ticket)
                                        except:pass
                                    time.sleep(1)
                                    chat = self.famz.getChats([to])
                                    chat.chats[0].extra.groupExtra.preventedJoinByTicket = True
                                    self.famz.updateChat(chat.chats[0],4)
                                    for i in self.antijs:
                                        self.famz.findAndAddContactsByMid(i)
                                    grup = self.famz.getChats([to])
                                    membList = grup.chats[0].extra.groupExtra.inviteeMids
                                    for x in self.antijs:
                                        if x not in membList:
                                            self.famz.inviteIntoChat(to, [x])
                                            self.famz.sendMessage(to,'Anti-Js Stay')

                        if cmd == "stay":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    for i in self.antijs:
                                        self.famz.findAndAddContactsByMid(i)
                                    self.famz.inviteIntoChat(to,self.antijs)
                                    self.famz.sendMessage(to,'Anti-Js Stay')

                        if cmd == "out":
                            if msg._from in self.owner:
                                if self.type == 100:
                                    return
                                if msg.to not in self.groupcontrol:
                                    targets = []
                                    for x in self.dataku["ajs"]:
                                        if self.dataku["ajs"] == []:
                                            pass
                                        else:
                                            targets.append(x)
                                    for i in targets:
                                        if self.type == 0:
                                            grup = self.famz.getChats([to])
                                            membList = grup.chats[0].extra.groupExtra.inviteeMids
                                            membList1 = grup.chats[0].extra.groupExtra.memberMids
                                            if i in membList:
                                                self.famz.cancelChatInvitation(to,[i])
                                            if i in membList1:
                                                self.famz.deleteOtherFromChat(to,[i])
                                                self.famz.deleteSelfFromChat(to)
                                    self.famz.deleteSelfFromChat(to)
                                else:
                                    self.famz.sendMessage(to,'tidak bisa keluar dari group control')

                        if cmd == "js out":
                            if msg._from in self.admin:
                                if self.type == 100:
                                    if msg.to not in self.groupcontrol:
                                        try:
                                            self.famz.deleteSelfFromChat(to)
                                        except:
                                            pass
                                    else:
                                        self.famz.sendMessage(to,'tidak bisa keluar dari group control')

                        if cmd == "outall:grup":
                            if msg._from in self.owner:
                                groups = self.famz.getGroupIdsJoined()
                                for y in groups:
                                    if y not in self.protectkick and y not in self.groupcontrol:
                                        try:
                                            self.famz.deleteSelfFromChat(y)
                                            self.famz.sendMessage(to, "succes leave")
                                        except:
                                            pass

                        if cmd == "status":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    md = ">>> Drack_____Angel <<<\n"
                                    if msg.to in self.protectqr: md+=">Protecturl「ON」\n"
                                    else: md+=">Protecturl「OFF」\n"
                                    if msg.to in self.protectjoin: md+=">Protectjoin「ON」\n"
                                    else: md+=">Protectjoin「OFF」\n"
                                    if msg.to in self.protectkick: md+=">Protectkick「ON」\n"
                                    else: md+=">Protectkick「OFF」\n"
                                    if msg.to in self.protectinvite: md+=">Protectinvite「ON」\n"
                                    else: md+=">Protectinvite「OFF」\n"
                                    if msg.to in self.protectcancel: md+=">Protectcancel「ON」\n"
                                    else: md+=">Protectcancel「OFF」\n"
                                    if msg.to in self.protectname: md+=">Protectname「ON」\n"
                                    else: md+=">Protectname「OFF」\n"
                                    if msg.to in self.proantijs: md+=">Anti-Js「ON」\n"
                                    else: md+=">Anti-Js「OFF」\n"
                                    self.famz.sendMessage(msg.to, md)

                        if cmd == "allpro on":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    try:
                                        if to not in self.proantijs:
                                            self.proantijs.append(to)
                                        else:pass
                                        if to not in self.protectqr:
                                            self.protectqr.append(to)
                                        else:pass
                                        if to not in self.protectkick:
                                            self.protectkick.append(to)
                                        else:pass
                                        if to not in self.protectcancel:
                                            self.protectcancel.append(to)
                                        else:pass
                                        if to not in self.protectname:
                                            self.protectname.append(to)
                                            if to not in self.dataku["Proname"]:
                                                self.dataku["Proname"][to] = str(self.famz.getGroup(to).name)
                                        else:pass
                                        if to not in self.protectinvite:
                                            self.protectinvite.append(to)
                                        else:pass
                                        time.sleep(1)
                                        self.famz.sendMessage(to,"protect enabled for > "+str(self.famz.getGroup(to).name))
                                    except Exception as e:
                                        print (e)

                        if cmd == "allpro off":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    try:
                                        if msg.to in self.proantijs:
                                            self.proantijs.remove(to)
                                        else:pass
                                        if msg.to in self.protectqr:
                                            self.protectqr.remove(to)
                                        else:pass
                                        if msg.to in self.protectkick:
                                            self.protectkick.remove(to)
                                        else:pass
                                        if msg.to in self.protectcancel:
                                            self.protectcancel.remove(to)
                                        else:pass
                                        if msg.to in self.protectname:
                                            self.protectname.remove(to)
                                            if msg.to in self.dataku['Proname']:
                                                del self.dataku['Proname'][to]
                                        else:pass
                                        if msg.to in self.protectinvite:
                                            self.protectinvite.remove(to)
                                            self.famz.sendMessage(to,"protect disabled for > "+str(self.famz.getGroup(to).name))
                                        else:
                                            self.famz.sendMessage(to,"protect disabled for > "+str(self.famz.getGroup(to).name))
                                    except Exception as e:
                                        print (e)

                        if cmd == "projoin on":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    if msg.to not in self.protectjoin:
                                        self.protectjoin.append(to)
                                        self.famz.sendMessage(to,"Protect Join Enable")
                                    else:
                                        self.famz.sendMessage(to,"Protect Join Active")

                        if cmd == "projoin off":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    if msg.to in self.protectjoin:
                                        self.protectjoin.remove(to)
                                        self.famz.sendMessage(to,"Protect Join Disable")
                                    else:
                                        self.famz.sendMessage(to,"Protect Join Disable")

                        if cmd == "proall:grup":
                            if msg._from in self.owner:
                                if self.type == 0:
                                    groups = self.famz.getGroupIdsJoined()
                                    for target in groups:
                                        try:
                                            if target not in self.proantijs:
                                                self.proantijs.append(target)
                                            else:pass
                                            if target not in self.protectqr:
                                                self.protectqr.append(target)
                                            else:pass
                                            if target not in self.protectkick:
                                                self.protectkick.append(target)
                                            else:pass
                                            if target not in self.protectcancel:
                                                self.protectcancel.append(target)
                                            else:pass
                                            if target not in self.protectname:
                                                self.protectname.append(target)
                                                if target not in self.dataku["Proname"]:
                                                    for i in groups:
                                                        if i not in self.dataku["Proname"]:
                                                            self.dataku["Proname"][i] = str(self.famz.getGroup(target).name)
                                            else:pass
                                            if target not in self.protectinvite:
                                                self.protectinvite.append(target)
                                            else:pass
                                            time.sleep(1)
                                            self.famz.sendMessage(to,"protect enabled for "+str(self.famz.getGroup(target).name))
                                        except Exception as e:
                                            print (e)

                        if cmd.startswith('allproon'):
                            if msg._from in self.owner:
                                if self.type == 0:
                                    sep = text.split(" ")
                                    txt = text.replace(sep[0] + " ","")
                                    groups = self.famz.getGroupIdsJoined()
                                    target = groups[int(txt)-1]
                                    grup = self.famz.getGroup(target)
                                    try:
                                        if target not in self.proantijs:
                                            self.proantijs.append(target)
                                        else:pass
                                        if target not in self.protectqr:
                                            self.protectqr.append(target)
                                        else:pass
                                        if target not in self.protectkick:
                                            self.protectkick.append(target)
                                        else:pass
                                        if target not in self.protectcancel:
                                            self.protectcancel.append(target)
                                        else:pass
                                        if target not in self.protectname:
                                            self.protectname.append(target)
                                            for i in groups:
                                                if i not in self.dataku["Proname"]:
                                                    self.dataku["Proname"][i] = str(grup.name)
                                        else:pass
                                        if target not in self.protectinvite:
                                            self.protectinvite.append(target)
                                        else:pass
                                        time.sleep(1)
                                        self.famz.sendMessage(to,"protect enabled for "+str(self.famz.getGroup(target).name))
                                    except Exception as e:
                                        print (e)

                        if cmd.startswith('allprooff'):
                            if msg._from in self.owner:
                                if self.type == 0:
                                    sep = text.split(" ")
                                    txt = text.replace(sep[0] + " ","")
                                    groups = self.famz.getGroupIdsJoined()
                                    target = groups[int(txt)-1]
                                    targets = self.famz.getGroup(target)
                                    try:
                                        if target in self.proantijs:
                                            self.proantijs.remove(target)
                                        else:pass
                                        if target in self.protectqr:
                                            self.protectqr.remove(target)
                                        else:pass
                                        if target in self.protectkick:
                                            self.protectkick.remove(target)
                                        else:pass
                                        if target in self.protectcancel:
                                            self.protectcancel.remove(target)
                                        else:pass
                                        if target in self.protectname:
                                            self.protectname.remove(target)
                                            if target in self.dataku['Proname']:
                                                del self.dataku['Proname'][target]
                                        else:pass
                                        if target in self.protectinvite:
                                            self.protectinvite.remove(target)
                                        else:pass
                                        time.sleep(1)
                                        self.famz.sendMessage(to,"protect enabled for "+str(targets.name))
                                    except Exception as e:
                                        print (e)

                        if cmd == str(self.type)+"gruplist":
                            if msg._from in self.admin:
                                groups = self.famz.getGroupIdsJoined()
                                tx = "╔─[【List Group】]\n"
                                num = 0
                                for gc in groups:
                                    num += 1
                                    tx += "╠❍"+str(num)+". "+self.famz.getGroup(gc).name+"\n"
                                tx += '╚─────────'
                                self.famz.sendMessage(to,tx)

                        if cmd == "gruplist":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    groups = self.famz.getGroupIdsJoined()
                                    tx = "╔─[【List Group】]\n"
                                    num = 0
                                    for gc in groups:
                                        num += 1
                                        tx += "╠❍"+str(num)+". "+self.famz.getGroup(gc).name+"\n"
                                    tx += '╚─────────'
                                    self.famz.sendMessage(to,tx)

                        elif cmd.startswith("outfrom"):
                            if msg._from in self.owner:
                                sep = text.split(" ")
                                spl = text.replace(sep[0] + " ","")
                                gid = self.famz.getGroupIdsJoined()
                                target = gid[int(spl)-1]
                                groupid = self.famz.getGroup(target).name
                                self.famz.sendMessage(target,"semua bot di keluarkan oleh owner dari luar group")
                                for i in gid:
                                    if i not in self.groupcontrol and i not in self.protectqr and i not in self.protectjoin and i not in self.protectkick and i not in self.protectinvite and i not in self.protectcancel and i not in self.proantijs and i not in self.protectname:
                                        try:
                                            self.famz.deleteSelfFromChat(target)
                                            time.sleep(1)
                                            self.famz.sendMessage(to,"sukses mengeluarkan semua bot dari group {}".format(groupid))
                                        except:
                                            pass

                        elif cmd.startswith(str(self.type)+"outfrom"):
                            if msg._from in self.owner:
                                sep = text.split(" ")
                                spl = text.replace(sep[0] + " ","")
                                gid = self.famz.getGroupIdsJoined()
                                target = gid[int(spl)-1]
                                groupid = self.famz.getGroup(target).name
                                self.famz.sendMessage(target,"semua bot di keluarkan oleh owner dari luar group")
                                for i in gid:
                                    if i not in self.groupcontrol and i not in self.protectqr and i not in self.protectjoin and i not in self.protectkick and i not in self.protectinvite and i not in self.protectcancel and i not in self.proantijs and i not in self.protectname:
                                        try:
                                            self.famz.deleteSelfFromChat(target)
                                            time.sleep(1)
                                            self.famz.sendMessage(to,"sukses mengeluarkan semua bot dari group {}".format(groupid))
                                        except:
                                            pass

                        elif cmd.startswith("inviteme"):
                            if msg._from in self.owner:
                                if self.type == 0:
                                    sep = text.split(" ")
                                    spl = text.replace(sep[0] + " ","")
                                    gid = self.famz.getGroupIdsJoined()
                                    target = gid[int(spl)-1]
                                    targets = sender
                                    try:
                                        group = self.famz.getGroup(target).name
                                        self.famz.findAndAddContactsByMid(targets)
                                        self.famz.inviteIntoChat(target, [targets])
                                        self.famz.sendMessage(to,"Invited to\n " + str(group))
                                    except Exception as e:
                                        print (e)

                        if cmd == "listprotect":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    md = ""
                                    me = ""
                                    mf = ""
                                    mg = ""
                                    a = 0
                                    gid = self.protectqr
                                    for group in gid:
                                        chat = self.famz.getGroup(group)
                                        a = a + 1
                                        end = '\n'
                                        ma += str(a) + ". " +chat.name + "\n"
                                    gid = self.protectkick
                                    for group in gid:
                                        chat = self.famz.getGroup(group)
                                        a = a + 1
                                        end = '\n'
                                        mb += str(a) + ". " +chat.name + "\n"
                                    gid = self.protectjoin
                                    for group in gid:
                                        chat = self.famz.getGroup(group)
                                        a = a + 1
                                        end = '\n'
                                        md += str(a) + ". " +chat.name + "\n"
                                    gid = self.protectcancel
                                    for group in gid:
                                        chat = self.famz.getGroup(group)
                                        a = a + 1
                                        end = '\n'
                                        mc += str(a) + ". " +chat.name + "\n"
                                    gid = self.protectinvite
                                    for group in gid:
                                        chat = self.famz.getGroup(group)
                                        a = a + 1
                                        end = '\n'
                                        me += str(a) + ". " +chat.name + "\n"
                                    gid = self.protectname
                                    for group in gid:
                                        chat = self.famz.getGroup(group)
                                        a = a + 1
                                        end = '\n'
                                        mf += str(a) + ". " +chat.name + "\n"
                                    gid = self.proantijs
                                    for group in gid:
                                        chat = self.famz.getGroup(group)
                                        a = a + 1
                                        end = '\n'
                                        mg += str(a) + ". " +chat.name + "\n"
                                    self.famz.sendMessage(to,"「◄━━◈⟦Famz_Protection⟧◈━━►」\n\n「✭」 PROTECT URL :\n"+ma+"\n「✭」 PROTECT KICK :\n"+mb+"\n「✭」 PROTECT JOIN :\n"+md+"\n「✭」 PROTECT CANCEL:\n"+mc+"\n「✭」 PROTECT INVITE:\n"+me+"\n「✭」 PROTECT NAME:\n"+mf+"\n「✭」 Anti-Js:\n"+mg+"\n\nTotal「%s」Grup diamankan" %(str(len(self.protectqr))))

                        if cmd == "listadmin":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    ma = ""
                                    mb = ""
                                    mc = ""
                                    a = 0
                                    b = 0
                                    c = 0
                                    for m_id in self.owner:
                                        a = a + 1
                                        end = '\n'
                                        ma += str(a) + ". " +self.famz.getContact(m_id).displayName + "\n"
                                    for m_id in self.admin:
                                        b = b + 1
                                        end = '\n'
                                        mb += str(b) + ". " +self.famz.getContact(m_id).displayName + "\n"
                                    for m_id in self.staff:
                                        c = c + 1
                                        end = '\n'
                                        mc += str(c) + ". " +self.famz.getContact(m_id).displayName + "\n"
                                    self.famz.sendMessage(to, "===[[🎓List__Owner🎓]]===\n"+ma+"===[[🎓List__Admin🎓]]===\n"+mb+"===[[🎓List__Staff🎓]]===\n"+mc+"\n\nᴛᴏᴛᴀʟ :「%s」Squad\n====================" %(str(len(self.owner)+len(self.admin)+len(self.staff))))

                        if cmd == "listbot":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    ma = ""
                                    mb = ""
                                    a = 0
                                    for m_id in self.bots:
                                        a = a + 1
                                        end = '\n'
                                        ma += str(a) + ". " +self.famz.getContact(m_id).displayName + "\n"
                                    for m_id in self.antijs:
                                        a = a + 1
                                        end = '\n'
                                        mb += str(a) + ". " +self.famz.getContact(m_id).displayName + "\n"
                                    self.famz.sendMessage(to, "===[[🎓List__Bots🎓]]===\n"+ma+"\n>Anti - Js\n"+mb+"\nᴛᴏᴛᴀʟ :「%s」Bots\n====================" %(str(len(self.bots)+len(self.antijs))))

                        if cmd == "banlist":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    if self.dataku["blacklist"] == {}:
                                        self.famz.sendMessage(to, "Not have blacklist")
                                    else:
                                        mc = "[ Black - List ]\n"
                                        a = 0
                                        for mid in self.dataku['blacklist']:
                                            a = a + 1
                                            mc += str(a) + ". " + self.famz.getContact(mid).displayName + "\n"
                                        self.famz.sendMessage(to,mc)

                        if cmd.startswith('cbl '):
                            if msg._from in self.owner:
                                if self.type == 0:
                                    sep = text.split(" ")
                                    txt = text.replace(sep[0] + " ","")
                                    ma = []
                                    for y in self.dataku["blacklist"]:
                                        ma.append(y)
                                    target = ma[int(txt)-1]
                                    try:
                                        del self.dataku['blacklist'][target]
                                        self.famz.sendMessage(to, "Succes Remove >> {} from blacklist".format(self.famz.getContact(target).displayName))
                                    except:
                                        pass

                        if cmd == "ceban":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    ragets = self.famz.getContacts(self.dataku["blacklist"])
                                    mc = "「%i」" % len(ragets)
                                    self.dataku["blacklist"] = {}
                                    self.famz.sendMessage(to, mc+": Succes Remove Blacklist")

                        if cmd == "contact bot":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    ma = ""
                                    for i in self.dataku['bots']:
                                        ma = self.famz.getContact(i)
                                        self.famz.sendMessage(to, None, contentMetadata={'mid': i}, contentType=13)
                                    mb = ""
                                    for i in self.dataku['ajs']:
                                        mb = self.famz.getContact(i)
                                        self.famz.sendMessage(to, None, contentMetadata={'mid': i}, contentType=13)

                        if cmd == str(self.type)+"cek pending":
                            if msg._from in self.owner:
                                gid = self.famz.getGroupIdsInvited()
                                num = 0
                                g = ""
                                for i in gid:
                                    g += "%i. " % num + "%s" % (self.famz.getGroup(i).name + " (%s)\n" % (str (len (self.famz.getGroup(i).members))))
                                    num = (num+1)
                                self.famz.sendMessage(msg.to,"Groups:\n\n"+ g + "\nTotal Groups : " + str(len(gid)))

                        if cmd.startswith(str(self.type)+'joinke '):
                            if msg._from in self.owner:
                                sep = text.split(" ")
                                txt = text.replace(sep[0] + " ","")
                                ma = self.famz.getGroupIdsInvited()
                                target = ma[int(txt)-1]
                                try:
                                    self.famz.acceptChatInvitation(target)
                                    self.famz.sendMessage(to, "Succes Join >> {}".format(self.famz.getGroup(target).name))
                                except:
                                    pass
#============Kickout================================================================
                        if cmd.startswith('kick'+str(self.type)):
                            if msg._from in self.admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for y in targets:
                                    if self.cek(y):
                                        try:
                                            self.black(y)
                                            self.famz.deleteOtherFromChat(to, [y])
                                        except:
                                            pass
                        
                        elif cmd.startswith("hajar"):
                            if msg._from in self.owner:
                                if self.type == self.type:
                                    split = text.split(" ")
                                    name = text.replace(split[0] + " ","")
                                    target = []
                                    member = self.famz.getChats([to]).chats[0].extra.groupExtra.memberMids
                                    for i in member:
                                        if name in self.famz.getContact(i).displayName:
                                            X = self.famz.getProfile(i).mid
                                            target.append(X)
                                    for y in target:
                                        if self.cek(y):
                                            try:
                                                self.black(y)
                                                self.famz.deleteOtherFromChat(to, [y])
                                            except Exception as e:
                                                print (e)
#============Add admin,staff,BL========================================================
                        if cmd == "add"+str(self.type):
                            if msg._from in self.creator:
                                for i in self.dataku["kicker"]:
                                    if i not in self.famz.getAllContactIds():
                                        if i not in self.mid:
                                            try:
                                                self.famz.findAndAddContactsByMid(i)
                                                self.famz.sendMessage(to, "sukses")
                                            except:
                                                self.famz.sendMessage(to, "Limit Add")
                                    else:
                                        self.famz.sendMessage(to, "Sudah Berteman")

                        if cmd.startswith('addfriend'+str(self.type)):
                            if msg._from in self.admin:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for y in targets:
                                    if y not in self.mid:
                                        try:
                                            self.famz.findAndAddContactsByMid(y)
                                            self.famz.sendMessage(to, "succes")
                                        except:
                                            pass

                        if cmd.startswith('addowner'):
                            if msg._from in self.creator:
                                if self.type == 0:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for y in targets:
                                        if y not in self.owner:
                                            self.owner.append(y)
                                            self.famz.sendMessage(to, "Succes Add owner")
                                        else:
                                            self.famz.sendMessage(to, "Sudah Menjadi owner")

                        if cmd.startswith('dellowner'):
                            if msg._from in self.creator:
                                if self.type == 0:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for y in targets:
                                        if y in self.owner:
                                            self.owner.remove(y)
                                            self.famz.sendMessage(to, "Succes Remove owner")
                                        else:
                                            self.famz.sendMessage(to, "Bukan owner")

                        if cmd.startswith('addadmin'):
                            if msg._from in self.owner:
                                if self.type == 0:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for y in targets:
                                        if y not in self.admin:
                                            self.admin.append(y)
                                            self.famz.sendMessage(to, "Succes Add Admin")
                                        else:
                                            self.famz.sendMessage(to, "Sudah Menjadi Admin")

                        if cmd.startswith('delladmin'):
                            if msg._from in self.owner:
                                if self.type == 0:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for y in targets:
                                        if y in self.admin:
                                            self.admin.remove(y)
                                            self.famz.sendMessage(to, "Succes Remove Admin")
                                        else:
                                            self.famz.sendMessage(to, "Bukan Admin")

                        if cmd.startswith('addstaff'):
                            if msg._from in self.admin:
                                if self.type == 0:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for y in targets:
                                        if y not in self.staff:
                                            self.staff.append(y)
                                            self.famz.sendMessage(to, "Succes Add staff")
                                        else:
                                            self.famz.sendMessage(to, "Sudah Menjadi staff")

                        if cmd.startswith('dellstaff'):
                            if msg._from in self.admin:
                                if self.type == 0:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for y in targets:
                                        if y in self.staff:
                                            self.staff.remove(y)
                                            self.famz.sendMessage(to, "Succes Remove staff")
                                        else:
                                            self.famz.sendMessage(to, "Bukan staff")

                        if cmd == "admin:on":
                            if msg._from in self.owner:
                                if self.type == 0:
                                    self.wait['addadmin'] = True
                                    self.famz.sendMessage(to, "Send Contact")
                        if cmd == "admin:off":
                            if msg._from in self.owner:
                                if self.type == 0:
                                    self.wait['delladmin'] = True
                                    self.famz.sendMessage(to, "Send Contact")
                        if cmd == "staff:on":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.wait['addstaff'] = True
                                    self.famz.sendMessage(to, "Send Contact")
                        if cmd == "staff:off":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.wait['dellstaff'] = True
                                    self.famz.sendMessage(to, "Send Contact")
                        if cmd == "ban:on":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.wait['addblacklist'] = True
                                    self.famz.sendMessage(to, "Send Contact")
                        if cmd == "ban:off":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.wait['dellblacklist'] = True
                                    self.famz.sendMessage(to, "Send Contact")

                        if cmd == "refresh":
                            if msg._from in self.admin:
                                if self.type == 0:
                                    self.wait['addadmin'] = False
                                    self.wait['delladmin'] = False
                                    self.wait['addstaff'] = False
                                    self.wait['dellstaff'] = False
                                    self.wait['addblacklist'] = False
                                    self.wait['dellblacklist'] = False
                                    self.famz.sendMessage(to, "Suscces Refresh All cmd")
#========Sider=========================================================================
                        if cmd == "cek count":
                            if msg._from in self.admin:
                                tx = """╔═══════════════════╗
╠> Count Kick: {}
╠> Count Invite: {}
╠> Count cancel: {}
╚═══════════════════╝""".format(self.countKick,self.countInvite,self.countCancel)
                                self.famz.sendMessage(to, tx)

                        if cmd == "set:control":
                            if msg._from in self.creator:
                                if self.type == 0:
                                    if self.dataku['gid'] == []:
                                        pass
                                    else:
                                        self.dataku['gid'] = []
                                    self.groupcontrol.append(msg.to)
                                    self.famz.sendMessage(to, "Succes set control")

                        if "/ti/g/" in text.lower():
                            if msg._from in self.dataku['bots'] or self.dataku['ajs']:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if self.type == 100:
                                        return
                                    zzz = self.famz.findChatByTicket(ticket_id)
                                    self.famz.acceptChatInvitationByTicket(zzz.chat.chatMid, ticket_id)
#===================================================================================================
            if op.type in [11, 122]:
                if op.param1 in self.protectqr:
                    if self.cek(op.param2):
                        if self.type == 1:
                            if self.famz.getChats([op.param1]).chats[0].extra.groupExtra.preventedJoinByTicket == True:
                                try:
                                    self.black(op.param2)
                                    self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                    chat = self.famz.getChats([op.param1])
                                    if chat.chats[0].extra.groupExtra.preventedJoinByTicket == True:
                                        self.famz.updateChat(chat.chats[0],4)
                                    else:
                                        pass
                                except:
                                    pass
                if op.param1 in self.protectname:
                    if self.cek(op.param2):
                        if self.type == 2:
                            try:
                                self.black(op.param2)
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                zzz = self.famz.getChats([op.param1])
                                if zzz.chats[0].chatName not in self.dataku['Proname'][op.param1]:
                                    try:
                                        zzz.chats[0].chatName = self.dataku['Proname'][op.param1]
                                        self.famz.updateChat(zzz.chats[0],1)
                                    except:
                                        pass
                            except:
                                pass
            if op.type in [15, 128]:
                if op.param2 in self.dataku["ajs"]:
                    if self.type == 0:
                        try:
                            self.famz.findAndAddContactsByMid(op.param2)
                            self.famz.inviteIntoChat(op.param1, self.antijs)
                        except:
                            pass
            if op.type in [17, 130]:
                if op.param1 in self.protectjoin:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                            except:
                                pass
                if op.param2 in self.dataku["blacklist"]:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                            except:
                                pass
            if op.type in [13, 124]:
                if self.mid in op.param3:
                    if self.type == 100:
                        if op.param2 in self.creator:
                            if op.param1 in self.dataku["gid"]:
                                self.famz.acceptChatInvitation(op.param1)
                        else:
                            pass
                    if self.wait["autoJoin"] == True:
                        if op.param2 not in self.creator and op.param2 not in self.dataku["owner"] and op.param2 not in self.dataku["bots"]:
                            pass
                        else:
                            self.famz.acceptChatInvitation(op.param1)
                            x = self.famz.getChats([op.param1]).chats[0].extra.groupExtra.memberMids
                            for y in self.dataku["blacklist"]:
                                if y in x:
                                    try:
                                        self.famz.deleteOtherFromChat(op.param1, [y])
                                    except:
                                        pass

                if op.param1 in self.protectinvite:
                    if self.cek(op.param2):
                        for invite in op.param3.split('\x1e'):
                            if self.cek(invite):
                                if self.type == self.type:
                                    try:
                                        self.black(invite)
                                        self.black(op.param2)
                                        self.famz.cancelChatInvitation(op.param1, [invite])
                                        self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                    except:
                                        pass
                if op.param3 in self.dataku["blacklist"]:
                    if self.cek(op.param2):
                        for invite in op.param3.split('\x1e'):
                            if self.cek(invite):
                                if self.type == self.type:
                                    try:
                                        self.black(invite)
                                        self.black(op.param2)
                                        self.famz.cancelChatInvitation(op.param1, [invite])
                                        self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                    except:
                                        pass
                                    pass
                if op.param2 in self.dataku["blacklist"]:
                    if self.cek(op.param2):
                        for invite in op.param3.split('\x1e'):
                            if self.cek(invite):
                                if self.type == self.type:
                                    try:
                                        self.black(invite)
                                        self.black(op.param2)
                                        self.famz.cancelChatInvitation(op.param1, [invite])
                                        self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                    except:
                                        pass

            if op.type in [19, 133]:
                if op.param1 in self.protectkick:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                self.famz.findAndAddContactsByMid(op.param3)
                                self.famz.inviteIntoChat(op.param1, [op.param3])
                            except:
                                pass
            if op.type in [32, 126]:
                if op.param1 in self.protectcancel:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                            except:
                                pass
            if op.type in [19, 133, 32, 126]:
                if op.param3 in self.owner:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                self.famz.findAndAddContactsByMid(op.param3)
                                self.famz.inviteIntoChat(op.param1, [op.param3])
                            except:
                                pass
                        if self.type == 100:
                            self.black(op.param2)
                            grup = self.famz.getChats([op.param1]).chats[0].extra.groupExtra.memberMids
                            for i in self.dataku['bots']:
                                if i in grup:
                                    pass
                                else:
                                    try:
                                        self.famz.acceptChatInvitation(op.param1)
                                        self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                        self.famz.findAndAddContactsByMid(op.param3)
                                        self.famz.inviteIntoChat(op.param1, [op.param3])
                                        self.famz.deleteSelfFromChat(op.param1)
                                    except:
                                        pass
                if op.param3 in self.admin:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                self.famz.findAndAddContactsByMid(op.param3)
                                self.famz.inviteIntoChat(op.param1, [op.param3])
                            except:
                                pass
                        if self.type == 100:
                            self.black(op.param2)
                            grup = self.famz.getChats([op.param1]).chats[0].extra.groupExtra.memberMids
                            for i in self.dataku['bots']:
                                if i in grup:
                                    pass
                                else:
                                    try:
                                        self.famz.acceptChatInvitation(op.param1)
                                        self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                        self.famz.findAndAddContactsByMid(op.param3)
                                        self.famz.inviteIntoChat(op.param1, [op.param3])
                                        self.famz.deleteSelfFromChat(op.param1)
                                    except:
                                        pass
                if op.param3 in self.staff:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                self.famz.findAndAddContactsByMid(op.param3)
                                self.famz.inviteIntoChat(op.param1, [op.param3])
                            except:
                                pass
                if op.param3 in self.bots:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                self.famz.inviteIntoChat(op.param1, self.kick)
                            except:
                                pass
                        if self.type == 100:
                            self.black(op.param2)
                            grup = self.famz.getChats([op.param1]).chats[0].extra.groupExtra.memberMids
                            for i in self.dataku['bots']:
                                if i in grup:
                                    pass
                                else:
                                    try:
                                        self.famz.acceptChatInvitation(op.param1)
                                        self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                        self.famz.inviteIntoChat(op.param1, self.kick)
                                        self.famz.deleteSelfFromChat(op.param1)
                                    except:
                                        pass
                if op.param3 in self.antijs:
                    if self.cek(op.param2):
                        if self.type == self.type:
                            self.black(op.param2)
                            try:
                                self.famz.deleteOtherFromChat(op.param1, [op.param2])
                                self.famz.findAndAddContactsByMid(op.param3)
                                self.famz.inviteIntoChat(op.param1, [op.param3])
                            except:
                                pass
        except Exception as catch:
            trace = catch.__traceback__
            print("Error Name: "+str(trace.tb_frame.f_code.co_name)+"\nError Filename: "+str(trace.tb_frame.f_code.co_filename)+"\nError Line: "+str(trace.tb_lineno)+"\nError: "+str(catch))
    def run(self):
        while True:
            try:
                ops = self.famz.fetchOps()
                for op in ops:
                    if op.revision == -1 and op.param2 != None:
                        self.famz.globalRev = int(op.param2.split("\x1e")[0])
                    if op.revision == -1 and op.param1 != None:
                        self.famz.individualRev = int(op.param1.split("\x1e")[0])
                    self.famz.localRev = max(op.revision, self.famz.localRev)
                    self.receive_message(op)
            except:
                pass
            
