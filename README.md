Wordle bot and Cowordle automation by Simon Valentino.

# What It Does

This project has a wordle bot in the wordle_bot.py file as well as a webdriver in the cowordle_driver.py file that uses the bot to automate Cowordle games because I was lazy and winning was way to hard. It's much more enjoyable to watch my opponents struggle while I sit back and win without lifting a finger. The bot goes until it draws or looses.

# How to Use the Wordle Bot

## Initializing the Bot

To create a Wordle bot object you must import the Bot class from wordle_bot.py. The Bot class has two optional parameters in its constructor, the word list it will use, and a list of starting words. If no word list is given it will make guesses from Wordle's official answer list. Also know that the Cowordle answer list and Wordle answer list are slightly different, with the Cowordle answer list having words like "april", so be sure to use that list for Cowordle. This list is still evolving, I just add to it when the bot can't guess the Cowordle word. All the lists can be found in their respective txt files and allocated in list form from the word_reservoir.py module. If no starting words are given it will calculate it's own starting word based on the word list that was given. I recommend leaving the word list parameter to its default because that will make the bot guess the word fastest. I also recommend giving the Wordle bot a starting word because if you do not than it will take a couple seconds to calculate the starting word itself, and those seconds can be crucial for the Cowordle webdriver. You should only pass multiple starting words if you are not playing on hard mode because the second word might not be valid after the hints of the first word. See "Starting Words Analysis" section for info on what words to start with.

## The Bot's Functions

The calculate_guess functions will return a str that is the guess the Wordle bot is making based off all the previously absorbed hints. This guess will be a starting word if the guess number is less than the length of the starting words guess list.

After a guess is made the bot's evaluate_word function will take in the guess and an answer and return at tuple of ints from 0 to 2, 2 meaning green, 1 meaning yellow, and 0 meaning grey. The order of these ints will correspond to the order of the letters in the guess.

The bot's absorb_hints function can be thought of as the bot learning from hints which are tuples of length 5 as explained before. This function doe not return anything, it just gets the bot ready for the next calculate_guess call.

The reset function resets all the learning that the bot had done, putting it in the same state as when it was first initialized. The words it knows and the starting words list stay the same.

# Cowordle automation

The bot has to use the Cowordle answer list because it is slightly different from the Wordle one. Using the normal answer list will cause errors.

## Cowordle Driver

The cowordle_driver.py module uses the bot and automates the popular website Cowordle where you race against someone to see who can solve the Wordle the fastest. You can customize the username and weather it is hard mode or not. My bot does not have a normal or hard mode distinction, but if you give it multiple starting words than you can force it to start out on normal mode. Just make sure if you do that you set IS_HARD_MODE to false.

## Cowordle Eldrow Driver

This webdriver does not involve any of my own Wordle bot, it solely gets words to guess from the website Eldrow, another Wordle bot online. This bot does have a hard mode and normal mode distinction. 

## Which is better?

Overall, I think my Wordle bot is faster because the Eldrow bot guesses words that are not in the answer list but still in the guess list. I haven't formally tested which is technically best but from experience it seems to me that mine is better. Also, using my bot allows words to be entered into Cowordle faster because extra time does have to be wasted waiting for the word to come up onto the Eldrow website. In terms of winning on Cowordle, mine definitely wins faster. Try out both and see for yourself.

# Starting Words Analysis

All the starting word data was done by my bot using the official Wordle answer list as possible answers and guesses (besides the first guess) and the entire guess lists as possible first guesses.

## On Starting Word

After 8 days of 100% CPU usage and the power of multithreading I was able to test every single guessable word with all of the answer list words, take the average number of guesses each starting word needed to win, and put the data into a csv file called starting_word_data.csv. Feel free to check how your favorite starting word sizes up with the others. The best starting word for my bot is "salet".

## Multiple Starting Words

For using multiple starting words on normal mode I know doing the "stare" "cloud" "pinky" strategy is very common, but the bot actually likes "salet" "round" "chick" "pygmy" the best.