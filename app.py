from flask import Flask, jsonify
import logging
from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = '294b946d501d05d5620010e788d0bc608443f689077814987'
client = swagger.ApiClient(apiKey, apiUrl)
app = Flask(__name__)
app.debug = True 
app.logger.setLevel(logging.DEBUG)
del app.logger.handlers[:]

handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)
handler.formatter = logging.Formatter(
    fmt=u"%(asctime)s level=%(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
app.logger.addHandler(handler)

@app.route('/word-of-the-day/')
def word():
	w = WordsApi.WordsApi(client) 
	word = w.getWordOfTheDay()
	dic = {}
	dic['word'] = word.word 
	dic['definitions'] = [x.text for x in word.definitions]
	dic['examples'] = [x.text for x in word.examples]
	dic['note'] = word.note

	return jsonify(dic)
if __name__ == '__main__':
    app.run()