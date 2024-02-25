from textblob import TextBlob

text = "I love pizza but I can't stand peppers"

polarity = TextBlob(text).sentiment.polarity
subjectivity = TextBlob(text).sentiment.subjectivity

print("Polarity: " + str(polarity))
print("Subjectivity: " + str(subjectivity))

# code to be used for analyzing headlines
# for headline in :
#     polarity = TextBlob(headline).sentiment.polarity
#     subjectivity = TextBlob(headline).sentiment.subjectivity
#     print(headline + "/npolarity: " + str(polarity) + "/nsubjectivity: " + str(subjectivity)) 