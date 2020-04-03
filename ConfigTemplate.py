# Use this as a guide for creating a file named "config.py" in your application root
# !!! DO NOT COMMIT A REAL CONFIG.PY TO GIT !!!

class config:
    # Remote db config
    aws_db = {'user': 'aws_user',
              'password': 'aws_pw',
              'database': 'aws_db',
              'host': 'aws_host',
              'port': 3306}

    # local db config
    local_db = {'user': 'user',
                'password': 'pass',
                'database': 'seniordesign',
                'host': 'localhost',
                'port': 1234}

    # any other settings that are needed (I copied this from another project, right now this means nothing)
    app_settings = {
        'host': '127.0.0.1',
        'port': 5000,
        'debug': True
    }
