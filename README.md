Cowordle bot by Simon Valentino.

Just a fun webscraping project I thought would be cool to make.

The bot goes until it looses. You can customize the username and weather or not Cowordle is played on hard mode or not with the USERNAME and IS_HARD_MODE variables respectively. The defaults are "Simon101" for the username and the game is set to hard mode. The underlying bot that is playing is ELDROW. You can view the Eldrow bot website that is being scraped by commenting out the follwoing piece of code: options.add_argument("--headless").

Cowordle website: https://cowordle.org/
Bot (Eldrow) website: https://www.simn.me/eldrow/

Some issues. There are words that are some words that are guessable in Wordle, such as LEGGO, that are not guessable on Cowordle for whatever reason. A more common problem is is the S is green and the E and R are yellow in SERIA (the bots favorite starting word), it then guesses SHERO, which Cowordle does not accept. The only way to solve this would be to use a bot that only guesses words that are in the answer list rather than the guessable list. I don't know why Cowordle does not accept some words that are acceptable on the official NY Times Wordle.
