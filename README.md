api fuzzer 2.0.py: The best option to use.

    An offline, multi-threaded API directory discovery tool that uses concurrent network workers to rapidly cross-reference a locally stored dictionary file (common.txt) against a targeted web server. 
     
    It isolates and surfaces active endpoints by filtering exclusively for 200 OK HTTP responses, utilizing an in-place terminal progress counter to display live metrics without cluttering the console interface

the fuzz.py is simple script but can search through a large number of endpoint depending on the wordlist provided while the advanced-version.py does the same things with a smaller local wordlist but the user does not need to edit the code every time they want to fuzz a certain domain, it is interactive and everything is done in the terminal 

fuzz .py: 

         This script is a directory and API endpoint fuzzer designed to discover hidden or valid paths on a web server.

        • Reads a wordlist: 
           It accepts input line-by-line from the terminal (sys.stdin), which typically consists of a list of potential file or directory names.
        • Cleans the input:
           It strips away hidden newline characters (\n) and skips any empty lines.
        • Sends requests: 
           It automatically sends an HTTP GET request to a specified IP address for every word in the list (e.g., http://IP/secret-folder).
        • Filters results: 
           It completely ignores standard "Not Found" errors (404 status codes).
        • Handles output: 
           If it finds a valid page or directory, it prints the status code and the path. 
           If the response contains JSON data, it prints the JSON payload; otherwise, it handles the text/HTML gracefully without crashing.
 faster method.py:
 
        This script is a more interactive but with less wordlist version of the fuzz.py script
    
       • User Input & Formatting: It asks you for an IP address or domain name, automatically fixes missing prefixes (like adding http://), and cleans up accidentalslashes.
       • Automated Request Loop: It loops through a built-in list of common API routes and web files (such as api/v1, json, and robots.txt). 
         It sends a web request to the target server for every word on the list.
       • Strict Filtering: It filters out all failed attempts, bad requests, and error pages. 
         It only prints successful paths that return a 200 OK status code, displaying each on its own clean line.
       • Network & Error Safety: It uses safety guards (try/except) so that network drops or timeouts won't crash the script.
         It also includes a tiny pause (time.sleep) between requests to avoid lagging your terminal or overloading the target server.
