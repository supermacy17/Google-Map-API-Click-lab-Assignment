__author__ = 'supermacy'

from flask.ext.restful import Resource
from flask.ext.restful import Api
from flask import Flask


application=Flask(__name__)
api=Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:rahulsinha@localhost:3306/clicklabs'
application.config['SQLALCHEMY_ECHO'] = True




import main
api.add_resource(main.index,'/clicklabs/index')


api.add_resource(main.api_class,'/clicklabs/main')

