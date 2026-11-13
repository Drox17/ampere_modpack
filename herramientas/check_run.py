import urllib.request
import json

url = 'https://api.github.com/repos/Drox17/ampere_modpack/actions/runs/42730079695/jobs'
headers = {'User-Agent': 'Mozilla/5.0'}
try:
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for j in data.get('jobs', []):
            print(f"{j.get('name')}: status={j.get('status')}, conclusion={j.get('conclusion')}")
            if j.get('name') == 'deploy':
                for s in j.get('steps', []):
                    print(f"  Step {s.get('name')}: {s.get('status')} - {s.get('conclusion')}")
except Exception as e:
    print('Error:', e)
