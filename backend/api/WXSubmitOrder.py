# -*- coding: utf-8 -*-
from utils.MemberService import MemberService
from flask import Blueprint, request, jsonify
import DataBaseFolder.Interface.UserBaseModify as U

route_WXSubmitOrder = Blueprint('WXSubmitOrder', __name__)