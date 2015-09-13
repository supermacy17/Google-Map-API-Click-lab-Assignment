__author__ = 'supermacy'

import controllers
if __name__ == '__main__':
    controllers.application.debug=True
    controllers.application.run(host='0.0.0.0',port=8091)
