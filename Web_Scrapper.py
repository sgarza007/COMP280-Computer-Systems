#Author: Saul Garza
#Synopsis: Python code that scrapes desired information from
#a website. In this project we wanted to scrape rank and job name
#of a website.

import re
import os

#getting URLs where jobs and ranks were located
os.system('lynx -dump -nolist http://www.careercast.com/jobs-rated/jobs-rated-report-2016-ranking-200-jobs '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-21-40 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-41-60 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-61-80 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-81-100 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-101-120 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-121-140 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-141-160 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-161-180 '
                '-dump -nolist http://www.careercast.com/content/2016-jobs-rated-report-181-200 '
                '> j.txt')

f = open('j.txt', errors='ignore')

lines = f.readlines()

#Deletes everything we don't need
while lines:
        line = lines[0]
        if '1. Data Scientist' not in line:
                del lines[0]
        else:
                break

jobs=[]
while True:
        jobs.append(lines[0])
        del lines[0]
        if '200. Newspaper Reporter' not in lines[0]:
                continue
        else:
                jobs.append(lines[0])
                break


#needed external source to find correct regular expression combo to match only what we seeked
jobs_and_ranks = []

for job in jobs:
        m = re.search(r'(\d+[.] ([A-Za-z]+..+))', job)#this regular exp searches for number. and letters until the end of the line
        if m:
                jobs_and_ranks.append(m.group(1))





#encountered issue where website had sentences like the ones below, ie meeting the criteria for the #job
bugged_phrases = ["40. Among the healthcare careers ranked here include Chiropractor," ,  "100. Such careers include Skincare Specialist, Electrician"]

#this removes those 2 sentences for our list
for j in jobs_and_ranks:
        if j == bugged_phrases[0]:
                jobs_and_ranks.remove(j)
        if j == bugged_phrases[1]:
                jobs_and_ranks.remove(j)
#this sorts the list of jobs alphabetically
alphabetic = []
for job in jobs_and_ranks:
        m = re.search(r'(\d+[.][ ]([A-Za-z]+..+))', job)
        if m:
                alphabetic.append((m.group(2), m.group(1)))
#if you want this to just display the name of job and sort it that way, delete m.group(1)

#testing code
print("List of jobs with respect to their ranks: ")
print( jobs_and_ranks)
alphabetic.sort()
print()
print("List of jobs in alphabetical order: ")
print(alphabetic)
