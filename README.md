# Sports Performance Analysis Framework

## Project Overview
An exploratory data analysis (EDA) project designed to quantify athletic performance across multi-tier competitions. This study evaluates win-loss ratios, performance deltas, and victory margins to identify key success factors in collegiate sports.

## Technical Stack
* Language: Python 3.x
* Libraries: 
    * Pandas (Data Manipulation and Analytics)
    * Matplotlib (Data Visualization and Plotting)
* Environment: IDLE / Local Interpreter
* Data Source: CSV (Structured Sports Statistics)

## Research and Data Cleaning
A critical phase of this project involved Data Integrity and Sanitization.
* Header Normalization: Implemented string stripping to resolve structural inconsistencies (hidden whitespaces) in the raw CSV headers.
* Feature Engineering: Derived a Win_Margin metric by calculating the delta between Score_For and Score_Against to identify dominant performances.

## Key Insights and Visualization
1. Performance Consistency: Analysis of cumulative win rates over time, visualized through trend lines.
2. Competition Variance: Comparative study of success rates in State vs. Inter-college tiers.
3. Margin Analysis: Automated identification of the highest-scoring matches and victory spreads.
4. Graphical Reporting: Leveraged Matplotlib to transform raw statistical data into interpretable visual trends.

## How to Run
1. Ensure required libraries are installed: pip install pandas matplotlib
2. Keep Sports_Analysis.py and Sports_Data.csv in the same directory.
3. Execute via IDLE or Terminal: python Sports_Analysis.py
