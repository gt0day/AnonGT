from core.config.librareis import *
from core.config.config import BACKUPDIR, CURRTENTDIR, TORRC, TOR_UID, TOR_PORT, TOR_DNS, TOR_EXCLUDE
from core.assets.alerts import *
from core.assets.banner import logo, banner
from core.assets.about import about
from core.config.functions import exec_command, get_process, clear, is_started, is_i2pstarted, check_update


# Anonymous Mode Functions
def check_backup_dir():
    if path.exists(BACKUPDIR) != True:
        INFO(f"Creating {BACKUPDIR}")
        exec_command(f"mkdir {BACKUPDIR}")


# start tor service
def start_service(s):
    cmd = ["systemctl", "is-active", s]
    service = get_process(cmd)
    if service != 'active':
        WARN(s + " is not active")
        exec_command(f"systemctl start {s}")
        MSG(f"started {s} service")
    else:
        WARN(f"{s} is active")
        exec_command(f"systemctl reload {s}")
        MSG(f"reloaded {s} service")


# stop tor service
def stop_service(s):
    cmd = ["systemctl", "is-active", s]
    service = get_process(cmd)
    if service == 'active':
        WARN(s + " is active")
        exec_command(f"systemctl stop {s}")
        MSG(f"stopped {s} service")
    else:
        WARN(f"{s} is not active")


def start_browser_anonymization():
    MSG("firefox browser anonymization started")
    if path.isdir("/etc/firefox-esr") == True or path.isdir("/etc/firefox") == True:
        exec_command(f"cp {CURRTENTDIR}/core/sources/anongt.js /etc/firefox-esr > /dev/null")
        exec_command(f"cp {CURRTENTDIR}/core/sources/anongt.js /etc/firefox > /dev/null")
    else:
        WARN("Browser anonymization only supports firefox and firefox not found on your system")


def stop_browser_anonymization():
    exec_command("rm -fr /etc/firefox-esr/anongt.js > /dev/null")
    exec_command("rm -fr /etc/firefox/anongt.js > /dev/null")
    MSG("firefox browser anonymization stopped")


# killing dangerous processes & applications
def safekill():
    WARN("killing dangerous processes & applications")
    exec_command("service network-manager force-reload > /dev/null 2>&1")
    # kill processes
    exec_command(
        "killall -q dnsmasq nscd chrome dropbox skype icedove thunderbird firefox firefox-esr chromium xchat hexchat transmission steam firejail pidgin /usr/lib/firefox-esr/firefox-esr")

    MSG("dangerous processes & applications killed")


# clean iptables
def flush_iptables():
    exec_command("/usr/sbin/iptables -F")
    exec_command("/usr/sbin/iptables -t nat -F")


# clean config
def wipe():
    exec_command("swapoff -a")
    exec_command("swapon -a")
    exec_command("echo 1024 > /proc/sys/vm/min_free_kbytes")
    exec_command("echo 3 > /proc/sys/vm/drop_caches")
    exec_command("echo 1 > /proc/sys/vm/oom_kill_allocating_task")
    exec_command("echo 1 > /proc/sys/vm/overcommit_memory")
    exec_command("echo 0 > /proc/sys/vm/oom_dump_tasks")
    # exec_command("sdmem -fllv > /dev/null 2>&1")

    # release DHCP address
    exec_command("dhclient -r > /dev/null 2>&1")
    exec_command("rm -f /var/lib/dhcp/dhclient* > /dev/null 2>&1")

    # remove cache
    exec_command(
        "bleachbit -c bash.history system.cache system.clipboard system.custom system.recent_documents system.rotated_logs system.tmp system.trash adobe_reader.cache chromium.cache chromium.session chromium.history chromium.form_history elinks.history emesene.cache epiphany.cache firefox.cache firefox.crash_reports firefox.url_history firefox.forms flash.cache flash.cookies google_chrome.cache google_chrome.history google_chrome.form_history google_chrome.search_engines google_chrome.session google_earth.temporary_files links2.history opera.cache opera.form_history opera.history > /dev/null 2>&1")

    # clear logs
    log_list = (
        "/var/log/messages", "/var/log/auth.log", "/var/log/kern.log", "/var/log/cron.log", "/var/log/maillog",
        "/var/log/boot.log", "/var/log/mysqld.log", "/var/log/secure", "/var/log/utmp", "/var/log/wtmp",
        "/var/log/yum.log", "/var/log/system.log", "/var/log/DiagnosticMessages", "~/.zsh_history", "~/.bash_history")
    for log in log_list:
        if path.isfile(log) == True or path.isdir(log) == True:
            exec_command(f"shred -vfzu {log} > /dev/null 2>&1")

    MSG("cleaned config & logs")


