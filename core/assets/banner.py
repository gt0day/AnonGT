from core.assets.colors import red, green
from core.config.functions import anongt_isactive, tor_isacttive

logo = f"""
                        ..::::::-::::..                           
                  .:-----:::......::::-----:.                     
               :---:...     .  ..  .    ...:---:                  
            :--:..  ........ :#=%#.........  ..:--.               
          :=-.  ..............:-%+............   .-=:             
        :=:.  ................ #= ...............  .-=:           
      .=-. ....................+=................ .. .-=          
     :+. ..  .. ...........   ..    ............ ..  . :+.        
    -=  . .-.+- .  ....    .:=*+*+-:    .....    +=.- . .+:       
   :+  . ..+**.         ..=@#.=%+:-@#:.          :#*-. .  +.      
  .+     #:=#:     =+*#%%@@@- -%+. %@@@%##*+.     =%-+*   .+      
  +:   .:=+*:     =@@@@@@@@@:  %+  %@@@@@@@@%      -#+-:.  :=     
 :=    #- #=      #@@@@@@@@@= -@% .@@@@@@@@@@:      ** #=   +.    
 =:    *:*+       %@@@@@@@@@% +@@ =@@@@@@@@@@-      .*+==   --    
 +.  .*..**      :@@@@@@@@@@@*+@@+@@@@@@@@@@@*       #+ -*  .+    
 +    @=-@-      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@.      =@.%#  .+    
 +   :::+**      %@@@@@@@@@@@@@@@@@@@@@@@@@@@@-     :*#:-:: .+    
 +.  #%- #@.    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+     :@= -@+ :=    
 --   +@=##%-   -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#    =*@==%-  =:    
  +   =-:.+@+   +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    #@- -=:  +     
  --  =@%= %*++ .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@=  *=@+.*@#. =:     
   =:  :*@*--#@.  -#@@@@@@@@@@@@@@@@@@@@@@@@+   -@+-=%%=  -=      
    +:   -*= =@++#. :#@@@@@@@@@@@@@@@@@@@@=  :%=%# .**.  :=       
     =:  :*%%+++-@@* +@@@@@@@@@@@@@@@@@@@@ .%@*-+=#@#=  -=        
      -=    :++=::*%#%@@@@@@@@@@@@@@@@@@@@+##-.-=+-.   =-         
       .=:   .=*##*++@@@@@@@@@@@@@@@@@@@@@#=+*#*+-   -=.          
         :-:     .=+%@@@@@@@@@@@@@@@@@@@@@@+=:     :=:            
           :--.     +%@@@@@@@@@@@@@@@@@@@@#     .--:              
             .:-:.   :@@@@@@@@@@@@@@@@@@@*   .--:                 
                 ::-::@@@@@@@@@@@@@@@@@@@+:-::                    
                     .:-+*##%%%@%%%##*+-:.         
        {green(f"--==[ AnonGT - Anonymous Ghost by GTSec ]==--")}
              {green(" https://github.com/GT0Day/AnonGT")}
"""


# banner with version
def banner():
    banner = f"""
    {red(logo)}
                {anongt_isactive()}   {tor_isacttive()}
    {green('''
    Let's To Be Anonymous Ghost!
    Usage: anongt <options>
    ---------------------------------------------------------
         Options  | Descriptions
    ---------------------------------------------------------
         start    | Anonymous Mode Start
         start+   | Start With Secure Tor Bridges
         stop     | Anonymous Mode Stop
                -----
         status   | Watch Tor Traffic
         myinfo   | Get Your Information
         chngid   | Change Tor Identity
         amitm    | Anti MITM
                -----
         chngmac  | Change Mac Addresses Of All Interfaces
         rvmac    | Revert Mac Addresses Of All Interfaces
                -----
         oniongen | Onion Links Generator
         checko   | Onion Links Checker
                -----
         wipe     | Memory Wipe & Clear Logs
         checku   | Check Update
         about    | About US
    ---------------------------------------------------------
    ''')}
    """

    print(banner)
