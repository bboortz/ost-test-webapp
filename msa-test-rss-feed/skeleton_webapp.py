#!/usr/bin/env python

import sys
import os
import ssl
import time
from datetime import datetime
from urlparse import urljoin
from flask import Flask, __version__, request
from flask import jsonify, make_response
from werkzeug.contrib.atom import AtomFeed


context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('cert.pem', 'key.pem')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'


def make_external(url):
	return urljoin(request.url_root, url)


@app.route('/alive')
def alive():
        return jsonify( { 'alive': 'true' } )

@app.route('/api')
def api():
        return jsonify( { 'api': 'ost-test-rss-feed', 'api-version': '1.0', 'flask-version': __version__ } )

@app.route('/api/atom')
def api_atom():
	feed = AtomFeed('Recent Articles', feed_url=request.url, url=request.url_root)
#	articles = Article.query.order_by(Article.pub_date.desc()).limit(15).all()
#	for article in articles:
	feed.add("title %s" % datetime.utcnow(), unicode("text %s" % datetime.utcnow() ), content_type='html', author="author", url=make_external("url"), updated=datetime.utcnow(), published=datetime.utcnow())
	return feed.get_response()

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(error):
	print error
	return make_response(jsonify({'error': 'Unexpected Server Error'}), 500)



def main():
	# This allows us to use a plain HTTP callback
	os.environ['DEBUG'] = "1"

	app.secret_key = os.urandom(24)
	app.run(host='0.0.0.0', port=9092, ssl_context=context, threaded=True, debug=True)


if __name__ == '__main__':
	main()