# get ip
def get_info():
    try:
        get_info = get("http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query", verify=True)

        ip = get_info.json()["query"]
        status = get_info.json()["status"]
        continent = get_info.json()["continent"]
        continentCode = get_info.json()["continentCode"]
        country = get_info.json()["country"]
        countryCode = get_info.json()["countryCode"]
        region = get_info.json()["region"]
        regionName = get_info.json()["regionName"]
        city = get_info.json()["city"]
        district = get_info.json()["district"]
        zip = get_info.json()["zip"]
        lat = get_info.json()["lat"]
        lon = get_info.json()["lon"]
        timezone = get_info.json()["timezone"]
        offset = get_info.json()["offset"]
        currency = get_info.json()["currency"]
        isp = get_info.json()["isp"]
        org = get_info.json()["org"]
        AS = get_info.json()["as"]
        asname = get_info.json()["asname"]
        reverse = get_info.json()["reverse"]
        mobile = get_info.json()["mobile"]
        proxy = get_info.json()["proxy"]
        hosting = get_info.json()["hosting"]


        info = f"""
    #IP: {ip}
    Status: {status}
    Continent: {continent}
    ContinentCode: {continentCode}
    Country: {country}
    CountryCode: {countryCode}
    Region: {region}
    RegionName: {regionName}
    City: {city}
    District: {district}
    ZIP: {zip}
    LAT: {lat}
    LON: {lon}
    TimeZone: {timezone}
    Offset: {offset}
    Currency: {currency}
    ISP: {isp}
    ORG: {org}
    AS: {AS}
    ASName: {asname}
    Reverse: {reverse}
    Mobile: {mobile}
    Proxy: {proxy}
    Hosting: {hosting}
    """
        print(green(info))
    except:
        ERROR("Remote #IP: unknown")


# backup torrc
def backup_torrc():
    exec_command(f"mv {TORRC} {BACKUPDIR}/torrc.bak")
    exec_command(f"chmod 644 {BACKUPDIR}/torrc.bak")
    MSG("backed up tor config")


# backup resolv config
def backup_resolv_conf():
    exec_command(f"mv /etc/resolv.conf {BACKUPDIR}/resolv.conf.bak")
    exec_command(f"chmod 644 {BACKUPDIR}/resolv.conf.bak")
    MSG("backed up nameservers")


# backup iptables
def backup_iptables():
    exec_command(f"iptables-save > {BACKUPDIR}/iptables.rules.bak")
    exec_command(f"chmod 644 {BACKUPDIR}/iptables.rules.bak")
    MSG("backed up iptables rules")


# backup sysctl rules
def backup_sysctl():
    exec_command(f"sysctl -a > {BACKUPDIR}/sysctl.conf.bak")
    exec_command(f"chmod 644 {BACKUPDIR}/sysctl.conf.bak")
    MSG("backed up sysctl rules")


# restore torrc
def restore_torrc():
    if path.isfile(BACKUPDIR + "/torrc.bak"):
        exec_command("rm -f /etc/tor/torrc")
        exec_command(f"mv {BACKUPDIR}/torrc.bak /etc/tor/torrc")
        MSG("restored tor config")


