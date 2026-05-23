# log-analysis-project

## 📈 Progress
- [x] Downloaded and explored NASA HTTP dataset
- [x] Built log parser in Python
- [x] Load data into SQLite
- [x] Write security focused SQL queries
- [x] Build visualizations
- [ ] Write up findings

# Project Overview
Analyzed over 1.8 million HTTP requests from NASA's Kennedy Space Center web server using the July 1995 dataset. The raw dataset required a custom regex parser to extract structured fields from an unformatted log file before any analysis could begin with The main tools used in this project were Python, Pandas, SQLite, and Matplotlib with the goal of identifying anomalous traffic patterns and investigating potential security threats. Specifically looking for any unusual overnight activity spikes, error rates, and suspicious endpoint access. Each anomalous traffic pattern was thoroughly investigated using the full analyst workflow of detection, investigation, and false positive reduction.

# Data Processing
The raw NASA log file was not a standard CSV file. Each unstructured line contained the IP address, timestamp HTTP request, status code, and byte size as a single string. A custom regex parser script was written in Python to clean any malformed strings and to structure the data by extracting each field line by line. Then it was loaded into both a Pandas dataframe and a SQLite database for analysis and querying. 


# Key Findings

1. Overnight traffic anomaly
2. Japanese timezone pattern
3. 404 error analysis
4. CGI endpoint probing
5. False positive reduction

# Conclusion

# Visualizations

<img width="1800" height="1200" alt="host_activity" src="https://github.com/user-attachments/assets/6c5f1822-443e-4a6d-b66e-eaea5f11e691" />

<img width="960" height="720" alt="http_status_code_distributions" src="https://github.com/user-attachments/assets/4b365681-8bbf-4077-b21c-41220f662233" />

<img width="1800" height="900" alt="requests_by_hour" src="https://github.com/user-attachments/assets/80ed7e56-b0d2-4b25-975e-005469122abc" />
