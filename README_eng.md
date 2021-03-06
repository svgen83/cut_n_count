# Сut_n_count

The program converts long Internet links into short (bitlinks), and also counts the number of transitions by bitlinks.

## How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

## Program settings

In order for the program to work correctly, create an .env file containing your Bitlink token in the program folder. Write it like this:

```
BITLY_TOKEN="number of token"
```

## How to run

The program runs from the command line. To run the program you first need to navigate to the folder containing the cut_n_count.py file using the cd command. After that, write to the command line:
```
python cut_n_count.py e-link
```
At the same time, if you enter a long e-link, for example, https://devman.org/encyclopedia/tutorial/tutorial_devman/, then the screen will display a short one: https://bit.ly/2TseRIR this link.

And if you enter bitlink, you get the number of clicks on this link.


## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
