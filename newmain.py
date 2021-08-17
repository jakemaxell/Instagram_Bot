from instapy import InstaPy
import os

session = InstaPy(username = "**********", password = "**********")
session.login()
session.set_do_follow(enabled = True, percentage = 100)
#session.set_do_comment(enabled = True, percentage = 50)
#session.set_comments(["Nice!", "Looks good!", "Keep up the good work!"])
session.like_by_tags(["art", "sketchbook", "comicbookart", "JimLee"], amount = 1)
session.end()
