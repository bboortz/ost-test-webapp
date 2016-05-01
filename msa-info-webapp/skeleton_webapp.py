#!/usr/bin/env python

import sys
import os
import ssl
from datetime import datetime
from flask import Flask, __version__
from flask import jsonify, make_response, request
import json


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.pem', 'key.pem')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'


db ={}


@app.route('/alive')
def alive():
        return jsonify( { 'alive': 'true' } )

@app.route('/api')
def api():
        return jsonify( { 'api': 'ost-test-webapp', 'api-version': '1.0', 'flask-version': __version__ } )

@app.route('/api/info', methods=['GET'])
def api_get_info():
	#request.form['username']
	return jsonify( db )

@app.route('/api/info', methods=['POST'])
def api_post_info():
	content =  request.form['info'] 
	json1 = content.replace("'", "\"")
	dict = json.loads( json1 )
	db.update(dict)
	return make_response(jsonify({'status': 'success', 'id': 1234, 'date': datetime.utcnow()}), 201)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Unexpected Server Error'}), 500)



def main():
	# This allows us to use a plain HTTP callback
	os.environ['DEBUG'] = "1"

	app.secret_key = os.urandom(24)
	app.run(host='0.0.0.0', port=9091, ssl_context=context, threaded=True, debug=True)


if __name__ == '__main__':
	main()

