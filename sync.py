import requests
import fire
import os
import dropbox

from slugify import slugify
from tqdm import tqdm


class CovidUtil(object):
    @staticmethod
    def download_file(d, path="./"):
        fname = slugify(d['title'])
        r = requests.get(d['url'])
        try:
            os.makedirs(path)
        except FileExistsError:
            pass
        open('{}/{}.csv'.format(path, fname), 'wb').write(r.content)

    @staticmethod
    def upload_dataset(directory):

        token = os.environ['DROPBOX_TOKEN']
        dbx = dropbox.Dropbox(token)

        rootdir = directory

        for dir, dirs, files in os.walk(rootdir):
            for file in files:
                try:
                    file_path = os.path.join(dir, file)
                    dest_path = os.path.join('/COVID-19-DATASETS', file)
                    print('Uploading %s to %s' % (file_path, dest_path))
                    with open(file_path, 'rb') as f:
                        dbx.files_upload(f.read(), dest_path, mute=True)
                except Exception as err:
                    print("Failed to upload %s\n%s" % (file, err))


class Covid(object):
    @staticmethod
    def download(path):
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
            CovidUtil.download_file(d, path)

    @staticmethod
    def upload(directory):
        CovidUtil.upload_dataset(directory)

    def sync(self, directory):
        self.download(directory)
        self.upload(directory)

if __name__ == '__main__':
  fire.Fire(Covid)
