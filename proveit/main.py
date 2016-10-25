import sys
reload(sys)
sys.setdefaultencoding('utf8')

from app import app, db
from models import *
from api import *


if __name__ == '__main__':
    app.run(debug=True, port=8085)
