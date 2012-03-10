def render_list(L):
    s = '<ul>'
    for x in L:
        s += '<li>{0}</li>'.format(str(x))
    s += '</ul>'
    return s

def render_list_oops(L):
    s = '<ul>'
    for x in L:
        s += '<li>{0}<li>'.format(str(x))
    s += '</ul>'
    return s
