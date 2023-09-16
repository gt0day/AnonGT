from core.config.functions import clear
from core.assets.colors import red, green
from core.config.config import VERSION


def about():
    about = f"""                                                                  
        {red("AnonGT")} {green("- redirect all traffic through tor network")}                         
        {red("VERSION:")} {green(VERSION)}
        
        {red("DESCRIPTION")}                                                               
        {green("Script to redirect all traffic through tor network including")}              
        {green("dns queries for anonymizing entire system")}                                 
        {green("killing dangerous applications")}                                            
        {green("clear configs & logs")}                                                      
        {green("firefox browser anonymization")}      
        {green("Changing Mac Address")}   

        {red("[Telegram]")}                                                                
        {green("https://t.me/gt0day")}                                                                                                   
        {red("[Youtube]")}                                                                 
        {green("https://youtube.com/@GT0day")}                                               

        {red("[Github]")}                                                                  
        {green("https://github.com/gt0day")}                                                 

        {red("[Blogger]")}
        {green("https://gt0day.blogspot.com/")}

        {red("[ Dark Web Onion Links ]")}                                                 
        {green("https://github.com/gt0day/DarkWeb")}                                         

        {red("[ Burp-Suite Professional Activation ]")}                                    
        {green("https://github.com/gt0day/Burp-Suite")}                                      
    """

    print(about)