# restore resolv config
def restore_resolv_conf():
    if path.isfile(BACKUPDIR + "/resolv.conf.bak"):
        exec_command(f"rm -f {BACKUPDIR}/resolv.conf")
        exec_command(f"mv {BACKUPDIR}/resolv.conf.bak /etc/resolv.conf")
        MSG("restored nameservers")


# restoring iptables rules
def restore_iptables():
    if path.isfile(BACKUPDIR + "/iptables.rules.bak"):
        exec_command(f"iptables-restore < {BACKUPDIR}/iptables.rules.bak")
        exec_command(f"rm -f {BACKUPDIR}/iptables.rules.bak")
        MSG("restored iptables rules")


# restore sysctl rules
def restore_sysctl():
    if path.isfile(BACKUPDIR + "/sysctl.conf.bak"):
        exec_command(f"sysctl -p {BACKUPDIR}/sysctl.conf.bak > /dev/null 2>&1")
        exec_command(f"rm -f {BACKUPDIR}/sysctl.conf.bak")
        MSG("restored sysctl rules")


# configure nameservers
def gen_resolv_conf():
    nameservers = ''' 
# generated by anongt
nameserver 127.0.0.1
nameserver 1.1.1.1
nameserver 1.0.0.1
nameserver 208.67.222.222
nameserver 208.67.220.220
nameserver 8.8.8.8
nameserver 8.8.4.4
'''
    exec_command(f'cat > "/etc/resolv.conf" <<EOF {nameservers}')
    exec_command("chmod 644 /etc/resolv.conf")
    MSG("configured nameservers")


# configure tor
def gen_torrc():
    torconfig = f''' 
# generated by anongt
User {TOR_UID}
DataDirectory /var/lib/tor
VirtualAddrNetwork 10.192.0.0/10
AutomapHostsOnResolve 1
AutomapHostsSuffixes .exit,.onion
#define tor ports and explicitly declare some security flags
TransPort 127.0.0.1:{TOR_PORT} IsolateClientAddr IsolateSOCKSAuth IsolateClientProtocol IsolateDestPort IsolateDestAddr
SocksPort 127.0.0.1:9050 IsolateClientAddr IsolateSOCKSAuth IsolateClientProtocol IsolateDestPort IsolateDestAddr
ControlPort 9051
HashedControlPassword 16:CDB54331C01EBF746021C0192920B313A08B18FD351B3E8D859EA8C0E4
#use tor to resolve domain names
DNSPort 127.0.0.1:{TOR_DNS}
#daemonize
RunAsDaemon 1
# Sandbox 1 - tor package is not built with --enable-seccomp required to use this option.
HardwareAccel 1
#socket safety hacks
TestSocks 1
AllowNonRFC953Hostnames 0
WARNPlaintextPorts 23,109,110,143,80
#dns safety hacks
ClientRejectInternalAddresses 1
#circuit hacks
NewCircuitPeriod 40
MaxCircuitDirtiness 600
MaxClientCircuitsPending 48
UseEntryGuards 1
EnforceDistinctSubnets 1
'''

    exec_command(f'cat > "{TORRC}" <<EOF {torconfig}')
    exec_command(f"chmod 644 {TORRC}")
    MSG("configured tor")


# get uid owner
# TOR_UID = get_process(["id", "-u", "debian-tor"])

