# -*- coding: utf-8 -*-
"""
    flaskext.stylus2css
    ~~~~~~~~~~~~~~~~~~~

    A small Flask extension that makes it easy to use Stylus for CSS
    with your Flask application.

    :copyright: (c) 2012 by Manuel Albarrán.
    :license: MIT, see LICENSE for more details.
"""

import os.path
import codecs

from stylus import Stylus


def _convert(compiler, src, dst):
    source = codecs.open(src, 'r', encoding='utf-8').read()
    output = compiler.compile(source)
    outfile = codecs.open(dst, 'w', encoding='utf-8')
    outfile.write(output)
    outfile.close()

    print 'compiled "%s" into "%s"' % (src, dst)

def stylus2css(app, css_folder='templates', stylus_folder='src/stylus', force=False):
    if not hasattr(app, 'static_url_path'):
        from warnings import warn
        warn(DeprecationWarning('static_path is called '
                                'static_url_path since Flask 0.7'),
                                stacklevel=2)
        static_url_path = app.static_path
    else:
        static_url_path = app.static_url_path

    _compiler = Stylus(paths=[stylus_folder])
    def _stylus2css(filepath):
        stylusfile = "%s/%s.styl" % (stylus_folder, filepath)
        filename = "%s/%s.css" % (css_folder, filepath)
        cssfile = "%s%s/%s" % (app.root_path, static_url_path, filename)

        if os.path.exists(stylusfile) and (force or \
           not os.path.exists(cssfile) or \
           os.path.getmtime(stylusfile) > os.path.getmtime(cssfile)):
            _convert(_compiler, stylusfile, cssfile)
            
        return app.send_static_file(filename)
        
    app.add_url_rule("%s/%s/<path:filepath>.css" %(static_url_path, css_folder), 'stylus2css', _stylus2css)