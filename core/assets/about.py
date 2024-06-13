from core.assets.colors import red, green
from core.config.config import VERSION


def about():
    about = f"""                                                                  
        {red("AnonGT")} {green("- redirect all traffic through tor network")}                         
        {red("VERSION:")} {green(VERSION)}
        
        {red("DESCRIPTION")}                                                               
        {green("Script to Redirect ALL Traffic Through TOR Network Including")}              
        {green("DNS Queries For Anonymizing Entire System")}                                 
        {green("Killing Dangerous Applications")}                                            
        {green("Clear Configs & Logs")}                                                      
        {green("Firefox Browser Anonymization")}
        {green("Timezone Changer")}      
        {green("Mac Address Changer")}   
        {green("Change #IP Automatically")}
        {green("Anti MITM")}
        {green("Onion Links Generator")}
        {green("Onion Links Checker")}
        {green("Share/Receive Files Anonymously")}
        {green("Anonymous Chat On Tor Network")}
        {green("Host Your Website On Dark Web!")}

        {red("[Telegram]")}                                                                
        {green("https://t.me/gt0day")}    
        
        {red("[Youtube]")}                                                                 
        {green("https://youtube.com/@GT0day")}                                               

        {red("[Github]")}                                                                  
        {green("https://github.com/gt0day")}                                                 

        {red("[ Dark Web Onion Links ]")}                                                 
        {green("https://github.com/gt0day/DarkWeb")}                                         

        {red("[ Burp-Suite Professional Activation ]")}                                    
        {green("https://github.com/gt0day/Burp-Suite")}                                      
    """

    print(about)
