from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initialize vote counts
votes = {'Candidate A': 0, 'Candidate B': 0, 'Candidate C': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    candidate = request.json['candidate']
    if candidate in votes:
        votes[candidate] += 1
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/votes')
def get_votes():
    return jsonify(votes)

if __name__ == '__main__':
    app.run(debug=True)
