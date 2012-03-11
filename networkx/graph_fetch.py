import fbconsole
import sys

fbconsole.AUTH_SCOPE = ['friends_about_me', 'friends_likes']
fbconsole.authenticate()
for url in sys.argv[1:]:
    print list(fbconsole.iter_pages(fbconsole.get(url)))
