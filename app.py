from flask import Flask, render_template, request
from utils import check_ban
import uvicorn

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
async def check():
    uid = request.form['uid']
    ban_status = await check_ban(uid)
    return render_template('result.html', ban_status=ban_status, uid=uid)

@app.route('/unban', methods=['POST'])
async def unban():
    uid = request.form['uid']
    return render_template('unban_result.html', uid=uid)

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=10000, reload=True)
