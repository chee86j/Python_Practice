# Write a function that when given a URL as a string, parses out 
# just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"   

# -------------------------------------------------------------------------------------
# -----Solution 1-----Split-----
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
#   1.  Split the url by "//" and get last element, which is the domain
#   2.  Split the domain by "www." and get last element, which is the domain name
#   3.  Finally split the domain name by "." and get first element, which is the domain name

# -------------------------------------------------------------------------------------
# -----Solution 2-----Regex & Group-----
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
#   1.  Re is the regex module used to search for a pattern in a string
#   2.  Here it looks for the domain name in the url string for parts like: 
#       http://, https://, www., www1., www2., etc.
#   3.  The domain name is then captured in a group named 'name' representing the domain name
#   4.  The group is then returned as the domain name

# -------------------------------------------------------------------------------------
# -----Solution 3-----Replace-----
def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]
#   1.  Remove common prefixes from the url like "www.", "https://", and "http://" from URL
#   2.  Find the idx of the first "." in the url and return the substring from the start to the idx
#   3.  Finally, return the domain name (the substring of the URL from the beginning to the first idx)