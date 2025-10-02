# Give Me The Lyrics

A python tool for scraping the lyrics of a song into a txt file. It uses searX for the search engine and genius for lyrics.

## how to use?

Simply enter key words as if you where searching for a song on google, this can be things like the songs name, author and quotes from it. (Don't forget to install dependencies before use)

## Dependencies

This requires requests and beautifulsoup4 to be installed. You can do this via pip or installing from your OS's repo.

### Links to dependencies

https://archlinux.org/packages/extra/any/python-beautifulsoup4/
https://archlinux.org/packages/extra/any/python-requests/

### pip install command

Always remember to be careful before running a pip command

```pip install beautifulsoup4 requests```

You can also use the activate.bash file on linux to automatically create a venv and install via pip

```source activate.bash```

If you are on windows just double click the ```activate.bat``` file to automatically create a venv and install via pip

## Tests

This app uses the in built unit tests package, you can test the code by running the below code and setting ```testing``` to ```True```

```python -m unittest tests/test_getLyrics.py```

## LICENCE

This project is under the MIT licence however the I claim no ownership of the lyrics used in the tests. AI was used for some of the test cases and the windows activation script
