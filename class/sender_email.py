
def write_sender_email(file):
    dict_emails = {}
    dict_domains = {}
    senders_addresses = []
    domains = []
    with open(file, "r") as f:
        info = f.readlines()
    for i in info:
        if "From " in i:
            senders_addresses.append(i.split()[1])
        try:
            with open("sender_email.txt", "x") as f:
                for email in senders_addresses:
                    f.write("Sender: " + email + "\n")
        except:
                with open("sender_email.txt", "w") as f:
                    for email in senders_addresses:
                        f.write("Sender: " + email + "\n")
    domains = [email.split("@")[1] for email in senders_addresses]
    dict_emails = {email: senders_addresses.count(email) for email in senders_addresses if email not in dict_emails}
    dict_domains = {domain: domains.count(domain) for domain in domains if domain not in dict_domains}
    print(dict_domains)
  
write_sender_email("mbox-short.txt")