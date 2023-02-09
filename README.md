# election_analysis
Elections, python / python-interpreter / vs-code

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won. 
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software : Python 3.10.4, Visual Studio Code, 1.71.2

## Basic Summary Analysis
The analysis of the election show that:
- There were a total of (369,711) votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana Degette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham, who received (23.0%) of the vote and (85,213) number of votes.
  - Diana Degette, who received (73.8%) of the vote and (272,892) number of votes.
  - Raymon Anthony Doane, who received (3.1%) of the vote and (11,606) number of votes.
- The winner of the election was:
  - Candidate Diane Degette, who received (73.8%) of the vote and (272,892) number of votes.

## Challenge Overview
## Challenge Summary

### Deliverable #3
## 1. Overview of Election Audit: Explain the purpose of this election audit analysis.
- The purpose of this analysis was to assist the Colorado Board of Election commitee requested me to calculate the total amount of votes, create a list a candidates who recieved those votes, calculate both the total number of votes & percentage for each corresponding candidate and establish a winner, and finally determine whther or not the winner of that election was based on popular vote.  

## 2. Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
- How many votes were cast in this congressional election? 
~ Total vote count accumulated to 369,711 votes.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
~ County Votes Breakdown of my findings: (County Votes/Percentages)
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

- Which county had the largest number of votes? 
~ The county with the largest number of votes estimated to about 306,055 votes (82.8%) of all counties voted in the county of Denver.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
~ County Votes Breakdown of my findings: (Candidate Votes/Percentages)
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
~ The winner of the election was Diana DeGette, their winning vote count was 272,892, & their percentage of total votes averaged to about 73.8%.

## 3. Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
- In summary, a great business proposition that I recommend would be for the election commision to focus solely on maybe the specific cities within that county's jurisdiction. Allowing that winning candidate from each city within any jurisdicted county, to sprout there wings and be able to advertise their campaign in the correcty city within that county. Without specific informortion allowing us to run analysis off of, it would be harder to predict this long term analysis. Another recommendation that I would provide to potentially make this process run seamless next time, would be to run a few linear prediciton models to see maybe what the best "future analysis" is needed to be done. With a linear regression model, my best recommendation would be to try to aim and predict in which county's each selected candidate would be best to campaign within that model itself. A ML model would also help us predict the long term goal for each candidate and seeing how we would be able to campaign specific to where they are most "popular".
