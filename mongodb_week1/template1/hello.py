import bottle

# Route to the context page begin with /

@bottle.route("/")
def index():
    """
    Return the template page with name hello_world, the template page is in views directory
    """
    return bottle.template("hello_world",{'value' : "Hello World!"})


# Debug to true
bottle.debug(True)

# Run the server at 8000 port
bottle.run(host = 'localhost', port = 8000)
