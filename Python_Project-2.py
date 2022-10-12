#!/usr/bin/env python
# coding: utf-8

# # Day 2
# ## Project Name : Tip Calculator

# In[1]:


bill = float(input("Welcome to the Tip Calculator.\n'what was the total bill ? $"))
tip = int(input("What percentage tip would you like to give? 10,12 or 15? $"))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip/100
total_tip_amount = tip_as_percentage*bill
total_bill = bill+total_tip_amount
bill_per_person = total_bill/people
round(bill_per_person,2)
print("{:.2f}" . format(bill_per_person))

