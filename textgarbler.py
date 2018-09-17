import os, timing, requests, difflib, sys, urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = r"C:\Users\jeffb\Anaconda3\Scripts\chromedriver.exe"
options = Options()
options.add_argument('--headless')

def text_compare (start_text, end_text):
    ratio = difflib.SequenceMatcher(None, start_text, end_text).ratio()
    return ratio

def languageConverter(text, language):
    if language == 'en':
        return text
    elif language == 'es': ##spanish
        return (text.replace('%C3%A1','á').replace("%C3%A9",'é').replace('%C3%AD','í').replace('%C3%B3','ó')
            .replace('%C3%BA','ú').replace('%C3%B1','ñ').replace('%C3%BC','ü').replace('%C3%81','Á')
            .replace('%C3%89','É').replace('%C3%8D','Í').replace('%C3%93','Ó').replace('%C3%9A','Ú')
            .replace('%C2%A1','¡').replace('%C2%BF','¿'))
    # elif language == 'sv': ## swedish
    # elif language == 'sl': ## slovenian

def text_encoder (text, lang):
    text = urllib.parse.quote(text)
    cleantext = text.replace('.', '')
    return languageConverter(cleantext, lang)
    

def text_decoder (text):
    cleantext = text.replace('.', '')
    return urllib.parse.unquote(cleantext)


def translate_request (inputText, inLang, outLang): 
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.get('https://translate.google.com/#' + inLang + '/' + outLang + '/' + inputText) ## converts betweeen input language and output language

    translationResult = driver.find_element_by_id("result_box")
    driver.quit
    return translationResult.get_attribute('textContent')

# english -> spanish -> swedish -> slovenian -> english
def translation_garble(start_text):
    counter = 0
    start_text = text_encoder(start_text,'eng')
    print (start_text)

    foreignText = (translate_request(start_text,'eng', 'es'))
    # print (foreignText)
    # foreignText = text_encoder(foreignText, 'es')


    # nativeText = (translate_request(start_text, 'eng'))
    # print (nativeText)
    # nativeText = text_encoder(foreignText, 'eng')

    # print ('Your text was garbled ' + str(counter) + ' times:')
    # print(text_decoder(nativeText))

print ('Enter desired text:')
start_text = input()

counter = 0
languageList = ['eng', 'es', 'sv', 'sl', 'eng']
translation_garble(start_text)