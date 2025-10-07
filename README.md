# Give Me The Lyrics

A python tool for scraping the lyrics of a song into a txt file. It uses searX for the search engine and genius/streetdirectory for lyrics.

## how to use?

Enter key words as if you where searching for a song on google, it usally works best when you use t he songs title. (Don't forget to install dependencies before use)

## Dependencies

This requires requests and beautifulsoup4 to be installed. You can do this via pip or installing from your OS's repo.

### Links to dependencies

[archlinux / python-beautifulsoup4](https://archlinux.org/packages/extra/any/python-beautifulsoup4/)

[archlinux / python-requests](https://archlinux.org/packages/extra/any/python-requests/)

### pip install command

Always remember to be careful before running a pip command

```pip install beautifulsoup4 requests```

You can also use the activate.bash file on linux to automatically create a venv and install via pip

```source activate.sh```

If you are on windows just double click the ```activate.bat``` file to automatically create a venv and install via pip

## Tests

This app uses the in built unit tests package, you can test the code by running the below code, you should get 17/17 if not create an issue (it takes me 32.6 seconds to run)

```python -m unittest tests/test_getLyrics.py```

## LICENCE

This project is under the MIT licence however the I claim no ownership of the lyrics used in the tests. AI was used for some of the test cases and the windows activation script

## To Do

- [ ] add GUI
- [x] allow mutiple sources
- [ ] setup mock http requests for local testing
- [ ] more formats for output i.e. JSON and csv
- [ ] collect meta data
- [ ] add get lyrics function as a pypi package
