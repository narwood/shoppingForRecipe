from textblob import TextBlob

text = "The Pen Proves Mighty for an Unlikely Trump Correspondent. The president relishes showing off the “beautiful” and “interesting” letters he receives from a man he once threatened with annihilation: North Korea’s leader, Kim Jong-un."

polarity = TextBlob(text).sentiment.polarity
subjectivity = TextBlob(text).sentiment.subjectivity

print("Polarity: " + str(polarity))
print("Subjectivity: " + str(subjectivity))

# code to be used for analyzing headlines
# for headline in :
#     polarity = TextBlob(headline).sentiment.polarity
#     subjectivity = TextBlob(headline).sentiment.subjectivity
#     print(headline + "/npolarity: " + str(polarity) + "/nsubjectivity: " + str(subjectivity)) 