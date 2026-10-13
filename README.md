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
