# import os, timing, requests, difflib, sys, urllib
# from bs4 import BeautifulSoup
# from lxml import html
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# # chrome_path = r"C:\Users\jeffb\Anaconda3\Scripts\chromedriver.exe"

# # options = Options()
# # options.add_argument('--headless')
# # # options.add_argument('--disable-gpu')  # Last I checked this was necessary.

# # driver = webdriver.Chrome(chrome_path, chrome_options=options)



# def text_compare (input, output):
#     ratio = difflib.SequenceMatcher(None, input, output).ratio()
#     return ratio


# def spanishconverter(text):
#     return (text.replace('%C3%A1','á').replace("%C3%A9",'é').replace('%C3%AD','í').replace('%C3%B3','ó')
#             .replace('%C3%BA','ú').replace('%C3%B1','ñ').replace('%C3%BC','ü').replace('%C3%81','Á')
#             .replace('%C3%89','É').replace('%C3%8D','Í').replace('%C3%93','Ó').replace('%C3%9A','Ú')
#             .replace('%C2%A1','¡').replace('%C2%BF','¿'))

# def text_encoder (text):
#     text = urllib.parse.quote(text)
#     # text = text.replace('%C3%AD', 'í')
#     text = spanishconverter(text)
#     return text

# def text_decoder (text):
#     return urllib.parse.unquote(text)


# # def translation_garble(text, language):
#     # text_encoder(text)
#     # r = requests.get('https://translate.google.com/#auto/'+language+'/' + text)

#     # soup = BeautifulSoup(r.text, 'html.parser')
    
#     # test = soup.find('span', id='result_box')
#     # test2 = test.find_next_sibling()
#     # print (test)
#     # f_trans = text_encoder(f_trans)

#     # r = requests.get('https://translate.google.com/#auto/en/' + f_trans)
#     # soup = BeautifulSoup(r.text, 'html.parser')
#     # n_trans = soup.find('span', id_='result_box')

#     # text_encoder(n_trans)


# print (text_encoder('á__é__í__ó__ú__ñ__ü__¡__¿__Á__É__Í__Ó__Ú'))




# # print ('Enter desired text:')
# # start_text = input()

# # print ('Enter desired number of translation exchanges')
# # loopnumber = int(input())

# # print ('Enter desired foriegn language. Spanish: es')
# # f_lang = input()

# # translation_garble(start_text, f_lang)

# # translation_garble('hello', 'es')




# # r = requests.get('https://translate.google.com/#auto/es/hello')
# # tree = html.fromstring(r.content)
# # test = tree.xpath('//*[@id="result_box"]/span/text()')
# # print (test)



sampletext = 'test test test. test test. test test.'
print (len(sampletext))
periodcount = (sampletext[:-1].count('.'))

for i in range(periodcount):
    print ('span['+str(i)+']')