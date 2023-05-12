import os
import zipcodes
import re
import json
#import base_parser
import sys
import csv
import glob

#sys.argv[1]

class Bank:

    def __init__(self):
        self.date = None
        self.bankname = []
        self.photo_id = None
        self.account_number = None
        self.amount = []
        self.account_type = []

    def get_date_and_id_from_title(self, title):
        re1 = title.split("@")
        photo_id=""
        date=""
        if('.DS_Store' not in re1):
            #print("@@@@@@@@@@@@@@@@@@",re1)
            photo_id = re1[0].split("_")[1]
            date = re1[1].split("_")[0]
        return photo_id, date

    def check_bankname(self, content):
        # return bank name if finds a match from the given names
        # print(Banks)
        bank_list = ['1st source bank','allegiance bank','american national bank',
        'american national bank of texas','amplify credit union','anb bank','associated bank',
        'atlantic union bank','bank of america','bank of the west','banner bank','bb&t','bbva',
        'bbva usa','bmo harris bank','c1 bank','cadence bank','capital bank','capital one',
        'capital one 360','catholic federal credit union','chase','chase bank','citigroup',
        'citi','citizencredit union','citizens bank','citizens first bank','citizens national bank',
        'cnb bank','columbia bank','comerica bank','community bank','community banks of colorado',
        'community first bank','community state bank','compeer financial','cornerstone bank',
        'cornerstone community financial','country bank','crossfirst bank','crystal lake bank & trust',
        'crystal valley credit union','csb bank','dakota community bank','dakota heritage bank',
        'dakota state bank','dakota valley bank','davies county bank','ddn credit union',
        'diamond bank','dime community bank','discover bank','east west bank',
        'edward jones credit union','empower credit union','esl federal credit union',
        'farm bureau bank','fifth third bank','first citizens bank','first community bank',
        'first citizens national bank','first community credit union','first community financial bank',
        'first farmers bank & trust','first financial bank','first financial credit union',
        'first financial bank, na','first financial northwest bank','first midwest bank',
        'first national bank','first national bank and trust','first national bank of omaha',
        'first national bank texas','first national community bank','first national of nebraska',
        'first state bank','first state bank and trust','first western bank','firstbank',
        'fluvanna bank','fnb bank','fnb community bank','frost bank','ge capital',
        'ge capital retail bank','gemb','genisys credit union','george weston limited',
        'goldman sachs','goldman sachs bank usa','green dot bank','hancock bank',
        'hancock whitney bank','harborstone credit union','hawaii national bank','hillcrest bank',
        'hilltop national bank','houston texans credit union','huntington bank','icici bank',
        'inland bank','integrity bank','interbank','investors bank','investors community bank',
        'jpmorgan chase','keybank','klein bank','kleinbank','lake city bank','lakeside bank',
        'landmark bank','latitude financial services','legacytexas bank','liberty bank',
        'libertyville bank & trust','lincoln savings bank','little river bank','logix credit union',
        'm&t bank','madison county state bank','maine savings federal credit union',
        'manchester credit union','maspeth federal savings and loan association','mecu credit union',
        'merchants bank','merchants and farmers bank','midfirst bank','midland states bank',
        'milwaukee credit union','minnwest bank','mizzou credit union','mounthaven bank',
        'mt. morris bank','mt. sterling national bank','mt. vernon bank & trust',
        'mutual of omaha bank','navy federal credit union','nebraska state bank',
        'nebraska state bank and trust','nebraska state bank of commerce','nicolet national bank',
        'north community bank','north central bank','north shore bank','northwest bank',
        'northwest bank and trust','northwest community credit union','northwest savings bank',
        'northwestfederal credit union','norwegian american credit union',
        'norwegian american hospital employees credit union','norwegian credit union',
        'ocean first bank','omega federal credit union','oneamerica bank','oneaz credit union',
        'oneunited bank','orchard bank','pinnacle bank','pinnacle bank nebraska','pnb bank',
        'pnc bank','pnc financial services','premier bank','premier bank inc','premier credit union',
        'premier members credit union','premier valley bank','provident bank','provident credit union',
        'ps bank','pscu','puget sound cooperative credit union','pulse federal credit union',
        'quest credit union','quorum federal credit union','reliant bank','republic bank',
        'republic bank of chicago','republic bank of nebraska','republic bank of texas',
        'republic first bank','republic state mortgage','republican valley bank','richmond state bank',
        'rock valley credit union','rockland trust','roundbank','rural heritage bank',
        'rural heritage bank and trust','rural state bank','s&t bank','s&t bank, na',
        'safra national bank of new york','sandy spring bank','santander bank','saratoga national bank',
        'saratoga national bank and trust','sbt bank','scotia bank','scotiabank','sdccu',
        'seaboard federal credit union','seacoast bank','seaway bank and trust','seaway community bank',
        'security bank','security bank of kansas city','security credit union','security first bank',
        'security state bank','security state bank of marine','sefcu','selco community credit union',
        'service credit union','servicefirst bank','serviceone credit union','shawmut bank','shore bank',
        'shore community bank','signature bank','skagit state bank','skokie bank',
        'skokie valley community federal credit union','smartbank','smith county national bank',
        'sns bank','south jersey federal credit union','southern trust bank','southwest missouri bank',
        'southwest national bank','sparks state bank','sparks state bank and trust','spencer savings bank',
        'spire credit union','standard bank and trust','standard bank and trust company',
        'standard chartered','standard chartered bank','star financial bank','star one credit union',
        'state bank','state bank and trust','state bank and trust company','state bank financial',
        'state bank of india','state bank of liang','state bank of long island','state bank of the lakes',
        'state department federal credit union','state employees credit union','state farm bank',
        'statewide federal credit union','stonebridge bank','stonegate bank','suntrust bank','svb',
        'svb financial group','synergy bank','texas capital bank','texas first bank',
        'texas bank and trust','texas trust credit union','the bank','the bank of clarendon',
        'the bank of edwardsville','the bank of greene county','the bank of hancock county',
        'the bank of harrison county','the bank of herrin','the bank of henderson','the bank of hickman',
        'the bank of hinsdale','the bank of jamestown','the bank of kentucky','the bank of lancaster county',
        'the bank of madison','the bank of marin','the bank of middletown','the bank of missouri',
        'the bank of new glarus and sugar river','the bank of new york mellon','the bank of nova scotia',
        'the bank of oak ridge','the bank of perryville','the bank of south carolina',
        'the bank of southside virginia','the bank of tampa','the bank of the commonwealth',
        'the bank of the james','the bank of the ozarks','the bank of tennessee','the bank of tony',
        'the bank of washington','the bank of wayne county','the bank of western massachusetts',
        'the bank of white county','the bank of winchester','the bank of york','the banks company',
        'the banks of the san juans','the banks of the san juans, n.a.','the banks of the san juans, na',
        'the benjamin bank','the california bank','the capital bank','the cedar valley bank and trust company',
        "the citizen's national bank",'the city national bank of florida','the commercial and savings bank',
        'the community bank','the community bank of raymore','the community bank of the chesapeake',
        'the cooperative bank','the credit union of colorado','the fairfield national bank',
        'the farmers and merchants state bank of argonia','the farmers bank','the farmers bank and trust',
        'the farmers bank and trust company','the farmers bank of china','the farmers state bank',
        'the farmers state bank of la porte city','the fauquier bank','the fauquier bank, na',
        'the fayette county bank','the fidelis group','the flint hills bank','the focus bank',
        'the frederick county bank','the freeport state bank','the fremont bank','the fremont company',
        'the fremont national bank','the fremont national bank and trust','the fremont national bank and trust company',
        'the fremont national bank of joliet','u.s. bank','u.s. bank national association',
        'u.s. bank, na','u.s. bancorp','u.s. bankcorp','ucbi','ucb&t','ucb&t co','ucb&t company',
        'ucb&t, co','ucb&t, company','ucb&t, national association','ucb&t, na','valley national bank',
        'xceed financial credit union','yadkin bank','yadkin valley bank and trust',
        'yadkin valley bank and trust company','yadkin valley financial corporation','zb',
        'zions bancorporation','zions bank','america first credit union' , 'wells fargo' , 
        'huntington' , 'arvest' , 'union bank' , 'woodforest national bank' , 'ameritrade' , 'regions' , 
        'commomwealth bank' , 'nevada state bank', 'truist', 'space coast credit union', 'm&t bank' , 
        'financial plus credit union' , 'greater nevada credit union' , 'usaa']
        re = set()
        
        ##### check bank name in text #####
        content_lower = content.lower()
        # print()
        for i in bank_list:
            if i in content_lower:
                re.add(i)
        return re

    def check_type(self, content):
        acc_type = ["saving", "checking", "credit"]
        re = set()
        content_lower = content.lower()
        for i in acc_type:
            if i in content_lower:
                re.add(i)
        return re

    def check_amount(self, content):
        # return the amounts present in the content
        result = {"amount":0,"Credited_sum":0,"Debited_sum":0} 
        credited_amount=[]
        debited_amount=[]
        # find with digit and decimal
        # for i in re.finditer(r"\d{1,4}(?:,\d{4})*(?:\.\d+)+", content):
        for i in re.finditer(r"\d{1,3}(?:,\d{3})*(?:\.\d+)+", content):
            # print(i)
            index = int(i.span()[0])
            check_trans = content[index-3:index]
            if("+" in check_trans):
                s=i.group().replace("$","").replace(",","")
                if(s.count(".")>1): 
                    s = s.replace(".","",1)
                    print("#############################",s)

                    
                credited_amount.append(s)
            elif("-" in check_trans):
                s=i.group().replace("$","").replace(",","")
                if(s.count(".")>1): 
                    s = s.replace(".","",1)
                    print("#############################",s)

                debited_amount.append(s)
            else:
                result["amount"]=i.group()
        #find with S digit and deciaml
        # for i in re.finditer(r"(\b[S][0-9]*\.[0-9]*)|\b[S][0-9]+", content):
        #     print(i.group())
        #     result.add(i.group()[1:])
        # for i in re.finditer(r"\b[S]\d{1,4}(?:,\d{4})*(?:\.\d+)+|\b[S]\d{1,4}(?:,\d{4})*", content):
        for i in re.finditer(r"\b[S]\d{1,3}(?:,\d{3})*(?:\.\d+)+|\b[S]\d{1,3}(?:,\d{3})*", content):
            # print(i.group())
            index = int(i.span()[0])
            check_trans = content[index-3:index]
            if("+" in check_trans):
                s=i.group().replace("$","").replace(",","").replace("S","")
                if(s.count(".")>1): 
                    s = s.replace(".","",1)
                    print("#############################",s)
                    
                credited_amount.append(s)
            elif("-" in check_trans):
                s=i.group().replace("$","").replace(",","").replace("S","")
                if(s.count(".")>1): 
                    s = s.replace(".","",1)
                    print("#############################",s)

                debited_amount.append(s)
            else:
                result["amount"] = i.group()[1:]
        # find with $ digit and decimal
        # for i in re.finditer(r"\$\d+(?:\.\d+)?", content):
        #     print(i.group())
        #     result.add(i.group()[1:])
        # for i in re.finditer(r"\$\d{1,3}(?:,\d{3})*(?:\.\d+)+|\$\d{1,3}(?:,\d{3})*", content):
        # for i in re.finditer(r"(?:\d{1,3})(?:,\d{1,3})*(?:,\d{1,3})(?:\.\d+)+", content):
        for i in re.finditer(r"\$\d{1,3}(?:,\d{3})*(?:\.\d+)+|\$\d{1,3}(?:,\d{3})*", content):
            # print(i.group())
            index = int(i.span()[0])
            check_trans = content[index-3:index]
            if("+" in check_trans):
                s=i.group().replace("$","").replace(",","")
                if(s.count(".")>1): 
                    s = s.replace(".","",1)
                    print("#############################",s)
                    
                credited_amount.append(s)
            elif("-" in check_trans):
                s=i.group().replace("$","").replace(",","")
                if(s.count(".")>1): 
                    s = s.replace(".","",1)
                    print("#############################",s)

                debited_amount.append(s)
            else:
                result["amount"] = i.group()[1:]
        
        credited_amount = list(set(credited_amount))
        debited_amount = list(set(debited_amount))
        
        credited_sum = 0
        debited_sum = 0
        for i in credited_amount:
            credited_sum=credited_sum+float(i)
            
        for i in debited_amount:
            debited_sum=debited_sum+float(i)
        
        result["Credited_sum"]=credited_sum
        result["Debited_sum"]=debited_sum
        print(result)
        
        return result

    def get_count_available_balance(self, content):
        # return the count of available amount
        word = "available balance"
        cnt = 0
        # content_lower = content.lower()
        for line in content:
            line = line.lower()
            if word in line:
                cnt += 1
        return cnt

    def data_assign_byrow(self, photo_id, date, bank, account_type, amount, balance_cnt,writer):
        amount.sort(reverse=True)
        # amount = amount[:balance_cnt]
        num_banks = len(bank)
        num_acc_type = len(account_type)
        num_amount = len(amount)
        if num_banks == 1:
            for i in range(0, max(num_banks,num_acc_type,num_amount)):
                if num_acc_type > 0:
                    acc_type = account_type.pop(0)
                    num_acc_type -= 1
                else:
                    acc_type = ""

                if num_amount > 0:
                    amt = amount.pop(0)
                    avail_amount=amt["amount"]
                    debited_amount=amt["Debited_sum"]
                    credited_amount=amt["Credited_sum"]
                    num_amount -= 1
                else:
                    amt = ""
                    avail_amount=""
                    debited_amount=""
                    credited_amount=""
                writer.writerow([photo_id, date, bank[0], acc_type, "", avail_amount,debited_amount,credited_amount])
            return 
        else:
            for i in range(0, max(num_banks,num_acc_type,num_amount)):
                if num_acc_type > 0:
                    acc_type = account_type.pop(0)
                    num_acc_type -= 1
                else:
                    acc_type = ""
                if num_amount > 0:
                    amt = amount.pop(0)
                    avail_amount=amt["amount"]
                    debited_amount=amt["Debited_sum"]
                    credited_amount=amt["Credited_sum"]
                    num_amount -= 1
                else:
                    amt = ""
                    avail_amount=""
                    debited_amount=""
                    credited_amount=""
                if num_banks > 0:
                    bank_name = bank.pop(0)
                    num_banks -= 1
                else:
                    bank_name = ""
                writer.writerow([photo_id, date, bank_name, acc_type, "",avail_amount,debited_amount,credited_amount])

