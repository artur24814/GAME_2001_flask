from flask import Flask, request
import random
import csv

app = Flask(__name__)


list_of_dice = ['3', '4', '6', '8', '10', '12', '20', '100']

HELLO_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello</title>
</head>
<body>
<h1>GEME 2001</h1>
<p1>hello player, let's start having fun</p1>
<form action="" method="POST">
    <input type="hidden" name="gemer_point" value="{}">
    <input type="hidden" name="komputer_point" value="{}">
    <input type="hidden" name="x1" value="{}">
    <input type="hidden" name="x2" value="{}">
    <input type="submit" value="GO">

</form>

</body>
</html>
"""

GEME_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>geme 2001</title>
</head>
<body>
<h1>GAME 2001</h1>
<p>gamer point : {gemer_point_w}</p>
<p>komputer point : {komputer_point_w}</p2><br>
<br>


<form action="" method="POST">
    <label>Choose type of dice
    <select name="geme_dice1"> 
        <option value="6">6</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="8">8</option>
        <option value="10">10</option>
        <option value="12">12</option>
        <option value="20">20</option>
        <option value="100">100</option>
    </select>
    </label>
    <label>Choose type of dice
    <select name="geme_dice2"> 
        <option value="6">6</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="8">8</option>
        <option value="10">10</option>
        <option value="12">12</option>
        <option value="20">20</option>
        <option value="100">100</option>
    </select>
    </label>
    <input type="submit" value="GAME">
    <input type="hidden" name="gemer_point" value="{gemer_point}">
    <input type="hidden" name="komputer_point" value="{komputer_point}">
</form>
<p>komputer choose Dice {x2}</p>
<p>komputer choose Dice {x1}</p>


<h1>Previous throw results</h2>
<p>gemer : {y}<p>
<p>computer : {x}<p><br>

</body>
</html>
"""
FINISH_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Finish</title>
</head>
<body>
<h1>finish of game</h1>
<p1>gamer point : {gemer_point}</p1>
<p2>komputer point : {komputer_point}</p2>
<a href="/scoreboard">scoreboard</a>

</body>
</html>
"""


@app.route("/", methods=['GET', 'POST'])
def geme():
    if request.method == 'POST':
        komputer_point = int(request.form.get("komputer_point"))
        gemer_point = int(request.form.get("gemer_point"))
        y1 = int(request.form["geme_dice1"])
        y2 = int(request.form["geme_dice2"])
        x1 = int(list_of_dice[random.randint(0, 7)])
        x2 = int(list_of_dice[random.randint(0, 7)])
        x = random.randint(1, x1) + random.randint(1, x2)
        if x == 7:
            komputer_point = komputer_point // 7
        elif x == 11:
            komputer_point = komputer_point * 11
        else:
            komputer_point += x
        y = random.randint(1, y1) + random.randint(1, y2)
        if y == 7:
            gemer_point = gemer_point // 7
        elif y == 11:
            gemer_point = gemer_point * 11
        else:
            gemer_point += y
        if komputer_point > 2001 or gemer_point > 2001:
            file = open("scoreboard.csv", "a")
            writer = csv.writer(file)
            writer.writerow((f"gemer = {gemer_point}", f"komputer = {komputer_point}"))
            file.close()
            return FINISH_HTML.format(gemer_point=gemer_point, komputer_point=komputer_point)

        return GEME_HTML.format(gemer_point=gemer_point, komputer_point=komputer_point, x1=x1, x2=x2, y=y, x=x,
                                gemer_point_w=gemer_point, komputer_point_w=komputer_point)
    else:
        return GEME_HTML.format(gemer_point=0, komputer_point=0, x1=6, x2=6, gemer_point_w=0, komputer_point_w=0, y=0,
                                x=0)



@app.route("/scoreboard")
def scoreboard():
    file = open("scoreboard.csv", "r")
    reader = csv.reader(file)
    result = list(reader)

    return f"scoreboard <br> {result}"

if __name__ == "__main__":
    app.run(debug=True)