
=============
The Phonebook
=============

Dictionaries play an important role in Python. Python ‘dict’ are mutable and can
contain any data type. Dictionaries consist of pairs (called items) of keys and
their corresponding values. The data may be structured and related with
meaningful keys which opens a huge realm of program capabilities.

Personas: Ramona – Day Care Services
====================================

Ramona is 47 years old. She runs her own day care center. The center 
provides caring services for children while their parents work or go 
to school. 

Details: 
--------

Ramona loves working with children. Her business is open weekdays 
from 6:30 AM until 6 PM. She likes teaching and caring for them.
She acquires satisfaction by making them feel at home while under
her care.

Goals:
------

Ramona wants to have a way that can help her have easy and quick
access to parent’s phone number by first names or even by using
the child’s name; when applicable. Many times she misplaces her
phonebook which can be a huge problem and isn’t able to contact
a parent. 

Problem Scenarios: How to contact a parent when warranted
=========================================================

Ramona constantly misplaces her phonebook. She acquires a long
time to find contacts in her phonebook because they are not easy
to locate.

Current Alternatives
--------------------

Ramona attempts to make her names bigger than the number to find
contacts better. This method works at times and she is able to keep
a track of customer contacts more efficiently. 

Value Proposition
-----------------

The purpose of creating a module is to allow Ramona to have access to
her contacts. The dictionary will be accessed quickly and easily by the
client’s first name. She will be able to enter the first letter and locate
her customer almost instantly.

User Stories
============

Ramona's Phonebook
------------------

As a day care facilitator, I want to be able to reach my clients easily
and quickly in time of need. I want to be able to search by a customer’s
first name, last name, or child’s client’s name. I want to access the
phonebook in order to contact a parent/client when warranted; for example
to let parents know of any upcoming trips or emergency visits to the
doctor’s office that arise while the child is under my care.

==================
Acceptance Stories
==================

Scenario 1: Entering a new contact
==================================
::

| Given that I have a new customer,
| And need to enter new contact info in my phone book,
| When I choose Option 1,
| Then I will get a prompt asking me to enter the contact information,
| And I will add first name, child name, and the telephone.

Scenario 2: Deleting an existing contact
========================================
::

| Given that my customer will no longer need my services,
| And need to remove the contact info from my phone book,
| When I choose Option 2,
| Then the contact will be deleted,
| And I get a statement saying my contact has been deleted.


Scenario 3: Displaying all contacts
=======================================
::

| Given that I want to view all contacts,
| And I need to see who is in my phone book,
| When I choose Option 4,
| Then I will get a prompt displaying all contact information,
| And I will be able to view all contact info, with any other additional info.



Scenario 4: Searching for an existing contact
=============================================

::

| Given that I have to contact my existing customer,
| And I need to enter new contact info in my phone book,
| When I choose Option 3,
| Then I will get a prompt asking me to enter the contact first name,
| And my phone book will retrieve my contact.
