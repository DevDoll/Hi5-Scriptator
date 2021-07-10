import requests
import json
import random
import time
import string
from collections import Counter
import re
from random import randrange

# extracting account id

def getacc():
    try:
        alphanumiric = string.ascii_lowercase + string.digits
        did = ''.join(random.choice(alphanumiric) for i in range(16))
        aid = "".join([random.choice(alphanumiric) for i in range(8)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(4)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(4)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(4)]) + "-" + "".join(
            [random.choice(alphanumiric) for i in range(12)])


        url = 'https://secure.hi5.com/api/?method=tagged.login.login&application_id=user'
        headers = {
            'User-Agent': 'hi5/9.30.1 (SPA Condor Electronics TFX-708G; Android 4.4.2; Android/TFX-708G/TFX-708G:4.4.2/KOT49H/1445414608:user/release-keys)'}
        obj = {'email': '%s@gmail.com' % email, 'password': 'NewPassword456', 'deviceId': '%s' % did,
               'aaid': '%s' % aid}
        try:
            r = requests.post(url, data=obj, headers=headers, proxies=proxy, timeout=30)
            response = json.loads(r.text)
            #print('Retrieving Account Info for %s' % email)
            #print(response)
            stats = response['stat']
            if stats == 'fail':
                print('-----------------------------------------------------------------> Previous Account Is Gone')
                return False
            else:
                print('%s is active'%email)
                results = response['result']
                accid = results['user_id']
                autotoken = results['auto_token']
                session = results['session']
                mid = str(accid)
                return mid, autotoken, session
        except requests.exceptions.ConnectionError:
            print("Connection refused")
            getacc()
    except:
        print('\nCant Login to the account, moving on\n')
        return False

def msgext(mn):
    mlist = list()
    with open('messages/cashapp-%s-reply.txt'%mn) as dfile:
        for mline in dfile:
            uline = mline.replace('you', 'u')
            udoline = uline.rstrip() + "".join('.')
            nline = mline.replace('and', 'n')
            ndoline = nline.rstrip() + "".join('.')
            moline = mline.replace('money', 'funds')
            mdoline = moline.rstrip() + "".join('.')
            daline = mline.replace('that', 'dat')
            ddoline = daline.rstrip() + "".join('.')
            thline = mline.replace('the', 'thé')
            tdoline = thline.rstrip() + "".join('.')
            urline = mline.replace('your', 'ur')
            urdoline = urline.rstrip() + "".join('.')
            rline = mline.replace('are', 'r')
            waline = mline.replace('wanna', 'wnna')#
            knline = mline.replace('know', 'knw')
            kndline = knline.rstrip() + "".join('.')
            jsline = mline.replace('just', 'jst')
            jsdline = jsline.rstrip() + "".join('.')
            vrline = mline.replace('verify', 'verfy')
            vrdline = vrline.rstrip() + "".join('.')
            bfline = mline.replace('before', 'b4')
            bfdline = bfline.rstrip() + "".join('.')
            snline = mline.replace('send', 'snd')
            wadoline = waline.rstrip() + "".join('.')#
            rdoline = rline.rstrip() + "".join('.')
            doline = mline.rstrip() + "".join('.')

            grfline = mline.replace('hey', 'ey')
            ugrfline = grfline.rstrip() + "".join('.')

            grfline2 = mline.replace('hello', 'hllo')
            ugrfline2 = grfline2.rstrip() + "".join('.')

            grfline3 = mline.replace('hi', 'yo')
            ugrfline3 = grfline3.rstrip() + "".join('.')

            grfline4 = mline.replace('plese', 'pls')
            ugrfline4 = grfline4.rstrip() + "".join('.')

            grfline5 = mline.replace('user', 'person')
            ugrfline5 = grfline5.rstrip() + "".join('.')

            grfline6 = mline.replace('website', 'link')
            ugrfline6 = grfline6.rstrip() + "".join('.')

            grfline7 = mline.replace('link', 'website')
            ugrfline7 = grfline7.rstrip() + "".join('.')

            grfline8 = mline.replace('$100', '100 Bucks')
            ugrfline8 = grfline8.rstrip() + "".join('.')

            grfline9 = mline.replace('$100', '100 Dollars')
            ugrfline9 = grfline9.rstrip() + "".join('.')

            mlist.append(grfline)
            mlist.append(ugrfline)
            mlist.append(grfline2)
            mlist.append(ugrfline2)
            mlist.append(grfline3)
            mlist.append(ugrfline3)
            mlist.append(grfline4)
            mlist.append(ugrfline4)
            mlist.append(grfline5)
            mlist.append(ugrfline5)
            mlist.append(grfline6)
            mlist.append(ugrfline6)
            mlist.append(grfline7)
            mlist.append(ugrfline7)
            mlist.append(grfline8)
            mlist.append(ugrfline8)
            mlist.append(grfline9)
            mlist.append(ugrfline9)


            mlist.append(mline)
            mlist.append(doline)
            mlist.append(uline)
            mlist.append(udoline)
            mlist.append(nline)
            mlist.append(ndoline)
            mlist.append(moline)
            mlist.append(mdoline)
            mlist.append(daline)
            mlist.append(ddoline)
            mlist.append(thline)
            mlist.append(tdoline)
            mlist.append(urline)
            mlist.append(urdoline)
            mlist.append(rline)
            mlist.append(rdoline)
            mlist.append(wadoline)
            mlist.append(waline)
            mlist.append(knline)
            mlist.append(kndline)
            mlist.append(jsline)
            mlist.append(jsdline)
            mlist.append(vrline)
            mlist.append(vrdline)
            mlist.append(bfline)
            mlist.append(bfdline)
            mlist.append(snline)
            mlist.append(wadoline)

        mlist = list(dict.fromkeys(mlist))
    return mlist