# apply iptables rules
def apply_iptables_rules():
    # set iptables nat
    exec_command(f"/usr/sbin/iptables -t nat -A OUTPUT -m owner --uid-owner {TOR_UID} -j RETURN")

    # set dns redirect
    exec_command(
        f"/usr/sbin/iptables -t nat -A OUTPUT -d 127.0.0.1/32 -p udp -m udp --dport 53 -j REDIRECT --to-ports {TOR_DNS}")
    exec_command(
        f"/usr/sbin/iptables -t nat -A OUTPUT -d 127.0.0.1/32 -p tcp -m tcp --dport 53 -j REDIRECT --to-ports {TOR_DNS}")
    exec_command(
        f"/usr/sbin/iptables -t nat -A OUTPUT -d 127.0.0.1/32 -p udp -m owner --uid-owner {TOR_UID} -m udp --dport 53 -j REDIRECT --to-ports {TOR_DNS}")

    # resolve .onion domains mapping 10.192.0.0/10 address space
    exec_command(f"/usr/sbin/iptables -t nat -A OUTPUT -p tcp -d 10.192.0.0/10 -j REDIRECT --to-ports {TOR_PORT}")
    exec_command(f"/usr/sbin/iptables -t nat -A OUTPUT -p udp -d 10.192.0.0/10 -j REDIRECT --to-ports {TOR_PORT}")

    # exlude locals
    cmd = f""" 
    for NET in {TOR_EXCLUDE} 127.0.0.0/9 127.128.0.0/10; do
        /usr/sbin/iptables -t nat -A OUTPUT -d "$NET" -j RETURN
        /usr/sbin/iptables -A OUTPUT -d "$NET" -j ACCEPT
    done
    """
    exec_command(cmd)

    # redirect all other output through tor
    exec_command(f"/usr/sbin/iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports {TOR_PORT}")
    exec_command(f"/usr/sbin/iptables -t nat -A OUTPUT -p udp -j REDIRECT --to-ports {TOR_PORT}")
    exec_command(f"/usr/sbin/iptables -t nat -A OUTPUT -p icmp -j REDIRECT --to-ports {TOR_PORT}")

    # accept already established connections
    exec_command("/usr/sbin/iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")

    # allow only tor output
    exec_command(f"/usr/sbin/iptables -A OUTPUT -m owner --uid-owner {TOR_UID} -j ACCEPT")
    exec_command("/usr/sbin/iptables -A OUTPUT -j REJECT")

    # TESTING block all incoming traffics
    # https://trac.torproject.org/projects/tor/wiki/doc/TransparentProxy
    exec_command("/usr/sbin/iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT")
    exec_command("/usr/sbin/iptables -A INPUT -i lo -j ACCEPT")

    exec_command("/usr/sbin/iptables -A INPUT -j DROP")

    # *filter FORWARD
    exec_command("/usr/sbin/iptables -A FORWARD -j DROP")

    # *filter OUTPUT
    exec_command("/usr/sbin/iptables -A OUTPUT -m state --state INVALID -j DROP")
    exec_command("/usr/sbin/iptables -A OUTPUT -m state --state ESTABLISHED -j ACCEPT")

    # Allow Tor process output
    exec_command(
        f"iptables -A OUTPUT -m owner --uid-owner {TOR_UID} -p tcp -m tcp --tcp-flags FIN,SYN,RST,ACK SYN -m state --state NEW -j ACCEPT")

    # Allow loopback output
    exec_command("/usr/sbin/iptables -A OUTPUT -d 127.0.0.1/32 -o lo -j ACCEPT")
    # iptables 1.8.5 can't use -o with input
    # exec_command("/usr/sbin/iptables -A INPUT -d 127.0.0.1/32 -o lo -j ACCEPT")

    # Tor transproxy magic
    exec_command(
        f'/usr/sbin/iptables -A OUTPUT -d 127.0.0.1/32 -p tcp -m tcp --dport "{TOR_PORT}" --tcp-flags FIN,SYN,RST,ACK SYN -j ACCEPT')

    # Allow OUTPUT to lan hosts in $_non_tor
    # Uncomment these 5 lines to enable.
    # cmd = """
    # for _lan in $_non_tor; do
    #     iptables -A OUTPUT -d $_lan -j ACCEPT
    # done
    # """
    # exec_command(cmd)

    # Log & Drop everything else. Uncomment to enable logging
    # exec_command('/usr/sbin/iptables -A OUTPUT -j LOG --log-prefix "Dropped OUTPUT packet: " --log-level 7 --log-uid')
    # exec_command("/usr/sbin/iptables -A OUTPUT -j DROP")

    ### Set default policies to DROP
    # exec_command("/usr/sbin/iptables -P INPUT DROP")
    # exec_command("/usr/sbin/iptables -P FORWARD DROP")
    # exec_command("/usr/sbin/iptables -P OUTPUT DROP")

    ### Set default policies to DROP for IPv6
    # exec_command("/usr/sbin/ip6tables -P INPUT DROP")
    # exec_command("/usr/sbin/ip6tables -P FORWARD DROP")
    # exec_command("/usr/sbin/ip6tables -P OUTPUT DROP")

    MSG("applied iptables rules")


