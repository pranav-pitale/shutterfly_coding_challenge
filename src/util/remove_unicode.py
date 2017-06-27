import re


# removes unicode from data
def clean_unicodeing(unicoding):
    """Clean a unicodeing."""
    if not unicoding:
        return unicoding

    unicoding = re.sub("(\u2018|\u2019|\u201c|\u201d)", "'", unicoding)
    unicoding = re.sub("(\u2013)", "-", unicoding)

    return unicoding
