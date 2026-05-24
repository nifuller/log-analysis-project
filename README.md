# log-analysis-project

## 📈 Progress
- [x] Downloaded and explored NASA HTTP dataset
- [x] Built log parser in Python
- [x] Load data into SQLite
- [x] Write security focused SQL queries
- [x] Build visualizations
- [x] Write up findings

## 🛠️ Tools & Technologies
`Python` `Pandas` `SQLite` `Matplotlib` `Regex` `Jupyter Notebook`

# Project Overview
Analyzed over 1.8 million HTTP requests from NASA's Kennedy Space Center web server using the July 1995 dataset. The raw dataset required a custom regex parser to extract structured fields from an unformatted log file before any analysis could begin. The main tools used in this project were Python, Pandas, SQLite, and Matplotlib with the goal of identifying anomalous traffic patterns and investigating potential security threats. Specifically looking for any unusual overnight activity spikes, error rates, and suspicious endpoint access. Each anomalous traffic pattern was thoroughly investigated using the full analyst workflow of detection, investigation, and false positive reduction.

# Data Processing
The raw NASA log file was not a standard CSV file. Each unstructured line contained the IP address, timestamp, HTTP request, status code, and byte size as a single string. A custom regex parser script was written in Python to clean any malformed strings and to structure the data by extracting each field line by line. Then it was loaded into both a Pandas dataframe and a SQLite database for analysis and querying. 


# Key Findings

## Overnight traffic anomaly
   
Analysis of overnight traffic between 12:00 am and 05:00 am, revealed several hosts that were exclusively active outside normal business hours. The top hosts made between 140 and 261 requests during this window with zero business hour activity. Upon further investigation the majority of these hosts were legitimate originating from both Japanese academic and government domains including NASDA, the Japanese space agency whose daytime hours align with NASA's nighttime hours. Several other hosts were identified as web crawlers systematically mirroring NASA shuttle mission content. 

## 404 error analysis

Analysis of HTTP status codes revealed that the overall health of the server was stable with 1,701,534 successful 200 responses out of 1.9 million total requests. However, 10,845 404 errors were identified and investigated further. Upon investigating the top offending hosts, it was found that these were legitimate and just hitting either broken or outdated links rather than scanning the server. One host that stood out was a US Naval Undersea Warfare Center IP which was initially flagged for suspicious scanning. Upon further investigation it was revealed that it was requesting legitimate NASA public pages, consistent with normal browsing behavior. 

## CGI endpoint probing

The most suspicious activity identified within the dataset originated from the IP address 163.205.1.45. It made 89 different requests to /cgi-bin/geturlstats.pl which included 21 POSTs. The combination of repeated GET and POST requests to the same CGI endpoint initially indicated potential automated probing. However upon further investigation the IP address was requesting standard NASA public images and pages, consistent with normal browsing behavior. This finding highlights the importance of deeper investigation before concluding malicious intent.  

# Conclusion

Throughout the investigation, several anomalies were flagged as potentially suspicious. This included overnight traffic spikes, high 404 error rates, and CGI endpoint access. Upon further investigation each anomaly was resolved as benign demonstrating the critical role of contextual analysis in reducing false positives. This project reflects the full analyst workflow of a SOC environment: detection, investigation, and resolution. The ability to distinguish between genuinely malicious activity and legitimate but unusual behavior is one of the most valuable skills in security operations.  

# Visualizations

<img width="1800" height="1200" alt="host_activity" src="https://github.com/user-attachments/assets/6c5f1822-443e-4a6d-b66e-eaea5f11e691" />

<img width="960" height="720" alt="http_status_code_distributions" src="https://github.com/user-attachments/assets/4b365681-8bbf-4077-b21c-41220f662233" />

<img width="1800" height="900" alt="requests_by_hour" src="https://github.com/user-attachments/assets/80ed7e56-b0d2-4b25-975e-005469122abc" />
