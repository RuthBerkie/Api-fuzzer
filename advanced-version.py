import requests  # library used to send http requests to web servers.
import time      

#internal dictionary of common API paths to test
API_WORDLIST = [
    "api", "api/v1", "api/v2", "v1", "v2", "rest", "graphql", "graph",
    "json", "html", "ip", "user-agent", "headers", "anything", "uuid", "xml",
    "status/200", "status/404", "status/418", "status/500", "delay/1",
    "api/auth", "api/login", "api/register", "api/users", "api/me", "api/profile",
    "api/swagger.json", "swagger.json", "openapi.json", "api/docs", "docs",
    "api/health", "api/status", "api/version", "healthz", "metrics",
    "robots.txt", "favicon.ico", "index.html", "sitemap.xml"
]
#the scanning function, accepting the target URL and the wordlist array
def loop(target_url, wordlist):
    print(f"\n[ * ] Starting process against {target_url}...")
    print(f"[ + ] Successfully loaded {len(wordlist)} test paths locally.")
    print("[ * ] Displaying ONLY successful paths (Status: 200)...")
    # Prints a clean horizontal separator line for visual organization in the console
    print("-" * 60)

    #iterate through every single word in the wordlist array, remove any characters other than the word
    for word in wordlist:
        clean_word = word.strip()
        if not clean_word:
            continue
            
        try:
            # Send the request to the target address
            res = requests.get(url=f"{target_url}/{clean_word}", timeout=5)
            
            # STRICT FILTER: Only print if the path actually returns a 200 OK status
            if res.status_code == 200:
                print(f"[200 OK] -> /{clean_word}")
                
        except requests.exceptions.RequestException:
            # Quietly skip network hiccups or timeouts
            continue
            
        # Tiny delay to prevent terminal lag and respect server performance
        time.sleep(0.02)
        
    print("-" * 60)
    print("[ * ] Process finished.")

# standard Python entry point idiom ensuring code only runs when executed directly
if __name__ == "__main__":
    user_input = input("Enter the target IP(e.g., 192.168.1.1) or domain: ").strip()
    
    # Auto-format target protocol prefix
    if not user_input.startswith("http://") and not user_input.startswith("https://"):
        target_base = f"http://{user_input}"
    else:
        target_base = user_input

    # Strip accidental trailing forward slashes
    target_base = target_base.rstrip('/')

    # Executes the directory scanner function using the prepared URL parameters and wordlist
    try:
        loop(target_base, API_WORDLIST)
    except KeyboardInterrupt:
    # Prints a clean exit verification string and terminates the execution stream cleanly
        print("\n[!] Script stopped cleanly by the user.")
