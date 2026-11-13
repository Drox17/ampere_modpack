import urllib.request
import time

target_hash = '88e1d338ccd31c74d63d56661657f648b0dc70d2afc04ac5d93d9cb30e9123d1'
for i in range(15):
    try:
        url = f'https://drox17.github.io/ampere_modpack/index.toml?nocache={int(time.time())}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Cache-Control': 'no-cache'})
        live = urllib.request.urlopen(req).read().decode('utf-8')
        if target_hash in live:
            print('MATCH! GitHub Pages index.toml updated!')
            break
        else:
            print(f'Attempt {i+1}: waiting...')
    except Exception as e:
        print('Error:', e)
    time.sleep(5)
