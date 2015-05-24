#!usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple phonebook module."""
import pickle


def dump():
    """For saving new contacts when added.
    Args: None
    Returns: None
    Examples:
        >>> Enter your choice (1-4) here: 1
        >>> Enter new contact name: sam
        >>> Enter contact child name: sammy
        >>> Enter contact phone number: 12345
        .... You have added a new contact!
    """
    phonebook = open('phonebook.txt', 'wb')
    pickle.dump(CONTACTS, phonebook)
    phonebook.close()


def load():
    """For loading past contacts.
    Args: None
    Returns: None
    Examples:
        >>> Enter your choice (1-4) here: 1
        ... JIM ('JIMMY', '88888')
        ... KIM ('KIMMY', '12335')
        ... SAM ('SAMMY', '12345')
        ... TIM ('TIMMY', '22222')
    """
    global CONTACTS
    try:
        phonebook = open('phonebook.txt', 'rb')
        CONTACTS = pickle.load(phonebook)
    except IOError, EOFError:
        CONTACTS = {}

load()

ANSWER = True
while ANSWER:
    print '-------Phonebook Menu-------''\n'
    print '1. Add a new contact name'
    print '2. Delete an existing contact'
    print '3. Search for an existing contact by name'
    print '4. Display all'
    print '5. Exit phonebook'
    ANSWER = raw_input('\nEnter your choice (1-4) here: ')
    print '---------------------------''\n'
    if ANSWER == '1':
        NAME = raw_input('\nEnter new contact name: ').upper()
        CHILD = raw_input('\nEnter contact child name: ').upper()
        PHONE = raw_input('\nEnter contact phone number: ')
        CONTACTS[NAME] = [CHILD, PHONE]
        print '---------------------------''\n'
        print 'You have added a new contact!''\n'
        dump()

    elif ANSWER == '2':
        REMOVE = raw_input('\nEnter the name you wish to delete: ')
        dump()
        if REMOVE in CONTACTS:
            del CONTACTS[REMOVE]
            print REMOVE.upper(), ':', 'Has been removed from the the phonebook'
            dump()
        else:
            print '---------------------------''\n'
            print REMOVE.upper(), ':', 'Does not exist in the phonebook!'
            dump()

    elif ANSWER == '3':
        SEARCH = raw_input('\nWho are you looking for? ')
        print '---------------------------''\n'
        if SEARCH in CONTACTS:
            print SEARCH, CONTACTS[SEARCH]
        else:
            print SEARCH.upper(), ':', 'Does not exist in the phonebook!'
    elif ANSWER == '4':
        print '---------------------------''\n'
        print CONTACTS

    elif ANSWER == '5':
        print 'Have a nice day!'
        break
    dump()
