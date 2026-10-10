import requests  # library used to send http requests to web servers.
import sys       # interact with standard input/output streams.

#loop through the standard input, until the status code becomes anything other than 404
def loop():
    for word in sys.stdin:
        clean_word = word.strip()  #Remove the hidden \n from the wordList line
        if not clean_word:
            continue
            
        res = requests.get(url=f"http://ENTER_IP_HERE/{clean_word}")
        
        if res.status_code == 404:
            continue
        else:
            #Prevent HTML responses from crashing the fuzzer if the server doesn't contain an API JSON response
            try:
                data = res.json()
                print(data)
            except:
                print(f"[+] Found non-JSON path: /{clean_word} (Status: {res.status_code})")
                
            print(res.status_code)
            print(clean_word)

loop()

    
