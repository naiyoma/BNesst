
def write_sender_email(file):
    dict_emails = {}
    dict_domains = {}
    senders_addresses = []
    domains = []
    with open(file, "r") as f:
        info = f.readlines()
    for i in info:
        
        if "From " in i:
            words = i.split()
            email = words[1]
            senders_addresses.append(email)
        try:
            with open("sender_email.txt", "x") as f:
                for email in senders_addresses:
                    f.write("Sender: " + email + "\n")
        except:
                with open("sender_email.txt", "w") as f:
                    for email in senders_addresses:
                        f.write("Sender: " + email + "\n")
    for email in senders_addresses:
        # import  pdb; pdb.set_trace()
        domains.append(email.split("@")[1])
        if email not in dict_emails:
            count = senders_addresses.count(email)
            dict_emails[email] = count            
    # print(dict_emails)
    for domain in domains:
        if domain not in dict_domains:
            count = domains.count(domain)
            dict_domains[domain] = count  

    print(dict_domains)


write_sender_email("mbox-short.txt")