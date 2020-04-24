'''

Narrowing the list of suspects
In Chapter 1, we found a list of people whose cars matched the description of the one that kidnapped Bayes:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We'd like to narrow this list down, so we obtained credit card records for each suspect. We'd like to know if any of them recently purchased dog treats to use in the kidnapping. If they did, they would have visited 'Pet Paradise'.

The credit records have been loaded into a DataFrame called credit_records.

Instructions 1/2
50 XP
Select rows of credit_records such that the column location is equal to 'Pet Paradise'.

Instructions 2/2
50 XP
2
Question
Which suspects purchased pet supplies before the kidnapping?

Possible Answers
1.-Fred Frequentist and Ronald Aylmer Fisher
2.-Gertrude Cox and Kirstine Smith
3.-Fred Frequentist and Gertrude Cox
4.-Ronald Aylmer Fisher and Kirstine Smith


Answer: 3
'''

# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)