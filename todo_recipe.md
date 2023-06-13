<!-- User Story -->
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.


<!-- Function Signature -->
def todo_checker() :
    Check that the given string includes the substring #TODO

parameters: string

<!-- Return Value -->
Boolean

<!-- Side Effects -->
Exception if data type given is not a string

<!-- Examples -->
'' = error 'The string is empty, please try another string.'
1234 = error 'The argument isn't a string.'
'This string includes #TODO' = True
'This string doesnt' = False