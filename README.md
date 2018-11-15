**Rookie's guide to getting started**

**Installation and Setup**
<br>
**1. See what you've got.** You probably already have python installed on your computer, but it might not be python 3. Check your python version using `$ python --version`.
<br>
**2. Install python 3.** `$ brew install python`
<br>
**Note:** Even after I installed the latest version of python, `$ python --version` informed me that I was still running python 2.7.x. However, after doing some more investigation, `/usr/local/bin` said it contained python 2 *and* python 3. So what gives? I'm not sure, but it turns out you can run either version by calling `$ python2` or `$ python3`.
<br>
**3. Install a few dependencies.**
<br>
Python's equivalent to JavaScript's *npm* and Ruby's *bundle* is *pip*. `$ pip` should automatically point to the version of python you `brew install`ed, but to be on the safe side you can be specific by saying `$ pip3`
<br>
Installing spaCy, general Python NLP lib
<br>`pip3 install spacy`

Downloading the English dictionary model for spaCy
<br>`python3 -m spacy download en_core_web_lg`

Installing textacy, basically a useful add-on to spaCy
<br>`pip3 install textacy`
<br>
**4. Saving and running a script**
Python scripts end in a `.py` extension. To run a python script, you can use the terminal like so: `$ python3 path/to/script.py`.
