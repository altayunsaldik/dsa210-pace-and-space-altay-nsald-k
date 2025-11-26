DSA 210 Project Proposal: The "Pace and Space" Revolution: Analysis of Three-Point Shooting and Game Tempo in the NBA

Course: DSA 210 Introduction to Data Science
Term: 2025-2026 Fall Term
Student:Altay Ünsaldık 34079


---

1. Project Proposal

1.1. Motivation and Objectives

The modern NBA has undergone a significant strategic transformation, widely characterized as the "Pace and Space" era. This evolution is defined by an increased statics on offensive spacing ("Space") and huge rise in the volume of three-point shot attempts (3PA).

While the "Pace and Space" term is widely used, the statistical relationship between these two terms are not always noticed. "Pace" refers to the game's tempo, formally measured as the number of possessions a team uses per 48 minutes. This project aims to search the statistical relationship between the strategic shift towards three-point shooting and the resulting change in game tempo.

The primary objective is to quantify this relationship, moving beyond observation to provide a data-driven analysis of how the NBA's offensive philosophy has evolved.

1.2. Research Questions

This study will address these following core research questions:

1.  What is the longitudinal trend of league-average `Pace` and `3PA` from the 2000 to 2025 season?
2.  Is there a statistically significant relationship between a team's number of three-point attempts (`3PA`) and its `Pace`?
3.  To what extent can a team's `Pace` be explained by its shot selection? We will develop a multivariate linear regression model to quantify the impact of `3PA`, `2PA` (two-point attempts), and `FTA` (free-throw attempts) on the `Pace` variable.
4.  How does offensive efficiency mediate the relationship between Pace and team winning percentage?


2. Data and Acquisition Methodology

2.1. Data Source and Structure

The data is sourced from Basketball-Reference.com, a validated public domain for NBA statistics. The core of this analysis relies on constructing a balanced panel dataset spanning 25 seasons (2000-01 to 2024-25) and covering approximately 750 team-seasons (≈30 teams×25 seasons).

2.2. Panel Data Construction and Feature Engineering

This project employs a two-stage data acquisition and feature engineering strategy to construct the final analytical dataset.

Base Datasets (Raw Acquisition):

Team Per Game Stats: Essential for volume metrics: 3PA, 2PA, FTA.

Team Advanced Statistics: Essential for dependent and control variables: Pace, Winning Percentage.

Team Shooting Stats: Essential for efficiency metrics: 3P%, eFG%. (This formalizes the use of the "Couple More Datasets" into the core plan).

Data Enrichment and Feature Engineering:

Panel Key: Datasets will be rigorously merged using the composite key (Team and Year) to establish the panel structure necessary for fixed-effects modeling.

Calculated Feature: We will engineer the crucial strategic variable Three-Point Attempt Rate (3PAr= 
FGA
3PA
​	
 ) to normalize volume and more accurately represent a team's offensive philosophy.
These two datasets will be merged using `Team` and `Year` as composite keys, creating a single, enriched dataset for analysis.


2.3. Data Acquisition and Processing Plan

The data acquisition and preparation process will be executed in the following steps:

1.  Data Scraping:  Python's `pandas` library (specifically the `read_html()` function) will be used to scrape the "Per Game Stats" and "Advanced" tables for each NBA season from 2000-2001 to 2024-2025.

2.  Data Cleaning: The raw scraped data will be cleaned. This includes removing non-team rows (e.g., "League Average"), standardizing team names (e.g., removing asterisks), and converting statistical columns to the appropriate numeric data types.

3.  Data Merging (Enrichment): The cleaned "Per Game" and "Advanced" DataFrames will be merged into a single DataFrame on the `Team` and `Year` keys.

4.  Data Storage: The final, cleaned, and enriched dataset will be saved as a `.csv` file within this repository's `/data` directory to ensure reproducibility.


