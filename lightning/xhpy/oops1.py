from xhpy.init import register_xhpy_module
register_xhpy_module('ui')
register_xhpy_module('view')
import view
view.render_list([
    "<script>alert('welcome to the jungle')</script>"
])
