# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from DataBaseFolder.Interface import DishBaseModify as d

route_WXDishInfo = Blueprint('WXDishInfo', __name__)


@route_WXDishInfo.route("/", methods=["GET", "POST"])
def foodInfo():
    """
    特定餐品信息(finish)
    """
    # 预定义回复结构
    resp = {'statusCode': 200, 'message': '操作成功~', 'data': {}}

    # 解析请求参数
    req = eval(request.values['data'])
    dish_id = int(req['dish_id'])

    # 获取菜品信息
    dish_info = d.PyFind_ID(dish_id)
    if not dish_info:
        resp['statusCode'] = 400
        resp['message'] = "没有找到对应菜品"

        return jsonify(resp)

    # 返回信息：菜品名称，菜品图片，菜品价格，菜品销售量，菜品评分
    resp['data'] = {
        "dish_name": dish_info.DishName,  # 菜品名
        'dish_img': dish_info.Thumbnail,  # 菜品图片
        "dish_price": str(dish_info.Price),  # 菜品价格
        "dish_sold": dish_info.Sold,  # 菜品销量
        "dish_score": dish_info.Score  # 菜品评分

    }

    return jsonify(resp)
