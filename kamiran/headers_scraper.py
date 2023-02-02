s = """accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
cache-control: max-age=0
content-length: 55
content-type: application/x-www-form-urlencoded
cookie: lang=russian; _ym_uid=1672332358849554041; _ym_d=1672332358; _ga=GA1.2.1304755773.1672332358; supportOnlineTalkID=TperF324DSzFavqzdVTIlhpa0au1GbZN; cartinn=0; cartpass=0; sortview=nameUP; _gid=GA1.2.1858715886.1673521387; _gat=1; _ym_isad=2
origin: https://www.oreht.ru
referer: https://www.oreht.ru/modules.php?name=orehtPriceLS&op=ShowInfo&code=415041
sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"""
print(*["'" + i.split(': ')[0] + "': '" + i.split(': ')[1] + "'," for i in s.split('\n')], sep='\n')
