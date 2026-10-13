import requests  #Sends web requests to servers
import os        #Checks local files on disk
import sys       #Live inline terminal updates
from concurrent.futures import ThreadPoolExecutor, as_completed    # Imports thread pool modules for concurrent/parallel networking

# Define the local filename
WORDLIST_FILENAME = "common.txt"

#Controls how many network requests are transmitted at the exact same moment
MAX_THREADS = 25 

def load_local_wordlist():
# Checks if the specified wordlist file is missing from the directory path and displays an error message
    if not os.path.exists(WORDLIST_FILENAME):
        print(f"[ ! ] Error: '{WORDLIST_FILENAME}' not found in this folder!")
        print("[ ! ] Please make sure you saved the file in your project directory.")
        return None
        
    print(f"[ * ] Reading local wordlist '{WORDLIST_FILENAME}'...")
    # Opens the local file using a safe context manager, handling text encoding and ignoring invalid characters
    with open(WORDLIST_FILENAME, "r", encoding="utf-8", errors="ignore") as file:
        # Strips hidden spacing, and filters out completely empty or commented rows   
        wordlist = [line.strip() for line in file if line.strip() and not line.strip().startswith("#")]
    # Safely format numbers with thousands separators    
    print(f"[ + ] Successfully loaded {len(wordlist):,} words from your local file.\n")
    return wordlist

def check_endpoint(target_url, word):
    #Sends a single HTTP request to the target endpoint.
    try:
        res = requests.get(url=f"{target_url}/{word}", timeout=4)
        # Only return the word with a 200 code, drop the others quietly
        if res.status_code == 200:
            return f"[200 OK] -> /{word}"
    except requests.exceptions.RequestException:
        pass
    return None

# Initializes the ThreadPoolExecutor context manager to regulate concurrent request threads
def loop(target_url, wordlist):
    print(f"[ * ] Starting multi-threaded process against {target_url} using {MAX_THREADS} requests...")
    print("[ * ] Scanning endpoints (Only successful 200 responses will appear below)...")
    print("-" * 60)

    # Calculates the total size of the testing pool to establish the counter limit
    total_words = len(wordlist)
    # Initializes the successful/processed item counter tracker at zero
    completed_count = 0

    # ThreadPoolExecutor runs multiple check_endpoint tasks in parallel
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        # Submit all tasks to the executor pool
        futures = {executor.submit(check_endpoint, target_url, word): word for word in wordlist}
        
        # As each thread finishes, process its result immediately
        for future in as_completed(futures):
            completed_count += 1
            result = future.result()
            
            # If a successful path was found, print it cleanly
            if result:
                # Clear the current status line before printing the success message
                sys.stdout.write("\r" + " " * 70 + "\r")
                sys.stdout.flush()
                print(result)

            # Uses a carriage return '\r' to force the text cursor back to the start of the current row without making a new line
            sys.stdout.write(f"\r[ * ] Progress: {completed_count}/{total_words} words checked...")
            # Pushes the inline progress numbers onto the console interface screen immediately
            sys.stdout.flush()
            
    print("\n" + "-" * 60)
    print("[ * ] Process finished successfully.")

if __name__ == "__main__":
    user_input = input("Enter the target IP or domain (e.g., 192.168.1.1): ").strip()
    # Assesses if the input string lacks a compliant network communication protocol prefix
    if not user_input.startswith("http://") and not user_input.startswith("https://"):
        target_base = f"http://{user_input}"
    else:
        target_base = user_input
    # Chops off any accidental trailing forward slashes to avoid generating double slash pathways (//)
    target_base = target_base.rstrip('/')

    # Executes the disk file parsing module to construct the active operational array
    active_wordlist = load_local_wordlist()

    # Verifies that the dictionary file was populated and parsed successfully
    if active_wordlist:
        try:
            # Transfers the execution parameters to the concurrent checking loop interface
            loop(target_base, active_wordlist)
        # Intercepts manual operator cancellation triggers gracefully (Ctrl+C)    
        except KeyboardInterrupt:
            print("\n[!] Script stopped cleanly by the user.")
