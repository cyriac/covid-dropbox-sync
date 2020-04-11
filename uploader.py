import dropbox
import os
import fire

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

  def upload(self, directory):
    upload_dataset(directory)

if __name__ == '__main__':
  fire.Fire(Covid)