# applying sysctl rules
def apply_sysctl_rules():
    # Disable Explicit Congestion Notification in TCP
    exec_command('/sbin/sysctl -w net.ipv4.tcp_ecn=0 > "/dev/null"')

    # window scaling
    exec_command('/sbin/sysctl -w net.ipv4.tcp_window_scaling=1 > "/dev/null"')

    # increase linux autotuning tcp buffer limits
    exec_command('/sbin/sysctl -w net.ipv4.tcp_rmem="8192 87380 16777216" > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.tcp_wmem="8192 65536 16777216" > "/dev/null"')

    # increase TCP max buffer size
    exec_command('/sbin/sysctl -w net.core.rmem_max=16777216 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.core.wmem_max=16777216 > "/dev/null"')

    # Increase number of incoming connections backlog
    exec_command('/sbin/sysctl -w net.core.netdev_max_backlog=16384 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.core.dev_weight=64 > "/dev/null"')

    # Increase number of incoming connections
    exec_command('/sbin/sysctl -w net.core.somaxconn=32768 > "/dev/null"')

    # Increase the maximum amount of option memory buffers
    exec_command('/sbin/sysctl -w net.core.optmem_max=65535 > "/dev/null"')

    # Increase the tcp-time-wait buckets pool size to prevent simple DOS attacks
    exec_command('/sbin/sysctl -w net.ipv4.tcp_max_tw_buckets=1440000 > "/dev/null"')

    # try to reuse time-wait connections, but don't recycle them
    # (recycle can break clients behind NAT)
    exec_command('/sbin/sysctl -w net.ipv4.tcp_tw_reuse=1 > "/dev/null"')

    # Limit number of orphans, each orphan can eat up to 16M (max wmem)
    # of unswappable memory
    exec_command('/sbin/sysctl -w net.ipv4.tcp_max_orphans=16384 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.tcp_orphan_retries=0 > "/dev/null"')

    # don't cache ssthresh from previous connection
    exec_command('/sbin/sysctl -w net.ipv4.tcp_no_metrics_save=1 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.tcp_moderate_rcvbuf=1 > "/dev/null"')

    # Increase size of RPC datagram queue length
    exec_command('/sbin/sysctl -w net.unix.max_dgram_qlen=50 > "/dev/null"')

    # Don't allow the arp table to become bigger than this
    exec_command('/sbin/sysctl -w net.ipv4.neigh.default.gc_thresh3=2048 > "/dev/null"')

    # Tell the gc when to become aggressive with arp table cleaning.
    # Adjust this based on size of the LAN. 1024 is suitable for most
    # /24 networks
    exec_command('/sbin/sysctl -w net.ipv4.neigh.default.gc_thresh2=1024 > "/dev/null"')

    # Adjust where the gc will leave arp table alone - set to 32.
    exec_command('/sbin/sysctl -w net.ipv4.neigh.default.gc_thresh1=32 > "/dev/null"')

    # Adjust to arp table gc to clean-up more often
    exec_command('/sbin/sysctl -w net.ipv4.neigh.default.gc_interval=30 > "/dev/null"')

    # Increase TCP queue length
    exec_command('/sbin/sysctl -w net.ipv4.neigh.default.proxy_qlen=96 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.neigh.default.unres_qlen=6 > "/dev/null"')

    # Enable Explicit Congestion Notification (RFC 3168), disable it
    # if it doesn't work for you
    exec_command('/sbin/sysctl -w net.ipv4.tcp_ecn=1 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.tcp_reordering=3 > "/dev/null"')

    # How many times to retry killing an alive TCP connection
    exec_command('/sbin/sysctl -w net.ipv4.tcp_retries2=15 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.tcp_retries1=3 > "/dev/null"')

    # Avoid falling back to slow start after a connection goes idle
    # keeps our cwnd large with the keep alive connections (kernel > 3.6)
    exec_command('/sbin/sysctl -w net.ipv4.tcp_slow_start_after_idle=0 > "/dev/null"')

    # Allow the TCP fastopen flag to be used,
    # beware some firewalls do not like TFO! (kernel > 3.7)
    exec_command('/sbin/sysctl -w net.ipv4.tcp_fastopen=3 > "/dev/null"')

    # This will enusre that immediatly subsequent connections use the new values
    exec_command('/sbin/sysctl -w net.ipv4.route.flush=1 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv6.route.flush=1 > "/dev/null"')

    # TCP SYN cookie protection
    exec_command('/sbin/sysctl -w net.ipv4.tcp_syncookies=1 > "/dev/null"')

    # TCP rfc1337
    exec_command('/sbin/sysctl -w net.ipv4.tcp_rfc1337=1 > "/dev/null"')

    # Reverse path filtering
    exec_command('/sbin/sysctl -w net.ipv4.conf.default.rp_filter=1 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.conf.all.rp_filter=1 > "/dev/null"')

    # Log martian packets
    exec_command('/sbin/sysctl -w net.ipv4.conf.default.log_martians=1 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.conf.all.log_martians=1 > "/dev/null"')

    # Disable ICMP redirecting
    exec_command('/sbin/sysctl -w net.ipv4.conf.all.accept_redirects=0 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.conf.default.accept_redirects=0 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.conf.all.secure_redirects=0 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.conf.default.secure_redirects=0 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv6.conf.all.accept_redirects=0 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv6.conf.default.accept_redirects=0 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.conf.all.send_redirects=0 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv4.conf.default.send_redirects=0 > "/dev/null"')

    # Enable Ignoring to ICMP Request
    exec_command('/sbin/sysctl -w net.ipv4.icmp_echo_ignore_all=1 > "/dev/null"')

    # Disable IPv6
    exec_command('/sbin/sysctl -w net.ipv6.conf.all.disable_ipv6=1 > "/dev/null"')
    exec_command('/sbin/sysctl -w net.ipv6.conf.default.disable_ipv6=1 > "/dev/null"')

    MSG("applied sysctl rules")


