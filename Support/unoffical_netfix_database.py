import requests

def netflix_api(search_in):
    try:
        url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"
        querystring = {"q":"" + search_in + "-!1900,2018-!0,5-!0,10-!0-!Any-!Any-!Any-!gt100-!{downloadable}","t":"ns","cl":"46","st":"adv","ob":"Relevance","p":"1","sa":"and"}
    #querystring = {"q":"%s-!1900,2018-!0,5-!0,10-!0-!Any-!Any-!Any-!gt100-!{downloadable}" % (search_in),"t":"ns","cl":"all","st":"adv","ob":"Relevance","p":"1","sa":"and"}

        headers = {
            'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
            'x-rapidapi-key': "PASS KEY HERE"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        response.json()
    #pprint.pprint(response.json()['ITEMS'][0]['netflixid'])
        netflix_api_res = (response.json()['ITEMS'][0]['netflixid'])
        print(netflix_api_res)
        return netflix_api_res
    except IndexError:
        error_in = "0"
        return error_in