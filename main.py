#webscaper using BeautifulSoup
def city_plumbing():
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import os
    baseurl = 'https://www.cityplumbing.co.uk'

    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    product_links = []

    #get the page

    for x in range(0,6):

        r = requests.get(f"https://www.cityplumbing.co.uk/Product/Heating/Boilers/Gas-Boilers/Gas-Combi-Boilers/c/1838005?q=%3Arelevance&page={x}&perPage=15")
        soup = BeautifulSoup(r.content, 'html.parser')

        product_list = soup.find_all('div', class_='prod_img')



        for item in product_list:
            for link in item.find_all('a', href=True):
                product_links.append(baseurl + link['href'])

    #test_link = "https://www.cityplumbing.co.uk/Vokera-Vision-25C-Combi-Boiler-20097278/p/529743"
    Product_final = []
    for link in product_links:
        r=requests.get(link, headers=header)

        soup = BeautifulSoup(r.content, 'html.parser')

        name=soup.find('h1', class_='tpProductTitle').text.strip()


        try:
            price =soup.find('span', class_='price_value').text.strip()
            price = price.replace('£','')
            price = price.replace(',','')
            price = price.replace(' ','')
            price = float(price)
        except:
            price = "Price not found"

        description1=soup.find('div', class_='summary-info').text.strip()
        description=description1.replace('Product Information\n\n', '')
        description=description.replace('More Info', '')

        product = {
            'name': name,
            'price': price,
            'description': description,

        }


        print("Saving : ", product)
        Product_final.append(product)
    df = pd.DataFrame(Product_final)
    df = df.replace(r'\n', ' ', regex=True)
    df.to_csv('boiler.csv', index=False)

    df_saved = pd.read_csv('boiler.csv')
    df_saved





city_plumbing()