def dmngen():
    dmnlist = list()
    chars = ['$$', '@@', '!!', '??', '##', '==', '--', '++', '**', '%%', '**', '^^', '(', ')']
    ranchar = random.choice(chars)
    with open('messages/cashappdomains.txt') as domfile:
        for dmn in domfile:
            charddmn = dmn.replace('.', '%s'%ranchar)
            dmnlist.append(charddmn)

        return dmnlist, ranchar

def nrmldomn():
    domlist = list()
    with open('messages/cashappdomains.txt') as domfile:
        for dmn in domfile:
            domlist.append(dmn)

        return domlist

def repl(m, c):
    str = m
    return str.replace("+-+", "%s"%c)


# Replying to users function
def replier():
    cookies = {'S': '%s' % session}
    headers = {'User-Agent': '%s' % useragent}
    inburl = 'https://secure.hi5.com/api/?method=tagged.im.getInbox&size=s&size2=m&count=20&filter=new&isPhotoCommentSupported=true&application_id=user'
    inb = requests.get(inburl, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
    inbox = json.loads(inb.text)
    print(inbox)
    results = inbox['result']
    usrs = results['items']
    linklimit = 0
    newp = 0
    oldp = 0
    notin = 0
    rejec = 0
    conv = 0

    for item in usrs:
        uid = item['uid']
        lastsender = item['lastUidInConv']
        #domainnames = open('messages/%sdomains.txt' % niche).read().splitlines()
        #domainslist = list()
        # Maintenence
        # with open('messages/%sdomains.txt'%niche) as dfile:
        #     for dn in dfile:
        #         ndomain = dn.replace('.', '$')
        #         domainslist.append(ndomain)


        if lastsender == uid:
            print('user has sent a message, checking the conversation...\n')
            convurl = 'https://secure.hi5.com/api/?method=tagged.im.getConversation&size=s&size2=m&uid=%s&count=25&isPhotoCommentSupported=true&application_id=user' % uid
            rq = requests.get(convurl, cookies=cookies, headers=headers, proxies=proxy, timeout=30)
            rep = json.loads(rq.text)
            #print(rep)
            res = rep['result']
            it = res['items']

            count = 0
            counth = 0
            for resu in reversed(it):
                uuid = str(resu['uid'])
                global umsg
                umsg = resu['html']
                if uuid == myid:
                    count += 1
                    print('-Script: %s'%umsg)

                else:
                    counth += 1
                    print('-Prospect: %s'%umsg)
                    if counth >= 1:
                        if re.compile('|'.join(intrested), re.IGNORECASE).search(umsg):
                            print('\nuser %s Accepted'%uuid)
                            intrusr.append(uuid)
                            print('User %s has been added to the list'% uuid)
                        elif re.compile('|'.join(notintrested), re.IGNORECASE).search(umsg):
                            print('user rejected')
                            notintrusr.append(uuid)
                    if count == 3:
                        print('User said after Seeing the link: %s'%umsg)
                        outm = open('messages/responses/after-link-response.txt', 'a')
                        outm.write('%s\n'%umsg)
                        outm.close()
                    if count == 4:
                        print('User said after Seeing the link: %s'%umsg)
                        outh = open('messages/responses/after-hesitation-response.txt', 'a')
                        outh.write('%s\n'%umsg)
                        outh.close()




            print('\nuser %s have RECEIVED: %s messages & SENT: %s messages' % (uid, count, counth))
            surl = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'

            if dmngener == 'yes':
                print('generating domains as texts...')
                domainnames, usdchar = dmngen()
                domn = msgext('dmn')
                randomn = random.choice(domn)
                domainunlck = repl(randomn, usdchar)

            else:
                #print('Taking domains as they are from the text file...')
                domainnames = nrmldomn()
                domainunlck = ''
            print('treating user %s'%uid)
            intrusrpu = set(list(intrusr))
            notinpu = set(list(notintrusr))
            rejectusrs = str(notinpu)
            inusers = str(intrusrpu)
            suid = str(uid)
            try:

                if inusers.count(suid) > 0:
                    print('yes its in')
                    isin = inusers.count(suid)
                    print('UID %s is in %s time'%(uid, isin))
                else:
                    isin = inusers.count(suid)
                    print('UID %s is in %s time'%(uid, isin))

            except Exception as e: print(e)

            if count == 1 and counth >= 1 and inusers.count(suid) > 0:
                print('user is intrested')
                # Chossing messages
                newp +=1
                randdomain = random.choice(domainnames)
                randext = random.choice(ext)
                blk = '%s' % randdomain
                second = random.choice(secondreply)
                print('picked a random domainname')


                if linklimit < linkperround:
                    # marking the message as read
                    rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                    rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                    markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                    unreadreq = json.loads(markread.text)

                    # Sending the first reponse
                    print('\nnew user replied, Sending the Landing Page...\n')

                    one = {'uid': '%s' % uid, 'message': '%s' % second, 'type': '1'}
                    send1 = requests.post(surl, data=one, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                    se1 = json.loads(send1.text)
                    #print(se1)
                    firstrep.append(second)
                    linklimit = + 1

                    # Sending the landing page
                    print('Using as landing page: %s'%blk)
                    blcav = {'uid': '%s' % uid, 'message': '%s' % blk, 'type': '1'}
                    send11 = requests.post(surl, data=blcav, headers=headers, cookies=cookies, proxies=proxy)
                    se11 = json.loads(send11.text)
                    domainsent.append(blk)
                    #print(se11)

                    # Modification of domain
                    if dmngener == 'yes':
                        dmnulck = domainunlck
                        three = {'uid': '%s' % uid, 'message': '%s'%dmnulck, 'type': '1'}
                        send3 = requests.post(surl, data=three, headers=headers, cookies=cookies)
                        se3 = json.loads(send3.text)
                        dmnunlkrep.append(dmnulck)
                    else:
                        print('Script is using normal domains strategy')
                    #print(se3)

                    #
                    # time.sleep(random.uniform(1, 3))
                    # lppb = {'uid': '%s' % uid, 'message': '%s' % gif, 'type': '9'}
                    # sendlp = requests.post(surl, data=lppb, headers=headers, cookies=cookies)
                    # selp = json.loads(sendlp.text)
                    # print(selp)
                    # print('Gif has been sent')

                    # imgurl = 'https://secure.hi5.com/api/?method=tagged.im.sendPhotoFromUpload&uid=%s&application_id=user' % uid
                    # sendimg = requests.post(imgurl, files=files, headers=headers, cookies=cookies)
                    # print(sendimg)
                    # seni = json.loads(sendimg.text)
                    # print(seni)
                    # time.sleep(random.uniform(2, 2))

                    print('USER %s Have Been Coocked =D' % uid)

                    outF = open("users/engaged-users.txt", "a")
                    usid = str('\n%s' % uid)
                    outF.write(usid)
                    outF.close()

                else:
                    print('Skiping User in order to keep it %s link per hour'%linkcount)

            elif count == 1 and counth >= 1 and rejectusrs.count(suid) > 0:
                print('\nuser %s rejected'% uid)
                rejec += 1
                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                unreadreq = json.loads(markread.text)

                # Sending the first reponse
                one = {'uid': '%s' % uid, 'message': 'look, i know a lot of people are promoting this but i have a real one, i can send you a proof if you want? here', 'type': '1'}
                send1 = requests.post(surl, data=one, headers=headers, cookies=cookies, proxies=proxy)
                se1 = json.loads(send1.text)
                # Sendning the Proof:

                tow = {'uid': '%s' % uid, 'message': 'https://i.postimg.cc/dQbn2tq0/89263415-517104595887072-6767159070102126592-n.jpg', 'type': '9'}
                send2 = requests.post(surl, data=tow, headers=headers, cookies=cookies, proxies=proxy)
                se2 = json.loads(send2.text)

                three = {'uid': '%s' % uid, 'message': 'thats my cut from users who got it, i promise u its legit, if u didnt get it ill cashapp u my self', 'type': '1'}
                send3 = requests.post(surl, data=three, headers=headers, cookies=cookies, proxies=proxy)
                se3 = json.loads(send3.text)


            elif count == 1 and counth >= 1 and inusers.count(suid) == 0 and rejectusrs.count(suid) == 0:
                print('\nuser %s is not intrested'% uid)
                notin += 1
                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                unreadreq = json.loads(markread.text)

                # Sending the first reponse
                print('\nUser did not accept, apologising...\n')

                one = {'uid': '%s' % uid, 'message': 'Okey sorry for disturbing you', 'type': '1'}
                send1 = requests.post(surl, data=one, headers=headers, cookies=cookies, proxies=proxy)
                se1 = json.loads(send1.text)
                # print(se1)

            elif count == 2 and counth >= 2 and inusers.count(suid) > 0:
                # getting response
                oldp += 1
                third = random.choice(thirdreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                json.loads(markread.text)

                # Flirting with user...
                tow = {'uid': '%s' % uid, 'message': '%s' % third, 'type': '1'}
                send2 = requests.post(surl, data=tow, headers=headers, cookies=cookies, proxies=proxy)
                se2 = json.loads(send2.text)
                secondrep.append(third)
            elif count == 2 and counth >= 2 and inusers.count(suid) == 0:
                print('user is not intrested')
                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                unreadreq = json.loads(markread.text)


            elif count == 3 and counth >= 2 and inusers.count(suid) > 0:
                # getting response
                oldp += 1
                forth = random.choice(forthreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                json.loads(markread.text)

                # Asking the user again to confirm Higher the impressions...
                url = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'
                one = {'uid': '%s' % uid, 'message': '%s' % forth, 'type': '1'}
                send1 = requests.post(url, data=one, headers=headers, cookies=cookies, timeout=30)
                json.loads(send1.text)
                thirdrep.append(forth)
            elif count == 3 and counth >= 2 and inusers.count(suid) == 0:
                print('user is not intrested')
                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                unreadreq = json.loads(markread.text)


            elif count == 4 and counth >= 2 and inusers.count(suid) > 0:
                # getting response
                oldp += 1
                fifth = random.choice(fifthreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                json.loads(markread.text)

                print('Asking the user to follow the instructions...')
                url = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'
                one = {'uid': '%s' % uid, 'message': '%s' % fifth, 'type': '1'}
                send1 = requests.post(url, data=one, headers=headers, cookies=cookies, timeout=30)
                json.loads(send1.text)
                forthrep.append(fifth)

            elif count == 4 and counth >=2 and rejectusrs.count(suid) > 0:
                conv +=1
                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                json.loads(markread.text)

                # the bs sending
                randdomain = random.choice(domainnames)
                blk = '%s' % randdomain

                # Sending a reponse
                print('\nnew user replied, Sending the Landing Page...\n')

                one = {'uid': '%s' % uid, 'message': 'you will be asked to download their money transfer app & than add your cashapp inside', 'type': '1'}
                send1 = requests.post(surl, data=one, headers=headers, cookies=cookies, proxies=proxy)
                se1 = json.loads(send1.text)

                # Sending the landing page
                print('Using as landing page: %s' % blk)
                blcav = {'uid': '%s' % uid, 'message': '%s' % blk, 'type': '1'}
                send11 = requests.post(surl, data=blcav, headers=headers, cookies=cookies, proxies=proxy)
                se11 = json.loads(send11.text)
                domainsent.append(blk)

            elif count == 4 and counth >= 2 and inusers.count(suid) == 0:
                print('user is not intrested')
                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                unreadreq = json.loads(markread.text)


            elif count == 5 and counth >=2 and inusers.count(suid) > 0:
                # getting response
                oldp += 1
                sisxth = random.choice(sixthreplys)

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                json.loads(markread.text)

                print('Retreating from the user...')
                url = 'https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user'
                one = {'uid': '%s' % uid, 'message': '%s'%sisxth, 'type': '1'}
                send1 = requests.post(url, data=one, headers=headers, cookies=cookies)
                json.loads(send1.text)
                fifthrep.append(sisxth)
            elif count == 5 and counth >= 2 and inusers.count(suid) == 0:
                print('user is not intrested')
                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                unreadreq = json.loads(markread.text)


            elif count == 6 and counth >=4 and inusers.count(suid) > 0:
                # getting response

                # marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                json.loads(markread.text)

            elif count == 1 and counth == 0:
                # #marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy, timeout=30)
                json.loads(markread.text)
                print('user received the first message but he didnt reply')


            elif count == 0 and counth >= 1:
                print('a user sent the first message, unreading him...')
                # #marking the message as read
                rurl = 'https://secure.hi5.com/api/?method=tagged.im.markRead&application_id=user'
                rcontent = {'uid': '%s' % uid, 'unread_count': '1'}
                markread = requests.post(rurl, data=rcontent, headers=headers, cookies=cookies, proxies=proxy)
                json.loads(markread.text)


        elif lastsender == myid:
            print('user didnt reply yet')

        print('\n%s New Person Accepeted & has been messaged' % newp)
        print('%s Old Person has been messaged' % oldp)
        print('%s New Person Rejected & has been messeged'% rejec)
        print('%s New Person is not intrested'% notin)
        print('%s Person has accepted after rejecting'% conv)


# collecting inputs:
uaf = open('config/user-agents.txt', 'r').read().splitlines()
# period = int(input('For how many minutes do you want to the Bot to run:  '))
accr = int(input('How Many Times Reeat the account:  '))
dmngener = input('Activate Domain Bypass: ')
cool = int(input('How many minutes between each Inbox Check for each account: ')) * 60
times = int(input('how many times do you wanna repeat: '))
wrkngtime = cool * times
#linkcount = int(input('how many links do you wanna send in each %s hours: '%wrkngtime))
linkcount = int(50)
cooldwn = int(input('How many minutes between every account:  ')) * 60
niche = 'cashapp'

intrested = ['sure', 'yes', 'yeah', 'ok', 'yea', 'ofcourse', 'for sure', 'Ok', 'Yes', 'Sure', 'Yeah'
            , 'Yea', 'Ofcourse', 'okey', 'website', 'link', 'why not', 'cashapp', 'yup', 'yhup', 'k'
            , 'yea', 'paypal', 'what', 'how', 'tell', 'what', 'legit', 'really', 'send', 'why']

notintrested = ['no', 'nah', "i'm good", 'not intrested', 'naw', 'scam', 'shit', 'bye', 'not intrested', 'bs', "it doesn't work"]

angry = []

linkperround = linkcount / times




#domainunlck = open('messages/domainunlock.txt').read().splitlines()
ext = open('messages/%s-domain-extention.txt'%niche, 'r').read().splitlines()
secondreply = msgext(2)
thirdreplys = msgext(3)
forthreplys = msgext(4)
fifthreplys = msgext(5)
sixthreplys = msgext(6)

# t_end = time.time() + 60 * period
s_time = time.time()

# while time.time() < t_end:


# Working to get the email:
emaillist = list()
intrusr = list()
notintrusr = list()
with open('accounts/hi5acc.txt', 'r') as efile:
    for emailuser in efile:
        email = emailuser.rstrip()
        emaillist.append(email)

start_time = time.time()

domainsent = list()

for email in emaillist:

    coolp = cool + 120
    coolm = cool - 120
    randf = cooldwn - 120
    randl = cooldwn + 120

    reacc = 0
    while reacc <= accr:

        Repeat = 0
        proxy = []
        firstrep = list()
        dmnunlkrep = list()
        secondrep = list()
        thirdrep = list()
        forthrep = list()
        fifthrep = list()


        while Repeat < times:

            acctchk = getacc()
            if acctchk is not False:

                coolr = randrange(coolm, coolp)
                sleeping = coolr / 60
                print('Sleeping for %s Minutes' % sleeping)
                time.sleep(coolr)
            else:

                onedict = Counter(firstrep)
                towdict = Counter(secondrep)
                threedict = Counter(thirdrep)
                fordict = Counter(forthrep)
                fivedict = Counter(fifthrep)
                sixdict = Counter(domainsent)
                sevendict = Counter(dmnunlkrep)
                totalintr = len(intrusr)
                print('\n# Results:\n')
                print('###############################################################################')
                print('# %s  #' % sixdict)
                print('# %s  #' % sevendict)
                print('# %s  #' % onedict)
                print('# %s Users accepted in total #' % totalintr)
                print('###############################################################################')
                break

            print('\nTrying To Login as: %s@gmail.com\n' % email)
            # Declaring Variables
            # proxy = {
            #           http_proxy = "http://devdoll:T10k5q6v3gCh6jZe@proxy.packetstream.io:31112"
            #           https_proxy = "http://devdoll:T10k5q6v3gCh6jZe@proxy.packetstream.io:31112"
            #           url = "https://ipv4.icanhazip.com"
            # }

            useragent = random.choice(uaf)
            stats = getacc()
            if stats is not False:
                try:
                    myid, token, session = getacc()

                    print('Replying to all users...')
                    rwave = time.time()
                    try:
                        try:
                            # if dmngener == 'yes':
                            #     print('generating domains as texts...')
                            #     domainnames, usdchar = dmngen()
                            #     domn = msgext('dmn')
                            #     randomn = random.choice(domn)
                            #     domainunlck = repl(randomn)
                            #
                            # else:
                            #     print('Taking domains as they are from the text file...')
                            #     domainnames = nrmldomn()

                            time.sleep(2)
                            replier()
                        except Exception as e: print(e)
                    except:
                        replier()
                    rdone = time.time() - rwave
                    rtime = rdone / 60

                    onedict = Counter(firstrep)
                    sixdict = Counter(domainsent)
                    sevendict = Counter(dmnunlkrep)
                    totalintr = len(intrusr)
                    print('\n# Results:\n')
                    print('###############################################################################')
                    print('# %s  #' % sixdict)
                    print('# %s  #' % sevendict)
                    print('# %s  #' % onedict)
                    print('# %s Users accepted in total #'% totalintr)
                    print('###############################################################################')
                    print("\nOne reply wave took %s minutes\n" % rtime)
                    Repeat += 1
                    print('repeating for the %s time...' % Repeat)

                except:
                    print('\naccount Blocked Moving on...\n')
                    onedict = Counter(firstrep)
                    towdict = Counter(secondrep)
                    threedict = Counter(thirdrep)
                    fordict = Counter(forthrep)
                    fivedict = Counter(fifthrep)
                    sixdict = Counter(domainsent)
                    sevendict = Counter(dmnunlkrep)
                    totalintr = len(intrusr)
                    print('\n# Results:\n')
                    print('###############################################################################')
                    print('# %s  #' % sixdict)
                    print('# %s  #' % sevendict)
                    print('# %s  #' % onedict)
                    print('# %s Users accepted in total #'% totalintr)
                    print('###############################################################################')

                    break

            else:
                blcktime = time.time() - s_time
                btime = blcktime / 60
                print('Account has been blocked after %s Minutes from Launch' % btime)
                onedict = Counter(firstrep)
                sixdict = Counter(domainsent)
                sevendict = Counter(dmnunlkrep)
                totalintr = len(intrusr)
                print('\n# Results:\n')
                print('###############################################################################')
                print('# %s  #' % sixdict)
                print('# %s  #' % sevendict)
                print('# %s  #' % onedict)
                print('# %s Users accepted in total #' % totalintr)
                print('###############################################################################')

                break

        accchk = getacc()
        if accchk is not False:

            cooldownran = randrange(randf, randl)

            cooldwnm = cooldownran / 60
            timeused = cooldownran / 8
            timeusedm = timeused / 60
            print('account done, sleeping for %s minutes' % timeusedm)
            sstart = time.time()
            time.sleep(timeused)
            # Account Cancelation Checking Started
            accchk1 = getacc()
            if accchk1 is not False:
                remt = time.time() - sstart
                frt = cooldwn - remt
                remtime = frt / 60
                print('\nstill active while in %s minutes sleep [%s Minutes Remaining] \n' % (cooldwnm, remtime))
                time.sleep(timeused)
            else:
                print('account removed, moving on /././.')
                Repeat += 100

            accchk2 = getacc()
            if accchk2 is not False:
                remt = time.time() - sstart
                frt = cooldwn - remt
                remtime = frt / 60
                print('\nstill active while in %s minutes sleep [%s Minutes Remaining] \n' % (cooldwnm, remtime))
                time.sleep(timeused)
            else:
                print('account removed, moving on /././.')
                Repeat += 100

            accchk3 = getacc()
            if accchk3 is not False:
                remt = time.time() - sstart
                frt = cooldwn - remt
                remtime = frt / 60
                print('\nstill active while in %s minutes sleep [%s Minutes Remaining] \n' % (cooldwnm, remtime))
                time.sleep(timeused)
            else:
                print('account removed, moving on /././.')
                Repeat += 100

            accchk4 = getacc()
            if accchk4 is not False:
                remt = time.time() - sstart
                frt = cooldwn - remt
                remtime = frt / 60
                print('\nstill active while in %s minutes sleep [%s Minutes Remaining] \n' % (cooldwnm, remtime))
                time.sleep(timeused)
            else:
                print('account removed, moving on /././.')
                Repeat += 100

            accchk5 = getacc()
            if accchk5 is not False:
                remt = time.time() - sstart
                frt = cooldwn - remt
                remtime = frt / 60
                print('\nstill active while in %s minutes sleep [%s Minutes Remaining] \n' % (cooldwnm, remtime))
                time.sleep(timeused)
            else:
                print('account removed, moving on /././.')
                Repeat += 100

            accchk6 = getacc()
            if accchk6 is not False:
                remt = time.time() - sstart
                frt = cooldwn - remt
                remtime = frt / 60
                print('\nstill active while in %s minutes sleep [%s Minutes Remaining] \n' % (cooldwnm, remtime))
                time.sleep(timeused)
            else:
                print('account removed, moving on /././.')
                Repeat += 100

            accchk7 = getacc()
            if accchk7 is not False:
                remt = time.time() - sstart
                frt = cooldwn - remt
                remtime = frt / 60
                print('\nstill active while in %s minutes sleep [%s Minutes Remaining] \n' % (cooldwnm, remtime))
                time.sleep(timeused)
            else:
                print('account removed, moving on /././.')
                Repeat += 100

            onedict = Counter(firstrep)
            sixdict = Counter(domainsent)
            sevendict = Counter(dmnunlkrep)
            totalintr = len(intrusr)
            print('\n# Results:\n')
            print('###############################################################################')
            print('# %s  #' % sixdict)
            print('# %s  #' % sevendict)
            print('# %s  #' % onedict)
            print('# %s Users accepted in total #' % totalintr)
            print('###############################################################################')

            print('Account Done, Pulling up another one...')
        else:

            onedict = Counter(firstrep)
            towdict = Counter(secondrep)
            threedict = Counter(thirdrep)
            fordict = Counter(forthrep)
            fivedict = Counter(fifthrep)
            sixdict = Counter(domainsent)
            sevendict = Counter(dmnunlkrep)
            totalintr = len(intrusr)
            print('\n# Results:\n')
            print('###############################################################################')
            print('# %s  #' % sixdict)
            print('# %s  #' % sevendict)
            print('# %s  #' % onedict)
            print('# %s Users accepted in total #' % totalintr)
            print('###############################################################################')
            Repeat += 100
        reacc +=1
end_time = time.time() - s_time
minu = end_time / 60
print("The Script have finished within %s minutes" % minu)
