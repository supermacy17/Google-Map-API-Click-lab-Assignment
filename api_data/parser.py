__author__ = 'supermacy'
import json
def get_json(_array):
    json_data = json.loads(_array)
    return json_data

def get_pickup_longitude(json):
    return json['pickup_longitude']
def get_pickup_latitude(json):
    return json['pickup_latitude']

def get_drop_longitude(json):
    return json['drop_longitude']

def get_metered_time(json):
    return json['metered_time']

def get_metered_distance(json):
    return json['metered_distance']

def get_drop_latitude(json):
    return json['drop_latitude']

def get_pickup_latitude(json):
    return json['pickup_latitude']

def get_engagement_id(json):
    return json['engagement_id']

