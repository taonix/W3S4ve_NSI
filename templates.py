def header(css_file):
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="/static/css/global.css">
        <link rel="stylesheet" href="/static/css/""" + css_file + """.css">
        <title>Enquête</title>
    </head>
    <body>
    """


footer = """
    </body>
    </html>
    """