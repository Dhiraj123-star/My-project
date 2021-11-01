# check domain registration using Python library

import whois

def is_registered(domain_name):
    """
    A function that returns a boolean indicating whether 
    a 'domain_name' is registered or not 
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

# driver code

if __name__ =="__main__":
    # list of registered and non-registered domains to test our function
    domains =[
        "google.com",
        "github.com",
        "unknownrandomdomain.com",
        "notregistered.co"
    ]
    # iterate over domains 

    for domain in domains:
        print(domain,"is registered" if is_registered(domain) else "is not registered")

        