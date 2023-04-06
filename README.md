# Qanalysis
Discord Bot for sentiment analysis using Python
This project is a Discord bot created using Python that performs sentiment analysis on messages posted in a Discord server within the last 10 days. The bot uses the TextBlob library for sentiment analysis. The command !sentiment can only be activated by an admin. The bot will exclude messages sent by role ID when analyzing all channels in the server. When the !sentiment command is triggered, the bot will display the message "I'm calculating the average of the past 10 days". After the calculation is complete, the bot will display the average sentiment with the message "The average sentiment of the last 10 days on the server is".

In TextBlob, polarity is a measure of how positive or negative a given text is. It is a float number between -1.0 and 1.0 where -1.0 is extremely negative and 1.0 is extremely positive.

Subjectivity, on the other hand, is a measure of how much the text is expressing a personal opinion or a factual information. It is also a float number between 0.0 and 1.0, where 0.0 is very objective and 1.0 is very subjective.

To edit the bot you just need to change the role ID for you Admin and the roles you want to whitelist from the sentiment analysis, and the Token App. 
