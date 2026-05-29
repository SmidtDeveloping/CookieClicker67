from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Game state (in production, use database)
game_state = {
    'cookies': 0,
    'clicks': 0,
    'cps': 1,  # cookies per second
    'multiplier': 1,
    'upgrades': {
        'grandma': 0,
        'robot': 0,
        'lucky_67': False,
        'golden_cookie': False,
    },
    'lucky_67_active': False,
    'lucky_67_multiplier': 1,
}

UPGRADE_COSTS = {
    'grandma': 15,
    'robot': 100,
    'lucky_67': 67,
    'golden_cookie': 500,
}

UPGRADE_VALUES = {
    'grandma': 1,
    'robot': 5,
    'lucky_67': 67,
    'golden_cookie': 67,
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/click', methods=['POST'])
def click():
    data = request.json

    # Check for 67 special click
    game_state['clicks'] += 1
    is_lucky_67 = (game_state['clicks'] % 67 == 0)

    # Calculate cookies earned
    base_cookies = 1 * game_state['multiplier']
    if is_lucky_67 and game_state['upgrades']['lucky_67']:
        base_cookies *= 67
        game_state['lucky_67_active'] = True

    game_state['cookies'] += base_cookies

    # Check if 67 cookies reached (unlock special power)
    lucky_67_unlocked = game_state['cookies'] >= 67 and not game_state['upgrades']['lucky_67']

    return jsonify({
        'cookies': game_state['cookies'],
        'clicks': game_state['clicks'],
        'lucky_67_unlocked': lucky_67_unlocked,
        'is_lucky_67': is_lucky_67,
        'cookies_earned': base_cookies,
    })


@app.route('/api/buy', methods=['POST'])
def buy_upgrade():
    data = request.json
    upgrade = data.get('upgrade')

    if upgrade not in UPGRADE_COSTS:
        return jsonify({'error': 'Invalid upgrade'}), 400

    cost = UPGRADE_COSTS[upgrade]

    if game_state['cookies'] < cost:
        return jsonify({'error': 'Not enough cookies'}), 400

    # Special case: Lucky 67 can only be bought once
    if upgrade == 'lucky_67' and game_state['upgrades']['lucky_67']:
        return jsonify({'error': 'Already unlocked'}), 400

    game_state['cookies'] -= cost

    if upgrade == 'lucky_67':
        game_state['upgrades']['lucky_67'] = True
        game_state['multiplier'] *= 1.5
    elif upgrade == 'golden_cookie':
        game_state['upgrades']['golden_cookie'] = True
        game_state['multiplier'] *= 1.3
    else:
        game_state['upgrades'][upgrade] += 1
        if upgrade == 'grandma':
            game_state['cps'] += UPGRADE_VALUES['grandma']
        elif upgrade == 'robot':
            game_state['cps'] += UPGRADE_VALUES['robot']

    return jsonify({
        'cookies': game_state['cookies'],
        'cps': game_state['cps'],
        'multiplier': game_state['multiplier'],
        'upgrades': game_state['upgrades'],
        'lucky_67_active': game_state['lucky_67_active'],
    })


@app.route('/api/state', methods=['GET'])
def get_state():
    return jsonify({
        'cookies': game_state['cookies'],
        'clicks': game_state['clicks'],
        'cps': game_state['cps'],
        'multiplier': game_state['multiplier'],
        'upgrades': game_state['upgrades'],
        'upgrade_costs': UPGRADE_COSTS,
        'lucky_67_active': game_state['lucky_67_active'],
    })


@app.route('/api/reset', methods=['POST'])
def reset_game():
    global game_state
    game_state = {
        'cookies': 0,
        'clicks': 0,
        'cps': 1,
        'multiplier': 1,
        'upgrades': {
            'grandma': 0,
            'robot': 0,
            'lucky_67': False,
            'golden_cookie': False,
        },
        'lucky_67_active': False,
        'lucky_67_multiplier': 1,
    }
    return jsonify({'status': 'reset'})


if __name__ == '__main__':
    app.run(debug=True)
