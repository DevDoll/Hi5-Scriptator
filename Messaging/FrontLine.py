import requests
import json
import os
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time
import random
import string
from random import randrange



 #extracting account id
def getacc():
    try:
        alphanumiric = string.ascii_lowercase + string.digits
        did = ''.join(random.choice(alphanumiric) for i in range(16))
        aid = "".join([random.choice(alphanumiric) for i in range(8)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(4)])+"-"+"".join([random.choice(alphanumiric) for i in range(12)])

        #print('Using %s as a DeviceID and as AAID: %s' % (did, aid))

        url = 'https://secure.hi5.com/api/?method=tagged.login.login&application_id=user'
        headers = {'User-Agent': '%s'%useragent}
        obj = {'email': '%s@gmail.com'%email, 'password': 'NewPassword456', 'deviceId': '%s'%did, 'aaid': '%s'%aid}
        try:
            r = requests.post(url, data=obj, headers=headers, proxies=proxy)
            response = json.loads(r.text)
            #print('Retrieving Account Info')
            #print(response)
            results = response['result']
            working = response['stat']
            if working == 'fail':
                print('-----------------------------------------------------------------> Previous Account Is Gone')
                return False
            else:
                print('%s is active'%email)
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
    with open('messages/cashapp-%s-reply.txt'% mn) as dfile:
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


def extractor(age):
    try:
        print(age)
        cookies = {'S': 'ev0fhabdvaaj8m8rrirqqlibmq'}
        headers = {'User-Agent': '%s'%useragent}
        r = requests.get('https://secure.hi5.com/api/?method=tagged.search.query&returns_users=true&show=25&language=-1&min_age=%s&max_age=%s&distance=750&location=USA&num_results=400&gender=%s&country=US&application_id=user'% (age, max, gender), cookies=cookies, headers=headers, proxies=proxy, timeout=10)
        users = json.loads(r.text)


        for result in users['results']:
            user = result['userId']
            usr = str(user)
            status = result['online']
            if status == True:
                outF = open("bot-users/%s-active-fresh-users.txt"%email, "a+")
                print('this user is online: %s'%user)
                print(user, file=outF)
                outF.close()

            elif status == False:
                a = 'user is offline'
            else:
                print('something went wrong with %s'%user)
    except:
        extractor(age)

 # Remove reached users
def rechecker():

    with open('%s/%s-reached-users.txt'%(nourfold2,niche), 'r+') as source:
        filter_lines = source.readlines()

    with open('bot-users/%s-active-fresh-users.txt'%email, 'r') as f:
        lines = f.readlines()

    with open('bot-users/%s-active-clean-users.txt'%email, 'w') as target:
        for line in lines:
            if line not in filter_lines:
                target.write(line)
    source.close()
    f.close()
    target.close()
    os.remove('bot-users/%s-active-fresh-users.txt'%email)
    actfile = open("bot-users/%s-active-clean-users.txt"%email, "r")
    line_count = 0
    for line in actfile:
        if line != "\n":
            line_count += 1
    actfile.close()
    print('%s fresh accounts was cleaned & are ready to be Cocked!' % line_count)



def sender():
    try:
        cookies = {'S': '%s'% session}
        headers = {'User-Agent': '%s'%useragent}
        r = requests.get('https://secure.hi5.com/api/?method=tagged.im.getConversation&size=s&size2=m&uid=%s&count=100&isPhotoCommentSupported=true&application_id=user'%usrid, cookies=cookies, headers=headers, proxies=proxy, timeout=30)
        reply = json.loads(r.text)
        print(reply)
        replys = reply['result']
        container = replys['items']
        count = 0
        for result in container:
            user = result['uid']
            uids = str(user)
            if uids == myid:
                count +=1

        if count == 0:
            try:
                print("trying to send the first message to: %s"%usrid)
                objec = {'uid': '%s'%usrid, 'message': '%s'% keywords, 'type': '1'}
                time.sleep(2)
                try:
                    send = requests.post('https://secure.hi5.com/api/?method=tagged.im.send&platform=android&application_id=user', data=objec, headers=headers, cookies=cookies)
                    fmsg = json.loads(send.text)
                    print(fmsg)
                    results = fmsg['result']

                    if "code" not in results:
                        print(fmsg)
                        print('Message Sent!\n')
                        outf = open("bot-users/%s-reached-users.txt"% niche, "a")
                        outf.write(usrid)
                        time.sleep(wt)
                        #outi = open('bot-users/%s-reached-users.txt' % email, 'a')
                        usrslist.append(usrid)
                        #outi.write(usrid)
                        outf.close()
                        #outi.close()
                    elif "code" in results:
                        code_num = results['code']
                        print(fmsg)
                        if code_num == 25:
                            print('\nThe account have reached the maximum messages sent... Replying to messages & Moving to the next account\n')
                            return False
                        else:
                            print('message didnt arrive, skipping to the next user...')
                except requests.exceptions.Timeout as e: print(e)

            except Exception as e: print(e)

        elif count > 0:
            print('Message has already been sent previously to %s'%usrid)
            outf = open("users/reached-users.txt", "a")
            outf.write(usrid)
            outf.close()
    except Exception as e: print(e)

# Generating a proxy
def get_proxies(ua):
    proxies = []
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

  # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
                        'ip':   row.find_all('td')[0].string,
                        'port': row.find_all('td')[1].string})
    return proxies

def random_proxy(proxies):
  return random.choice(proxies)


#Reading Config:

def parsel(line):
    delim = line.find(':')
    return line[delim+1:].strip()

