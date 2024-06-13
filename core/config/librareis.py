from os import system,getuid,path, makedirs
from requests import get
from urllib.request import urlopen
import re as r
from socket import gethostname, sethostname
from bs4 import BeautifulSoup
from time import sleep
import sys
import tempfile
import subprocess
import netifaces
from nacl.signing import SigningKey, VerifyKey
import nacl.encoding
import hashlib
import base64
import re
import time

