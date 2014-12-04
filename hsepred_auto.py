import sys
from time import sleep
import mechanize

uri = "http://sunflower.kuicr.kyoto-u.ac.jp/~sjn/hse/webserver.html#"
count = 0
f = open('seq_leftover2.txt')
for line in f:
    count = count + 1
    seq = line.strip()

    request = mechanize.Request(uri)
    response = mechanize.urlopen(request)
    forms = mechanize.ParseResponse(response, backwards_compat=False)
    response.close()

    form = forms[0]

    form.set_value(["3"], name="select")
    form.set_value("james.lyons0@gmail.com", name="textfield")
    form.set_value(">test\n"+seq, name="textarea") # fasta data


    request2 = form.click()  # mechanize.Request object
    try:
        response2 = mechanize.urlopen(request2)
    except mechanize.HTTPError, response2:
        pass

    response2.read()  # body
    response2.close()

    print count,seq # show progress
    sleep(10*60) # wait 10 mins between requests
    
f.close()
