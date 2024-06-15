# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

licenses = {
    "some-unique-license-key": {"activated": False}
}

@app.route('/activate', methods=['POST'])
def activate():
    license_key = request.json.get('license_key')
    if license_key in licenses:
        licenses[license_key]['activated'] = True
        return jsonify({"message": "License activated successfully"}), 200
    return jsonify({"message": "Invalid license key"}), 400

if __name__ == '__main__':
    app.run(debug=True)
