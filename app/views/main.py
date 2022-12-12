from flask import Blueprint, render_template, request
from ..models import getLoginRequest, getRigistRequest

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('login.html')

@main.route('/regist')
def regist():
    return render_template('regist.html')

@main.route('/registuser')
def regist_user():
    user = request.args.get('user')
    password = request.args.get('password')
    if getRigistRequest(user, password):
        render_template('login.html')
    else:
        return '注册失败'

@main.route('/loginuser')
def login_user():
    user = request.args.get('user')
    password = request.args.get('password')
    return '登录成功' if getLoginRequest(user, password) else '登录失败'

