from flask import Blueprint, jsonify
from DataBaseFolder.Models.RestaurantModels.RestaurantBase import Restaurant
from DataBaseFolder.DataBase import db
from .DishBaseModify import PyDirectlyAdd as DishAdd
from .OrderBaseModify import PyDirectlyAdd as OrderAdd

#restaurant=Blueprint('restaurant',__name__)
'''
@restaurant.route('/t')
def ServerTest():
    print('Connect Success')
    return jsonify('Test Success')

@restaurant.route('/add/<resname>/<resadd>')
def Add(resname, resadd):
    print(resname, resadd)
    resinfo = Restaurant(RestaurantName=resname,Address=resadd)
    db.session.add(resinfo)
    db.session.commit()
    return jsonify(resinfo.to_json())
'''

def PyAdd(resname, resadd):
    '''
    Add a new restaurant
    :param resname: restaurant name
    :param resadd: restaurant address
    :return: restaurant object
    '''
    print(resname, resadd)
    resinfo = Restaurant(RestaurantName=resname,Address=resadd)
    db.session.add(resinfo)
    db.session.commit()
    return resinfo
'''
@restaurant.route('/<resid>/adddish/<dishname>/<price>/<type>/<tag>/<picture>/<description>')
def AddDish(resid,dishname,price,type,tag='',picture='DefaultPath',description='None'):
    dishinfo = DishAdd(resid,dishname,price,type,tag,picture,description)
    return jsonify(dishinfo.to_json())
'''

def PyAddDish(resid,dishname,price,type,tag='',picture='DefaultPath',description='None'):
    '''
    Add new dish in this restaurant
    :param resid: restaurant id
    :param dishname: dish name
    :param price: dish price
    :param type: dish type
    :param tag: dish tag
    :param picture: dish picture
    :param description: dish description
    :return: dish object
    '''
    dishinfo = DishAdd(resid,dishname, price, type, tag, picture, description)
    return dishinfo

'''
@restaurant.route('/<resid>/addorder/<uid>/<remark>/<address>/<dishes>/<price>/<carriage>')
def AddOrder(resid, uid, remark, address, dishes, price, carriage):
    orderinfo=OrderAdd(resid,uid, remark, address, dishes, price, carriage)
    return jsonify(orderinfo.to_json())
'''

def PyAddOrder(resid,uid, remark, address, orders, price, carriage):
    '''
    Add new order in this restaurant
    :param resid: restaurant id
    :param uid: user id
    :param remark: user remark
    :param address: user address
    :param dishes: dishes
    :param price: order price
    :param carriage: order carriage
    :return: order object
    '''
    orderinfo=OrderAdd(resid,uid, remark, address, orders, price, carriage)
    return orderinfo

'''
@restaurant.route('/list')
def List():
    ress = Restaurant.query.all()
    print(ress)
    ress_output = []
    for res in ress:
        ress_output.append(res.to_json())
    return jsonify(ress_output)
'''

def PyList():
    '''
    :return: all restaurants list
    '''
    return Restaurant.query.all()

'''
@restaurant.route('/find/id/<resid>')
def Find_ID(resid):
    return jsonify(Restaurant.query.get(resid).to_json())
'''

def PyFind_ID(resid):
    '''
    Find a restaurant matched input restaurant id
    :param resid: restaurant id
    :return: restaurant object
    '''
    return Restaurant.query.get(resid)

'''
@restaurant.route('/find/name/<resname>')
def Find_Name(resname):
    return jsonify(Restaurant.query.filter_by(RestaurantName=resname).first().to_json())
'''

def PyFind_Name(resname):
    '''
    Find a restaurant matched input restaurant name
    :param resname: restaurant restaurant
    :return: restaurant object
    '''
    return Restaurant.query.filter_by(RestaurantName=resname).first()
