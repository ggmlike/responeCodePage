# responeCodePage
Batch scanning of server response codes
1. install the libary in the project using command - pip install requests / tqdm
2. create file dataUrls.txt for wrating URLs-address
---------------------------------------------------------------------------
Attention! To avoid overloading the server, set the time.sleep(1) parameter to +2

Bulk response code checking, this script is useful for SEO specialists when analyzing 
page indexing. When running the script, you should be aware of your server's 
limitations. If you run the check with minimal delay, there might be issues with 
server availability. It is also essential to consider that when using DDoS-Guard or 
Cloudflare, the administrator may block your IP address, resulting in a loss of 
access to the resource.