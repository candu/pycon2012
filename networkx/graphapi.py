import fbconsole

def init(perms = []):
    fbconsole.AUTH_SCOPE = list(perms)
    fbconsole.authenticate()

def fetch(url):
    result = fbconsole.get(url)
    if 'paging' in result:
        return list(fbconsole.iter_pages(result))
    if 'data' in result:
        return result['data']
    return result

def pull(L, k):
    return map(lambda x: x[k], L)
