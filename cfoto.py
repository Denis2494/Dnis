from upfoto import *
from datetime import datetime, timedelta
import time, random, sys, json, codecs, threading, asyncio, glob, re, string, os, six, ast, pytz, atexit, traceback,requests
pub = LINE('',appName='')
a = 'img.jpg'
try:pub.updateProfilePicture(a)
except:pub.updateProfilePicture(a)