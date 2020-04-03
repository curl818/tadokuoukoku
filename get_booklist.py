import requests
import bs4

base_url = 'https://tadoking.com/user/booklist.php?usr_no='
tadoid = '0000'
separator = ', '
url = base_url + tadoid

while url is not None:

    res = requests.get(url, auth=('username', 'password'))

    soup = bs4.BeautifulSoup(res.text)
    for row in soup.select('table.tadoku tr'):
        tds = row.select('td')
        if len(tds) != 0:
            print(tds[0].string + separator + 
                  '"' + tds[1].string + '"' + separator +
                  tds[1].a.attrs['href'][-10:] + separator +
                  tds[2].string + separator + 
                  tds[3].string + separator + 
                  tds[4].string + separator + 
                  tds[5].string + separator + 
                  tds[6].string)

    pager = soup.select('div.pager')[0]
    url = None
    for anchor in pager.select('a'):
        if anchor.string == '次のページ':
            url = 'https://tadoking.com/user/' + anchor.attrs['href'][2:]
