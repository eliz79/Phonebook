Scenario [01]: [Entering a new Contact]
Given [that I have a new customer,]
And [need to enter new contact info in my phone book,]
When [I choose Option 1,]
Then [I will get a prompt asking me to enter the contact information,]
And [I will add first name, last name, the telephone, and child name.]


Scenario [02]: [Deleting a Contact]
Given [that my customer will no longer need my services,]
And [need to remove the contact info from my phone book,]
When [I choose Option 2,]
Then [I will get a prompt confirming if I want to remove the contact,]
And [I will enter 'Y' for Yes or 'N' for No.]


Scenario [03]: [Editing a current Contact]
Given [that my customer has changed their number]
And [I need to update the contact info in my phone book,]
When [I choose Option 3,]
Then [I will get a prompt asking me to enter the updated contact information]
And [I will add the telephone, and any additional child name, if warranted]


Scenario [04]: [Searching for an existing Contact]
Given [that I have to contact my existing customer]
#And [I need to enter new contact info in my phone book,]
When [I choose Option 4,]
Then [I will get a prompt asking me to enter the contact first name or letter]
And [my phone book will retrieve my contact.]
