# flaskをインポートします
from flask import Flask, request, jsonify
from flask_cors import CORS

# Flaskアプリケーションのインスタンスを作成します
app = Flask(__name__)
# これによりすべてのルートでCORSが有効になります
CORS(app)

# ルートURLにアクセスがあった場合に実行される関数を定義します
@app.route('/')
def hello_world():
    return 'Hello, World!'

# /nightにアクセスがあった場合に実行される関数を定義します
@app.route('/night', methods=['GET'])
def hello_night_world():
    # GETメソッドで/nightにアクセスしてきたら、good nightと返答します
    if request.method == 'GET':
        return 'Good night!'
    else:
        return 'Method Not Allowed', 405

# # /night/<id>にアクセスがあった場合に実行される関数を定義します
# @app.route('/night/<id>', methods=['GET'])
# def good_night(id):
#     # GETメソッドで/night/idにアクセスしてきたら、idさん、「早く寝てね」と返答します
#     if request.method == 'GET':
#         return f'{id}さん、「早く寝てね」'
#     else:
#         return 'Method Not Allowed', 405

# # 簡単なユーザーデータベース（実際の実装ではセキュアな方法で保存する必要があります）
# users = {
#     'yagimasa': 'password123',
#     'lego': 'password456'
# }

# # '/login'エンドポイントを定義し、POSTメソッドのみを許可します
# @app.route('/login', methods=['POST'])
# def login():
#     # リクエストのJSONデータを取得します
#     data = request.json
    
#     # JSONデータから'username'を取得します。存在しない場合はNoneを返します
#     username = data.get('username')
    
#     # JSONデータから'password'を取得します。存在しない場合はNoneを返します
#     password = data.get('password')
    
#     # ユーザー名がusersディクショナリに存在し、かつパスワードが一致するか確認します
#     if username in users and users[username] == password:
#         # 認証成功の場合、歓迎メッセージを含むJSONレスポンスを返します
#         return jsonify({'message': f'ようこそ！{username}さん'})
#     else:
#         # 認証失敗の場合、エラーメッセージを含むJSONレスポンスと
#         # HTTP status code 401（Unauthorized）を返します
#         return jsonify({'message': '認証失敗'}), 401


# アプリケーションを実行します
if __name__ == 'main':
    # アプリケーションを指定されたURLで実行します
    app.run(host='127.0.0.1', port=5000)