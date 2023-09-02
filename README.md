Wordle bot and Cowordle automation by Simon Valentino.

# What It Does

This project has a wordle bot in the wordle_bot.py file as well as a webdriver in the cowordle_driver.py file that uses the bot to automate Cowordle games because I was lazy and winning was way to hard. It's much more enjoyable to watch my opponents struggle while I sit back and win without lifting a finger.

# The Wordle Bot

When coding this bot I realized how many ways there are to go about making a wordle bot. I will explain my approach, but remember, this is by no stretch of imagination the only one.

### Which Words It Can Guess

My wordle bot defaults to only guessing and calculating based off answer list words. The answer list and guess list (including answers too) are in answer_list.txt and guess_list.txt files respectively. You can change the words for the bot at will, and I highly encourage it. The bot will only make guesses from these words, and it will treat all of them as possible answers. It is a keyword arg in the Bot class's constructor that defaults to wordle's answer list. Try changing this to the guess list and see what happens. You can get the answer and guess list in python list form from the word_reservoir.py file.

As you may or may not know, but the wordle ANSWER list (2,315 words) and the wordle GUESS list (12,972 words) are two different things. So, when making the bot, I had to decide both which words it would guess, and which words it would use to calculate the guesses. I originally wanted it to be able to guess all words but only calculate with the answer list words, but it was hard to make sure it wouldn't only guess guess list words and not enough answer list words. You may get a lot of information, but the odds of guessing the correct word on a guess becomes lower when you use a guess list word. Finding this balance is one of the really important keys to a great wordle bot, so hats off to anyone that can figure that out.

### The Bot's Algorithm

The bot essentially checks every word with every other word and finds which one will end up with the smallest average number of guesses needed after is makes that word guess. It can also be made so that it selects which ever word has the best worst case scenario: the smallest most number of guesses that could be needed. Because it goes through all the words on the first loop, I HIGHLY recommend passing a starting word in the keyword args parameter. It will be slow at first if you do not. To save you some time, the best starting word according to the bot from the answer list is "trace" and the best starting word from the guess list is "tares". 

# Where this project started

Originally, this project would just automate Cowordle games and get the answers from the website Eldrow (a very smart wordle bot). This code is still preserved in the cowordle_eldrow_bot.py file. While this was cool, and definitely very fun to mess around with, it had some problems. The bot would guess words like "ormer" or "globi" which are not in the answer list, which results in debatably worse performance. Additionally, it would rarely guess a word that would not even be accepted by Cowordle, which completely broke the game. This approach was also messy as two webdrivers had to be managed at once.

I was having enough fun with this project and thought it would be really cool to design my own wordle bot, so I did.

