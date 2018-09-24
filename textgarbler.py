import os, timing, requests, difflib, sys, urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = r"C:\Users\jeffb\Anaconda3\Scripts\chromedriver.exe"
options = Options()
options.add_argument('--headless')

def text_compare (start_text, end_text):
    ratio = difflib.SequenceMatcher(None, start_text, end_text).ratio()
    return ratio

def text_encoder (text):
    return (text.replace(' ','%20').replace(',','%2C').replace('@','%40').replace('#','%23')
    .replace('$','%24').replace('^','%5E').replace('&','%26').replace('.','')
    .replace('=','%3D').replace('+','%2B').replace(':','%3A').replace(';','%3B').replace('?','%3F'))
    

def text_decoder (text):
    cleantext = text.replace('.', '')
    return urllib.parse.unquote(cleantext)


def translate_request (inputText, inLang, outLang): 
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.get('https://translate.google.com/#' + inLang + '/' + outLang + '/' + inputText) ## converts betweeen input language and output language
    translationResult = driver.find_element_by_id("result_box")
 
    driver.quit()
    return translationResult.get_attribute('textContent')

# english -> spanish -> swedish -> slovenian -> english
def translation_garble(start_text):
    languageList = ['eng', 'es', 'sv', 'sl', 'eng']
    langpointer = 0
    start = text_encoder(start_text)
    print (start)

    foreign_start = translate_request(start, languageList[langpointer], languageList[langpointer+1])
    print (foreign_start)
    langpointer += 1
    print (langpointer)
    # for _ in range(len(languageList)-2):
    #     foreign_start = text_encoder(foreign_start)
    #     foreign_start = (translate_request(foreign_start, languageList[langpointer], languageList[langpointer+1]))
        
    #     langpointer += 1
    # print ('Your text was garbled through' + str(langpointer) + ' languages:')
    # print (foreign_start)

    textComparison  = text_compare(start, foreign_start)
    print ('Difference between initial and garbled text: ' + str(textComparison))


print ('Enter desired text:')
start_text = str(input())

translation_garble(start_text)
