from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_folder='static')

# 辛普森角色資料
characters = {
    'maggie': {
        'name': 'Maggie Simpson',
        'description': 'Maggie是辛普森家族中最安靜但最神秘的小嬰兒。別被她的奶嘴聲騙了，她可是多次拯救過家人的小英雄！儘管還不會說話，她的眼神裡卻充滿著智慧，彷彿早就看透一切。<br><br>她曾用奶嘴當武器「教訓」過一頭熊，你能想像嗎？',
        'image': 'images/maggie.jpg'
    },
    'lisa': {
        'name': 'Lisa Simpson',
        'description': 'Lisa是家中的天才少女，學霸中的學霸，卻又有一顆柔軟的藝術心。她熱愛薩克斯風，總能用音樂療癒大家。她對環保和社會公義的熱情，常讓她成為家中「理性」的聲音。<br><br>雖然她追求完美，但也曾因作弊而被內疚折磨，這樣的Lisa是不是更可愛呢？',
        'image': 'images/lisa.jpeg'
    },
    'homer': {
        'name': 'Homer Simpson',
        'description': 'Homer是這個家庭的「搞笑擔當」，也是甜甜圈的頭號粉絲。他的口頭禪「D"oh!」已成經典。他也許有點笨拙，偶爾鬧出笑話，但對家人的愛從未減少。<br><br>他曾在夢裡跟甜甜圈「對話」，甚至幻想它們是他最好的朋友！',
        'image': 'images/homer.jpg'
    },
    'bart': {
        'name': 'Bart Simpson',
        'description': 'Bart是個名副其實的小惡魔，專門捉弄老師和同學。他的滑板技術一流，經典台詞「吃我的短褲！」讓他成為每個調皮小孩的偶像。<br><br>他曾試圖用一個假蟑螂嚇壞整個學校，卻差點把自己嚇得跳起來！',
        'image': 'images/bart.jpeg'
    },
    'marge': {
        'name': 'Marge Simpson',
        'description': 'Marge是辛普森家的「定心丸」，她的藍色高髮型早已成為標誌。她總是用無限的愛和耐心，包容著家人的各種奇葩行為。雖然平時溫柔，但她也有自己的倔強時刻。<br><br>她曾參加過一場保齡球比賽，結果把球館砸得差點變成廢墟，實力不容小覷！',
        'image': 'images/marge.jpeg'
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livingroom')
def livingroom():
    return render_template('livingroom.html')

@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')  # 返回廚房頁面

@app.route('/character/<name>')
def character(name):
    character = characters.get(name)
    if character:
        return render_template('character.html', character=character)
    return "Character not found", 404

if __name__ == "__main__":
    app.run(debug=True)
