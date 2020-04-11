# covid-dropbox-sync
Sync covid datasets from [starschema github page](https://github.com/starschema/COVID-19-data) to your dropbox. 


# Usage

1. Create a [dropbox app](https://www.dropbox.com/developers/apps), and generate a token by clicking `Generate access token`
2. Set your environment variable `DROPBOX_TOKEN` with the token from the previous step.
3. Download datasets with `python sync.py <path_to_local_directory>`
4. Upload to dropbox with `python sync.py <path_to_local_directory>`
5. You could combine the above steps with `python sync.py sync <path_to_local_directory>`

You will see the app in your dropbox under `COVID-19-DATASETS`, either in your root directory or apps directory as per the permission granted to the dropbox app when you created it at Step #1.

**NOTE: Set the `sync.py sync` in your crontab to keep them synced properly**
