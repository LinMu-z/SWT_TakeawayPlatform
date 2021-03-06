# -*- coding: utf-8 -*-
from flask import request

# 相关数据库调用
from DataBaseFolder.Interface import DishBaseModify as d
from DataBaseFolder.Interface.InterfaceHelper import *

route_dishList = Blueprint('dish-list', __name__)


@route_dishList.route("/", methods=['GET', 'POST'])
def index():
    '''
    菜品列表接口
    '''
    # 获取请求结果
    req = request.values

    # 解析参数
    pageNum = int(req['pageNum']) if ('pageNum' in req and req['pageNum']) else 1
    pageSize = int(req['pageSize'])

    # 从数据库拉取列表信息
    dishList = d.PyList()
    listNum = len(dishList)
    dishList = dishList[(pageNum - 1) * pageSize:pageNum * pageSize]

    # 数据为空时查询失败
    if listNum < 1 or pageNum > listNum:
        lic = {
            'code': 400,
            'message': '请求失败,检查当前页数或者联系后台检查数据库',
            'data': []
        }
        return jsonify(lic)

    # 数据有效时，创建响应体
    lic = {
        'code': 200,
        'message': '请求成功',
        'data': [],
        'total': listNum
    }

    # 加入菜品数据
    def bedict(dataList):
        for item in dataList:
            lic['data'].append(
                {
                    "dish_id": item.DishID,
                    "dish_name": item.DishName,
                    "dish_class": item.DishType
                }
            )
        return lic

    return jsonify(bedict(dishList))
