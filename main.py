__author__ = 'supermacy'
import requests
from api_data import data_getter,parser,response
from flask.ext.restful import Resource
import HTMLParser

class api_class(Resource):
    def get(self):
       api()
       return str

class index(Resource):
    def get(self):
        return {"message":"hi","success":True}

def api():
    key="key=AIzaSyB-UAeifaI-VadElGpEFbrGxT3nI4T22yc"
    _url_="https://maps.googleapis.com/maps/api/distancematrix/json?"
    json_array=data_getter.get_data()
    for json in json_array:
        _origins_latitude=parser.get_pickup_latitude(json)
        _origins_longitude=parser.get_pickup_longitude(json)
        _destination_latitude=parser.get_drop_latitude(json)
        _destination_longitude=parser.get_drop_latitude(json)
        _origins_="origins="+str(_origins_latitude)+","+str(_origins_longitude)
        _destination="destinations="+str(_destination_latitude)+","+str(_destination_longitude)
        _parameter_=_origins_+"&"+_destination+"&"+key
        _url_final=_url_+_parameter_
        r=requests.get(_url_final)
        response_json=response.response_parser(r.text)
        dist=response.get_reponse_distance(response_json)
        time=response.get_response_time(response_json)
        dist_deviation=response.distance_deviation(json,dist)
        time_deviation=response.time_deviation(json,time)
        faulty=response.is_faulty(time_deviation,dist_deviation)
        engagement_id=parser.get_engagement_id(json)
        from models import insertion_db
        insertion_db.db.create_all()
        query= insertion_db.final_database(engagement_id,parser.get_metered_distance(json),time_deviation,dist_deviation,faulty)
        insertion_db.db.session.add(query)
        insertion_db.db.session.commit()



