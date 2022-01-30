import requests
from telegram.ext import Updater,Filters,MessageHandler

TOKEN = '5210335225:AAE1N4pnPLpbL9-wpI25Jb3RPzXr9tI8hPA'

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "ae4bf73f25msh0dae51b2d199082p1100bajsncc96529f0bd0"
    }

def query_builder(text: str, fields : dict) -> str:
    query = "q="
    query += text.replace(" ","%20")
    if len(fields) >0:
        for key,value in fields.items():
            query += "&"
            query += key
            query += "="
            query += value

    return query

def get_translation(text : str, fields: dict):
    query = query_builder(text, fields)
    response = requests.request("POST", url, data = query, headers=headers)
    return response.json()['data']['translations'][0]['translatedText']

def translate(update, context):
    text = update.message.text
    fields = {"target" : "tr", "source": "en"}
    response = get_translation(text, fields)
    update.message.reply_text(response)
    


def main():
    update=Updater(TOKEN)
    update.dispatcher.add_handler(MessageHandler(Filters.text,translate))

    update.start_polling()
    update.idle()


if __name__== "__main__":
    main()