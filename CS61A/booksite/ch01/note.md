[iown@mq3 ch01]$ python3
Python 3.6.8 (default, Nov 16 2020, 16:55:22) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from urllib.request import urlopen
>>> shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
>>> 
>>> words = set(shakespeare.read().decode().split())
>>> 
>>> {w for w in words if len(w) == 6 and w[::-1] in words}
{'repaid', 'redder', 'drawer', 'diaper', 'reward'}
>>> 
>>> 