if __name__ == '__main__':
    #folder_textdoc_path = sys.argv[1]
    #textdoc_paths = base_parser.get_textdoc_paths(folder_textdoc_path)
    textdoc_paths = glob.glob(r'/Users/sravanipotlapalli/Bank_Accounts_Parser/BankAccounts_January/BankAccounts/1/*.txt')
    print(len(textdoc_paths))
    #print("HelloHElllo")
    #print(textdoc_paths)
    headerList = ['Pic Id', 'Date', 'Bank Name', 'Account Type', 'Account Number', 'Amount', 'Credited Amount','Debited Amount']
    with open('bank_accounts_data'+'.csv','w', newline='', encoding='utf-8') as f1:
        dw = csv.DictWriter(f1, delimiter=',', fieldnames=headerList)
        dw.writeheader()
        writer=csv.writer(f1, delimiter=',')#lineterminator='\n',
    # for i in np.arange(0,9):
    #     row = data[i]
    #     writer.writerow(row)
  
        for text_doc in textdoc_paths:
            writer=csv.writer(f1, delimiter=',')
            check = Bank()
            file_name = os.path.basename(text_doc)

            #### parse photo id and date
            photo_id, date = check.get_date_and_id_from_title(file_name)
            if photo_id:
                check.photo_id = photo_id
            if date:
                check.date = date

            ### parse zipcode and state
            with open(text_doc, encoding = "utf-8") as f:
                content = f.readlines()
            if content:
                text_des = content[-1]
            else:
                writer.writerow([check.photo_id, check.date, "", "", "", "", ""])
                continue
            #print((text_des).encode('utf-8'))

            if content:
                info_bank_type = check.check_type(text_des)
                check.account_type.extend([i for i in info_bank_type])

            #### parse bankname
                info_bank = check.check_bankname(text_des)
                check.bankname.extend([i for i in info_bank])
                for i in check.bankname:
                    #print("bank:",i)
                    pass
                check.amount = [check.check_amount(text_des)]
                #check.amount.extend(i for i in info_amount)
                avail_amt = check.get_count_available_balance(content[:-1])

            # for i,code in enumerate(check.zipcode):
            #     writer.writerow()
            else:
                print("Empty file")
            #print(check.photo_id, check.date, check.bankname, check.account_type, check.account_number, check.amount)
            # writer.writerow([check.photo_id, check.date, check.bankname, check.account_type, check.account_number, check.amount, avail_amt])
            check.data_assign_byrow(check.photo_id, check.date, check.bankname, check.account_type, check.amount, avail_amt, writer)
