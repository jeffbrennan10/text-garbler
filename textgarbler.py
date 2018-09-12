import os, timing, requests, difflib, sys, urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = r"C:\Users\jeffb\Anaconda3\Scripts\chromedriver.exe"
options = Options()
options.add_argument('--headless')

def text_compare (start_text, end_text):
    ratio = difflib.SequenceMatcher(None, start_text, end_text).ratio()
    return ratio

def spanishconverter(text):
    return (text.replace('%C3%A1','á').replace("%C3%A9",'é').replace('%C3%AD','í').replace('%C3%B3','ó')
            .replace('%C3%BA','ú').replace('%C3%B1','ñ').replace('%C3%BC','ü').replace('%C3%81','Á')
            .replace('%C3%89','É').replace('%C3%8D','Í').replace('%C3%93','Ó').replace('%C3%9A','Ú')
            .replace('%C2%A1','¡').replace('%C2%BF','¿'))

def text_encoder (text, lang):
    text = urllib.parse.quote(text)
    cleantext = text.replace('.', '')
    if lang == 'es':
        return spanishconverter(cleantext)
    
    return cleantext

def text_decoder (text):
    cleantext = text.replace('.', '')
    return urllib.parse.unquote(cleantext)


def translate_request (text): 
    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.get('https://translate.google.com/#en/' + f_lang + '/' + start_text)
    try:
        return driver.find_element_by_xpath('//*[@id="result_box"]/span').text
    except:
        return driver.find_element_by_xpath('//*[@id="result_box"]/span/text()').text

def translation_garble(start_text, f_lang):

    counter = 0
    start_text = text_encoder(start_text,'eng')

    print (start_text)

    driver = webdriver.Chrome(chrome_path, chrome_options=options)
    driver.get('https://translate.google.com/#en/' + f_lang + '/' + start_text)
    foreignText = driver.find_element_by_xpath('//*[@id="result_box"]/span').text
    driver.quit()
    print (foreignText)

    foreignText = text_encoder(foreignText,'es')

    print (foreignText)

    # driver = webdriver.Chrome(chrome_path, chrome_options=options)
    # driver.get('https://translate.google.com/#'+ f_lang + '/en/' + foreignText)
    # nativeText = driver.find_element_by_xpath('//*[@id="result_box"]/span').text
    # driver.quit()
    # nativeText = text_encoder(nativeText,'eng')

    # print (nativeText)

    # for _ in range(loopnumber):
    #     driver = webdriver.Chrome(chrome_path, chrome_options=options)
    #     driver.get('https://translate.google.com/#en/' + f_lang + '/' + nativeText)
    #     foreignText = driver.find_element_by_xpath('//*[@id="result_box"]/span').text
        
    #     driver.quit()

    #     foreignText = text_encoder(foreignText,'es')

    #     print ('loop ftext' + foreignText)

    #     driver = webdriver.Chrome(chrome_path, chrome_options=options)
    #     driver.get('https://translate.google.com/#'+ f_lang + '/en/' + foreignText)
    #     nativeText = driver.find_element_by_xpath('//*[@id="result_box"]/span').text

    #     nativeText = text_encoder(nativeText,'eng')

    #     counter +=1
    #     print (counter)
    
    # print ('Text similarity:' + "{0:.2f}".format(text_compare(start_text, nativeText)))
    # print ('Your text was garbled ' + str(counter) + ' times:')
    # print(text_decoder(nativeText))

print ('Enter desired text:')
start_text = input()

print ('Enter desired number of translation exchanges')
loopnumber = int(input())

print ('Enter desired foriegn language. Spanish: es')
f_lang = input()

counter = 0
translation_garble(start_text, f_lang)