def configer(config_string):
    try:
        account_loop = int(parsel(config_string[0]))
        gender = parsel(config_string[1])
        messages_waves = int(parsel(config_string[2]))
        waves_timebreak = int(parsel(config_string[3]))
        waves_count = int(parsel(config_string[4]))
        account_timebreak = int(parsel(config_string[5]))
        return account_loop, gender, messages_waves, waves_timebreak, waves_count, account_timebreak
    except Exception as e: print(e)

with open("config.txt") as config:
    config_values = config.readlines()

account_loop, tgender, messages_waves, waves_timebreak, waves_count, account_timebreak = configer(config_values)

# collecting inputs:

#type = input('(S)olo or (D)uo')    #for

osystem = "M"
devicename = 'macbook'
madir = open('config.txt', 'r').read().splitlines()
mdir = random.choice(madir)

accr = account_loop     #int(input('How Many Times Reeat the account:  '))
gender = tgender   #input('do you want them (F)emale or (M)ale:  ')
uaf = open('config/user-agents.txt', 'r').read().splitlines()
messn = messages_waves    #int(input('how many messages do you wanna send with each account:  '))
col = waves_timebreak * 60  #int(input('how many minutes between every %s messages:  '%messn)) * 60
niche = 'cashapp'
times = waves_count     #int(input('how many times do you wanna repeat the messages:  '))
entimes = times - 1
cooldwn = account_timebreak * 60      #int(input('How many minutes between each account:  ')) * 60

# adding backround touches
speeddeter = 'L'
DropboxFolder = '/Users/%s/Dropbox' % devicename
nourfold = '%s/Messaging/users'%mdir
nourfold2 = 'users'
wt = 0




#t_end = time.time() + 60 * period
s_time = time.time()





# Working to get the email:
emaillist = list()

with open('accounts/hi5acc.txt', 'r') as efile:
    for emailuser in efile:
        email = emailuser.rstrip()
        emaillist.append(email)

start_time = time.time() / 60

for email in emaillist:

    randf = cooldwn - 200
    randl = cooldwn + 200
    colf = col - 60
    coll = col + 60

    Repeat = 0
    reacc = 0
    while reacc <= accr:
        Repeat = 0

        while Repeat < times:
            print('Repeating %s for the %s time'%(email, Repeat))
            #Getting Proxy
            # ua = UserAgent()
            # proxies = get_proxies(ua)
            proxy = []

            # prostr = str(nproxy)
            # ip = prostr.split(',')[0]
            # port = prostr.split(',')[1]
            # ipa = ip.split(':')[1]
            # porta = port.split(':')[1]
            # fport = porta.replace('}', '')
            #
            # ips = ipa.replace("'", "")
            # ports = fport.replace("'", "")
            # pip = ips.replace(" ", "")
            # pport = ports.replace(" ", "")

            # proxy = {
            #     "http": "http://%s:%s" % (pip, pport),
            #     "https": "http://%s:%s" % (pip, pport),
            # }

            # proxy = {
            #     "http": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
            #     "https": "http://vnpfwklm-rotate:kz65gib69zcm@45.9.123.41:80",
            # }


            print('\nLogged in as: %s@gmail.com'%email)
            # Declaring Variables
            useragent = random.choice(uaf)
            stats = getacc()
            if stats is not False:
                try:
                    myid, token, session = getacc()

                    #scrapper
                    print('Scrapping Active Users...\n')
                    agelist = list()
                    with open("config/age.txt", "r") as file:
                        for line in file:
                            age = line
                            agelist.append((age))

                    for age in agelist:
                        max = age
                        extractor(age)

                    #Plugin for Keep on tracking niche reach & to keep on growing it:
                    time.sleep(5)
                    rechecker()

                    #sending the first messages:
                    print('\nThrowing Clean accounts to the grill...\n')
                    usrlist = list()
                    with open("bot-users/%s-active-clean-users.txt"%email, "r") as usrfile:
                        for line in usrfile:
                            usrid = line
                            usrlist.append((usrid))

                        st = 0
                        usrslist = list()
                        for usrid in usrlist:

                            msglines = msgext(1)
                            keywords = random.choice(msglines)

                            if st < messn:
                                limit = sender()
                                if limit is not False:
                                    print('message %s has been sent' % st)
                                    st +=1
                                else:
                                    break

                            else:
                                break
                    Repeat += 1
                    # add the content of the list to a file here
                    if speeddeter == 'D':
                        notifyu = open("%s/%s-reached-users.txt" % (DropboxFolder, niche), "a")
                        for usid in usrslist:
                            notifyu.write(usid)
                        notifyu.close()
                        usrslist.clear()

                    print('Reapeating for the %s time'%Repeat)
                    entime = time.time() - start_time * 60
                    frontlinedone = entime / 60
                    print('an account completed in %s Minutes' % frontlinedone)
                    ncol = randrange(colf, coll)
                    sleeping = ncol / 60
                    print('Sleeping for %s Minutes' % sleeping)
                    if Repeat == times:
                        break
                    else:
                        time.sleep(ncol)


                except Exception as e: print(e)

            else:
                blcktime = s_time - time.time()
                btime = blcktime / 60
                print('Account has been blocked after %s Minutes from Launch' % btime)
                break
        accchk = getacc()
        if accchk is not False:

            cooldownran = randrange(randf, randl)
            print('picked %s for sleeping')

            cooldwnm = cooldownran / 60
            timeused = cooldownran / 8
            timeusedm = timeused / 60
            print('\naccount done sleeping for %s minutes'%cooldwnm)
            sstart = time.time()
            time.sleep(timeused)
            print('\nstill active while in %s minutes sleep\n' % cooldwnm)
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

        else:
            Repeat =+ 100
            print('Previous account is blocked: %s'%email)
        reacc += 1





sec = time.time() - s_time
minu = sec / 60
print("\n\nThe bot finished within %s minutes" % minu)
