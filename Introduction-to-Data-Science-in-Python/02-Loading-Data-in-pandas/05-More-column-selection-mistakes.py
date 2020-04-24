'''

More column selection mistakes
Another junior detective is examining a DataFrame of Missing Puppy Reports. He's made some mistakes that cause the code to fail.

The pandas module has been loaded under the alias pd, and the DataFrame is called mpr.

Instructions 1/3
35 XP
Inspect the DataFrame mpr using info().

Instructions 2/3
35 XP
Correct the mistakes in the code so that it runs without errors.

Instructions 3/3
30 XP
Question
Why did this code generate an error?

name = mpr.Dog Name

Possible Answers
1.-We need to remove the space in Dog Name.
2.-If a column name has capital letters, then it needs to be in brackets and string notation.
3.-If a column name contains a space, then it needs to be in brackets and string notation.

Answer: 3
'''

# Use info() to inspect mpr
print(mpr.info())

# Use info() to inspect mpr
print(mpr.info())

# The following code contains one or more errors
# Correct the mistakes in the code so that it runs without errors

# Select column "Dog Name" from mpr
name = mpr['Dog Name']

# Select column "Missing?" from mpr
is_missing = mpr['Missing?']

# Display the columns
print(name)
print(is_missing)