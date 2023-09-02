from core.config.config import VERSION
from core.assets.colors import red,green,blue
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
        {green(f"--==[ AnonGT - Anonymous Ghost by GT0Day ]==--")}
              {green(" https://github.com/GT0Day/AnonGT")}
"""


# banner with version
def banner():
    banner = f"""
    {red(logo)}     
                {anongt_isactive()}   {tor_isacttive()}
    {green('''         
    Let's To Be Anonymous Ghost!
    Commands:
        start    - Anonymous Mode Start 
        stop     - Anonymous Mode Stop
        status   - Watch Tor Traffic
        myinfo   - Get Your Information
        chngid   - Change Tor Identity
        chngmac  - Change MAC Addresses Of All Interfaces
        rvmac    - Revert MAC Addresses Of All Interfaces
        wipe     - Memory Wipe & Clear Logs
        ----[ I2P Related Features ]----
        starti2p - Start I2P Services
        stopi2p  - Stop  I2P Services
        --------------------------------
        checku   - Check Update
        about    - About US
    ''')}
    """

    print(banner)