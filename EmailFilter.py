import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# nltk stopwords
nltk.download('stopwords')
# nltk punkt
nltk.download('punkt')

# Function to check if email is spam or not
def spam_filter(mail):
    # Tokenize the email
    email_words = word_tokenize(mail)
    # Remove stopwords from email
    email_words = [word for word in email_words if word.lower() not in stopwords.words("english")]
    # Define list of spam words
    spam_words = ["money", "loan", "won", "free", "action required"]

    # Check if any of the spam words appear in the email
    for word in email_words:
        if word.lower() in spam_words:
            return True
    return False

# Testing spam filter
mail = "Your free $500 voucher is about to expire. Click the button below to claim now."

if spam_filter(mail):
    print("This email is spam")
else:
    print("This email is not spam")