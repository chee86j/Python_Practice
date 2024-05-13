# DESCRIPTION:
# Complete the function/method so that it returns the url 
# with anything after the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

# -------------------------------------------------------------------------------------
# -----Solution 1-----Split Method-----
def remove_url_anchor(url):
    return url.split('#')[0]

# 1.  Split the url at the anchor using the split method
#     split('#')[0] returns the first part of the url before the anchor
#     at index 0.