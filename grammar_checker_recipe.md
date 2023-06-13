<!-- User Story -->
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

<!-- Function Signature -->
def grammar_checker() :
    Check that the given string begins with capital letter and ends with .,!,?
parameters: string

<!-- Return Value -->
A string either 'Great grammar!' or 'Sorry, this string is missing capital letter/doesnt end with .,!,?'
<!-- Side Effects -->
Exception if data type given is not a string

<!-- Examples -->
'' = error 'The string is empty, please try another string.'
'This is a good string!' = 'Great grammar!'
'this string sucks' = Sorry, this string is missing capital letter and doesnt end with .,!,?'
'this string is average.' = 'Sorry, this string is missing a capital letter.'