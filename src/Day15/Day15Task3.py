p_spam = 0.10          # P(Spam)
p_ham = 0.90           # P(Ham)

p_free_given_spam = 0.90   # P(Free | Spam)
p_free_given_ham = 0.05    # P(Free | Ham)

p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)

p_spam_given_free = (p_free_given_spam * p_spam) / p_free

print("Probability the email is Spam given it contains 'Free':")
print(p_spam_given_free)
