from flask import Flask, request, render_template_string, send_from_directory
import os

app = Flask(__name__)
# 允许跨域（前端和后端分离时需要）
app.config['JSON_AS_ASCII'] = False

# 主页路由：返回前端页面的入口
@app.route('/')
def index():
    return send_from_directory('.', '101.html')

# 校验接口：处理前端的GET请求
@app.route('/check', methods=['GET'])
def check():
    # 获取前端传递的score和sign参数
    score = request.args.get('score', '')
    sign = request.args.get('sign', '')
    
    # 构造响应内容，包含规律提示
    response_text = f"""提交数据：score={score}，sign={sign}
【核心规律】sign = "zM" + Base64(score) + "=="
【通关关键】计算score=1000时的sign值，访问：success.html?sign=xxx"""
    
    return response_text, 200, {'Content-Type': 'text/plain; charset=utf-8'}

# 通关验证接口
@app.route('/success', methods=['GET'])
def success():
    sign = request.args.get('sign', '')
    # 验证正确的sign值（score=1000对应的sign）
    if sign == 'zMMTAwMA====':
        return send_from_directory('.', 'success.html')
    else:
        return "错误的sign值！", 400

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
