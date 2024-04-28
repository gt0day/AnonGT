from core.config.librareis import *
from core.config.functions import is_started, clear
from core.assets.alerts import ERROR, red, green, yellow
from core.assets.banner import logo

class ONION:

    # https://github.com/tsierawski/oniongen-py/tree/main
    def onion_gen():
        '''

            oniongen-py

            v3 .onion vanity URL generator written in Python3

            This is just a toy program, if you need to generate .onion
            url you will be better off with another tool.

            ---

            https://gitweb.torproject.org/torspec.git/tree/rend-spec-v3.txt#n2135

            "6. Encoding onion addresses [ONIONADDRESS]

            The onion address of a hidden service includes its identity public key, a
            version field and a basic checksum. All this information is then base32
            encoded as shown below:

                onion_address = base32(PUBKEY | CHECKSUM | VERSION) + ".onion"
                CHECKSUM = H(".onion checksum" | PUBKEY | VERSION)[:2]

                where:
                - PUBKEY is the 32 bytes ed25519 master pubkey of the hidden service.
                - VERSION is an one byte version field (default value '\x03')
                - ".onion checksum" is a constant string
                - CHECKSUM is truncated to two bytes before inserting it in onion_address

            Here are a few example addresses:

                pg6mmjiyjmcrsslvykfwnntlaru7p5svn6y2ymmju6nubxndf4pscryd.onion
                sp3k262uwy4r2k3ycr5awluarykdpag6a7y33jxop4cs2lu5uz5sseqd.onion
                xa4r2iadxm55fbnqgwwi5mymqdcofiu3w6rpbtqn7b2dyn7mgwj64jyd.onion"

        '''

        # check if started
        if is_started() == 1:
            clear
            print(red(logo))


            site_count = input(f"{yellow('Enter number of addresses to find: ')}")
            site_regex = input(f"{yellow('Enter pattern addresses should match: ')}")

            # Eye candy
            def printProgressBar(value, target, proc):
                size = 10
                progress = value / int(target)
                sys.stdout.write('\r')
                bar = '▒' * int(size * progress)
                bar += ' ' * int(size * (1 - progress))
                sys.stdout.write(f"{bar:{size}s} {int(100 * progress)}% {proc} addresses tested")
                sys.stdout.flush()


            # Time start
            start_time = time.process_time()

            # Stats
            vanity_onions = 0
            processed = 0

            while (vanity_onions < int(site_count)):

                # Generate key pair
                priv_key = SigningKey.generate()
                pub_key = priv_key.verify_key

                # Checksum
                checksum = hashlib.sha3_256(b".onion checksum" + bytes(pub_key) + b"\x03")

                # Onion address
                onion = (base64.b32encode(bytes(pub_key) + checksum.digest()[:2] + b'\x03')).decode(
                    "utf-8").lower() + ".onion"

                # Check regular expression
                if re.match(site_regex, onion):

                    # Check for "onions" folder
                    if not path.exists("onions"):
                        makedirs("onions")

                    # Check for vanity .onion
                    if not path.exists("onions/" + str(onion)):
                        makedirs("onions/" + onion)

                        # Save private key
                        f = open("onions/" + onion + "/hs_ed25519_secret_key", "wb")
                        f.write(b"== ed25519v1-secret: type0 ==\x00\x00\x00" + bytes(priv_key))
                        f.close()

                        # Save public key
                        f = open("onions/" + onion + "/hs_ed25519_public_key", "wb")
                        f.write(b"== ed25519v1-public: type0 ==\x00\x00\x00" + bytes(pub_key))
                        f.close()

                        # Save hostname
                        f = open("onions/" + onion + "/hostname", "w+")
                        f.write(onion)
                        f.close()

                        # Append Onion Links
                        f = open(f"onions-{site_regex}-{site_count}", "a")
                        f.write(onion + "\n")
                        f.close()

                        # Print
                        # print(f"\r {green(onion)}")
                        try:
                            data = get(onion)
                        except:
                            data = 'error'
                        if data != 'error':
                            url = green(onion)
                            status = green('Active')
                            status_code = green(data.status_code)
                            soup = BeautifulSoup(data.text, 'html.parser')
                            page_title = green(str(soup.title))
                            page_title = page_title.replace('<title>', '')
                            page_title = page_title.replace('</title>', '')
                        elif data == 'error':
                            url = red(onion)
                            status = red("Inactive")
                            status_code = red('NA')
                            page_title = red('NA')
                        print("\n")
                        print(url, ': ', status, ': ', status_code, ': ', page_title)
                        print("\n")

                    vanity_onions += 1

                processed += 1

                if (vanity_onions < int(site_count)):
                    # Print Eye Candy
                    printProgressBar(vanity_onions, site_count, processed)

            elapsed_time = time.process_time() - start_time

            print(green(f"{vanity_onions} matching entries from {processed} generated .onion URLs found in {elapsed_time}s"))

        else:
            ERROR("Please Start AnonGT.")

    def check():
        # check if started
        if is_started() == 1:
            clear
            print(red(logo))
            in_file = input(green("Submit the URL File: "))
            if path.exists(in_file):
                input_file = open(in_file, 'r')

                for url in input_file:
                    url = url.rstrip('\n')
                    try:
                        data = get(url)
                    except:
                        data = 'error'
                    if data != 'error':
                        url = green(url)
                        status = green('Active')
                        status_code = green(data.status_code)
                        soup = BeautifulSoup(data.text, 'html.parser')
                        page_title = green(str(soup.title))
                        page_title = page_title.replace('<title>', '')
                        page_title = page_title.replace('</title>', '')
                    elif data == 'error':
                        url = red(url)
                        status = red("Inactive")
                        status_code = red('NA')
                        page_title = red('NA')
                    print(url, ': ', status, ': ', status_code, ': ', page_title)
            else:
                ERROR("File Not Exist.")
        else:
            ERROR("Please Start AnonGT.")