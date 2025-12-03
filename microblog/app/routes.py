from app import first_app

@first_app.route('/')
@first_app.route('/index')
def index():
    return "Hello , World!"