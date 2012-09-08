flask-stylus2css
================

A small Flask extension that makes it easy to use Stylus with your Flask application.


## Installation

### Install with PIP

    pip install flask-stylus2css


## Usage

You can activate it by calling the `stylus2css` function with your Flask app as a parameter:

    from flaskext.stylus2css import stylus2css
    stylus2css(app, css_folder='css', stylus_folder='src/stylus')

This will intercept the request to `css_folder` and compile de file if is necesary using the files from `stylus_folder`.

When you deploy your app you might not want to accept the overhead of checking the modification time of your `.styl` and `.css` files on each request. A simple way to avoid this is wrapping the stylus2css call in an if statement:

    if app.debug:
        from flaskext.stylus2css import stylus2css
        stylus2css(app)
        
If you do this you’ll be responsible for rendering the `.styl` files into `.css` when you deploy in non-debug mode to your production server.