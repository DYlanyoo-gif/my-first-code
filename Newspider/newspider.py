import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin 


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
}

def scrape_site_headlines(site_config):

    print(f"\n--- 正在抓取【{site_config['name']}】的新闻头条 ---")
    headlines_data = []
    try:
        
        response = requests.get(site_config['url'], headers=HEADERS, timeout=10)
        
        response.raise_for_status()
        


        soup = BeautifulSoup(response.text, 'html.parser')
        

        selected_elements = soup.select(site_config['selector'])

        if not selected_elements:
            print(f"在【{site_config['name']}】没有找到匹配选择器 '{site_config['selector']}' 的元素。")
            return []

        for element in selected_elements:
            title = element.get_text(strip=True) 
            link = None


            if element.name == 'a':  
                link = element.get('href')
            else:  
                parent_a_tag = element.find_parent('a')
                if parent_a_tag:
                    link = parent_a_tag.get('href')
            

            if link:
                link = urljoin(site_config['url'], link)

            if title: 
                headlines_data.append({'title': title, 'link': link})
        
        if not headlines_data:
            print(f"在【{site_config['name']}】找到了元素但未能提取有效标题和链接。")

    except requests.exceptions.Timeout:
        print(f"抓取【{site_config['name']}】超时。")
    except requests.exceptions.HTTPError as http_err:
        print(f"抓取【{site_config['name']}】时发生HTTP错误: {http_err} (状态码: {response.status_code})")
    except requests.exceptions.RequestException as req_err:
        print(f"抓取【{site_config['name']}】时发生网络请求错误: {req_err}")
    except Exception as e:
        print(f"处理【{site_config['name']}】时发生未知错误: {e}")
        
    return headlines_data

def main():

    sites_to_scrape = [
        {
            "name": "BBC 中文网",
            "url": "https://www.bbc.com/zhongwen/simp",
            "selector": "a.bbc-1b1lgpo" 
        },
        {
            "name": "百度-热搜榜",
            "url": "https://top.baidu.com/board?tab=realtime",

            "selector": "div.c-single-text-ellipsis" 
        },
        {
            "name": "环球网",
            "url": "https://www.huanqiu.com/",

            "selector": "p.listp > a" 
        },
        {
            "name": "联合早报",
            "url": "https://www.zaobao.com.sg/realtime?ref=sidebar-realtime-header",

            "selector": "h2.card-header" 
        },
    ]

    all_headlines_collected = [] 

    for site_config in sites_to_scrape:
        headlines = scrape_site_headlines(site_config)
        if headlines:
            for index, data in enumerate(headlines, 1):
                print(f"  {index}. {data['title']}")
                if data['link']:
                    print(f"     链接: {data['link']}")
            all_headlines_collected.extend(headlines) 
        else:
            print(f"未能从【{site_config['name']}】获取任何头条。")
    



if __name__ == "__main__":
    main()
