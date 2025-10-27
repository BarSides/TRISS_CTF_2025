import hashlib
import os
import secrets
from flask import Flask
from flask import redirect, render_template, request, url_for
from flask import jsonify, session
from rules import RULES_DEFINITION

app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = os.environ.get('FLASK_SECRET_KEY', secrets.token_hex(24))

# Load the flag from an external file
with open('flag.txt', 'r') as f:
    CTF_FLAG = f.read().strip()

# Create a separate list of rules with Python check functions for the backend
RULES = {}
for i, rule in enumerate(RULES_DEFINITION):
    if not rule.get('active', True):
        continue
    rule_number = len(RULES) + 1
    rule_id = hashlib.md5(str(rule_number).encode()).hexdigest()
    RULES[rule_id] = {'id': rule_id, 'check': rule['check_py']}


@app.route('/')
def home():
    session.clear()
    return render_template('index.html')


@app.route('/login')
def login():
    username = session.get('username')
    is_new = request.args.get('newuser', type=str)
    return render_template('login.html', username=username, newuser=is_new)


@app.route('/register', methods=['GET'])
def register_get():
    username = session.get('username')
    if not username:
        return redirect(url_for('login', newuser='1'))
    return render_template('register.html', username=username)


@app.route('/login_attempt_post', methods=['POST'])
def login_attempt_post():
    """Handles the login form submission. Always returns user not found."""
    data = request.get_json()
    username = data.get('username')
    session['username'] = username
    return jsonify({
        "message": (f"Username '{username}' not found. "
                    "Please register a new account."),
        "redirect_url": url_for('register_get')
    })


@app.route('/register_attempt', methods=['POST'])
def register_attempt():
    data = request.get_json()
    if not data:
        return jsonify({"message": "Invalid request format."}), 400

    password = data.get('password', '')
    submitted_hashes = data.get('rules_satisfied', [])

    if len(submitted_hashes) != len(RULES):
        return jsonify({"message": (
            f"You need to satisfy {len(RULES) - len(submitted_hashes)} "
            "more rules!")})

    if not all([id in RULES.keys() for id in submitted_hashes]):
        return jsonify({"message": "Invalid submission!"})

    if hashlib.md5(
        f'{len(RULES)}'.encode()
    ).hexdigest() not in submitted_hashes:
        return jsonify({"message": "You didn't satisfy all the rules!"})

    satisfied_rules = [
        id for id in submitted_hashes if RULES[id]['check'](password)
    ]

    if len(satisfied_rules) != len(RULES):
        return jsonify(
            {"message": (f"Your password only satisfies {len(satisfied_rules)}"
                         f" of {len(RULES)} rules."
                         )}
            )

    session['authenticated'] = True
    return redirect(url_for('app_page'))


@app.route('/vault')
def app_page():
    if not session.get('authenticated'):
        return redirect(url_for('login'))

    username = session.get('username', '')
    return render_template('vault.html', username=username, flag=CTF_FLAG)