# Anonymous Mode CLass
class Anonymous:
    def Start():
        clear()
        print(red(logo))

        # check if started
        if is_started() == 1:
            ERROR("Anonymous Mode is already started")

        else:
            MSG("Start Anonymous Mode")

            cmd = input(f"{yellow('Do you want kill dangerous applications? ')} ").lower()
            if cmd == "y" or cmd == "":
                # killing dangerous applications
                safekill()

            # check backup dir
            check_backup_dir()

            # backup torrc
            backup_torrc()

            if is_i2pstarted() == 0:
                # backup resolve.conf
                backup_resolv_conf()

            # backup iptables rules
            backup_iptables()

            # backup sysctl rules
            backup_sysctl()

            # flush iptables
            flush_iptables()

            # generate new torrc
            gen_torrc()

            if is_i2pstarted() == 0:
                # generate new resolv.conf
                gen_resolv_conf()

            # start tor service
            start_service("tor")

            # apply new iptables rules
            apply_iptables_rules()

            # apply new sysctl rules
            apply_sysctl_rules()

            # start browser anonymization
            start_browser_anonymization()

            # wipe & clear logs
            wipe()

            # check tor
            exec_command("xdg-open 'https://check.torproject.org/?lang=en' > /dev/null 2>&1")

            exec_command(f"touch {BACKUPDIR}/started")
            MSG("Anonymous Mode Started")


    def Stop():
        clear()
        print(red(logo))

        # check if stopped
        if is_started() == 0:
            ERROR("Anonymous Mode is already stopped")

        else:
            MSG("Stop Anonymous Mode")

            cmd = input(f"{yellow('Do you want kill dangerous applications? ')} ").lower()
            if cmd == "y" or cmd == "":
                # killing dangerous applications
                safekill()

            # check backup dir
            check_backup_dir()

            # restore sysctl rules
            restore_sysctl()

            # re-enable ipv6
            exec_command("/sbin/sysctl -w net.ipv6.conf.all.disable_ipv6=0 > /dev/null 2>&1")
            exec_command("/sbin/sysctl -w net.ipv6.conf.default.disable_ipv6=0 > /dev/null 2>&1")

            # flush iptables rules
            flush_iptables()

            # restore iptables rules
            restore_iptables()

            # stop tor service
            stop_service("tor")

            # restore torrc
            restore_torrc()

            # check i2p stopped
            if is_i2pstarted() == 0:
                # restore resolv.conf
                restore_resolv_conf()

            # stop browser anonymization
            stop_browser_anonymization()

            # wipe & clear logs
            wipe()


            exec_command("killall tor > /dev/null 2>&1")

            exec_command(f"rm -f {BACKUPDIR}/started")
            MSG("Anonymous Mode Stoped")

    def Status():
        # check if started
        if is_started() == 1:
            exec_command("xterm -geometry 140x40 -e nyx &")
            clear()
            banner()
        else:
            clear()
            print(red(logo))
            ERROR("AnonGT is stopped")

    def MyInfo():
        clear()
        print(red(logo))

        get_info()

    def Change_ID():
        clear()
        print(red(logo))

        # check if stopped
        if is_started() == 0:
            ERROR("Anonymous Mode is already stopped")

        else:
            WARN("changing tor identity")
            stop_service("tor")
            sleep(1)
            start_service("tor")
            MSG("tor identity changed")


    def Change_Mac():
        clear()
        print(red(logo))

        WARN("Changing Mac Addresses")
        IFACES = netifaces.interfaces()
        for IFACE in IFACES:
            if IFACE != "lo":
                exec_command(f'ip link set {IFACE} down > "/dev/null"')
                exec_command(f'macchanger -r {IFACE} > "/dev/null"')
                exec_command(f'ip link set {IFACE} up > "/dev/null"')
        MSG("changed mac addresses")

    def Reverte_Mac():
        clear()
        print(red(logo))

        WARN("Reverting Mac Addresses")
        IFACES = netifaces.interfaces()
        for IFACE in IFACES:
            if IFACE != "lo":
                exec_command(f'ip link set {IFACE} down > "/dev/null"')
                exec_command(f'macchanger -p {IFACE} > "/dev/null"')
                exec_command(f'ip link set {IFACE} up > "/dev/null"')

        MSG("reverted mac addresses")

    def Wipe():
        clear()
        print(red(logo))

        wipe()


    def StartI2P():
        clear()
        print(red(logo))

        if is_i2pstarted() == 1:
            ERROR("I2P Already Started")
        else:
            MSG("Start I2P Services")
            check_backup_dir()
            if is_started() == 0:
                backup_resolv_conf()
                gen_resolv_conf()
            else:
                stop_service("tor")
            exec_command("sudo -u i2psvc i2prouter start > /dev/null 2>&1")
            if is_started() == 1:
                start_service("tor")
            sleep(2)
            exec_command("xdg-open 'http://127.0.0.1:7657/home' > /dev/null 2>&1")
            MSG("I2P Services Started")

            exec_command(f"touch {BACKUPDIR}/i2pstarted")

    def StopI2P():
        clear()
        print(red(logo))

        if is_i2pstarted() == 0:
            ERROR("I2P Already Stopped")
        else:
            MSG("Stop I2P Services")
            check_backup_dir()
            exec_command("sudo -u i2psvc i2prouter stop > /dev/null 2>&1")
            if is_started() == 0:
                restore_resolv_conf()
            MSG("I2P Services Stopped")

            exec_command(f"rm {BACKUPDIR}/i2pstarted")


    def CheckUpdate():
        clear()
        print(red(logo))

        check_update()


    def About():
        clear()
        print(red(logo))

        about()

