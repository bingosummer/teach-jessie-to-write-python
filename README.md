# Teach Jessie to write Python

# How to run the Python script
1. SSH into a Linux VM (Ubuntu). Will share with you the credentials offline.
2. Install `requests` and `BeautifulSoup4` on Ubuntu.

  ```
  sudo apt-get -y install python-pip
  sudo pip install requests beautifulsoup4
  ```

3. Download [crawler.py](https://raw.githubusercontent.com/bingosummer/teach-jessie-to-write-python/master/crawler.py).
4. Run `python crawler.py http://en.people.cn/ China`.

  The script will output all the links in http://en.people.cn/ which contain the keyword `China`.
