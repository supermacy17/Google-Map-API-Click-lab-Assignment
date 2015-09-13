__author__ = 'supermacy'
import json as j
import parser
timequanta=10
distancequanta=10

def response_parser(json):
    res_json =j.loads(json)
    return res_json


def get_reponse_distance(json):
    dist= json['rows'][0]['elements'][0]['distance']['value'];
    return dist



def distance_deviation(json,dist):
    distance=parser.get_metered_distance(json)*1000000
    standard_dist=dist-distance
    if distance != 0:
        standard_dist=abs(standard_dist)/distance*100
    return standard_dist

def get_response_time(json):
    dist= json['rows'][0]['elements'][0]['duration']['value'];
    return dist


def time_deviation(json,r_time):
    time=parser.get_metered_time(json)*60
    standard_time=r_time-time
    if standard_time!=0:
        standard_time=abs(standard_time)/time*100
    return standard_time

def is_faulty(t_deviation,d_deviation):
    if t_deviation>timequanta:
        return 0
    if d_deviation >distancequanta:
        return 0
    return 1

