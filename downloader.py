import requests
import fire
import os
from slugify import slugify
from tqdm import tqdm

class Covid(object):
    def download(self, path):
        url = "https://raw.githubusercontent.com/starschema/COVID-19-data/master/README.md"
        r = requests.get(url)
        content = filter(lambda line: 'starschema.covid' in line, str(r.content).split('\\n'))
        downloadables = []

        for line in content:
            line = line.strip()
            c = list(map(lambda x: x.strip(), filter(lambda i: len(i.strip()) > 0, line.split('|'))))
            url = c[-1].split('(')[-1].rstrip(')')
            downloadables.append({'url': url, 'title': c[0]})

        for d in tqdm(downloadables):
            self.download_file(d, path)


    @staticmethod
    def download_file(d, path="./"):
        fname = slugify(d['title'])
        r = requests.get(d['url'])
        try:
            os.makedirs(path)
        except FileExistsError:
            pass
        open('{}/{}.csv'.format(path, fname), 'wb').write(r.content)


if __name__ == '__main__':
  fire.Fire(Covid)
