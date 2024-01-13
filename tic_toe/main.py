from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

game_state = [["", "", ""], ["", "", ""], ["", "", ""]]
current_player = 2

def update_player(current_player=current_player):
    if current_player == 1:
        current_player = 2
        return current_player
    else:
        current_player = 1
        return current_player

def check_win():
    # Check rows, columns, and diagonals for wins
    for i in range(3):
        if (game_state[i][0] == game_state[i][1] == game_state[i][2] != ""):
            return True  # Check rows
        if (game_state[0][i] == game_state[1][i] == game_state[2][i] != ""):
            return True  # Check columns
    if (game_state[0][0] == game_state[1][1] == game_state[2][2] != "" or
        game_state[0][2] == game_state[1][1] == game_state[2][0] != ""):
        return True  # Check diagonals

    # Check for tie
    if not any("" in row for row in game_state):
        return True

    return False  # No win or tie yet

@app.route('/')
def home():
    return render_template('home.html', game_state=game_state)

@app.route('/make_move', methods=['POST'])
def make_move():
    global current_player
    if request.method == 'POST':
        position = request.form.get('position')
        row, col = map(int, position.split('-'))
        if game_state[row][col] == "":
            game_state[row][col] = "X" if current_player == 1 else "O"
            update_player()
            if check_win():
                return f"{current_player} wins"
            else:
                return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
