    headlineAndAbstract = article['headline']['main'] + ". " + article['abstract']
            polarity = TextBlob(headlineAndAbstract).sentiment.polarity
            subjectivity = TextBlob(headlineAndAbstract).sentiment.subjectivity
            dict[article['headline']['main']] = {'x': polarity, 'y': subjectivity}