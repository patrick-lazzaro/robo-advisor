# robo-advisor

## PREREQUISITES

Anaconda 3.7+

Python 3.7+

Pip

## INSTALLATION

Fork this remote repository under your own control, then download your remote copy onto your local computer. 

Then navigate there from the command line:

```sh
cd ~/Desktop/robo-advisor
```

Use Anaconda to create and activate a virtual envirnoment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python = 3.8
conda activate stocks-env
```

From inside the virtual envirnoment, install package dependencies:

```sh
pip install -r requirements.txt
```

## SETUP

Go to https://www.alphavantage.co/ and follow the instructions on the website to get your free API key

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your API key:

```sh
ALPHAVANTAGE_API_KEY = "abc123"
```

## USAGE 

Run the game script:

```sh
python app/robo_advisor.py
```

Enter your preferred stock ticker, and enjoy your stock statistics and recommendation!