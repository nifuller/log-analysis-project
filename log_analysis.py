import re
import pandas as pd

def open_txt():
    pattern = r" - - "
    line_dict = {}
    line_list = []

    with open('data/access_logs.txt', 'r') as f:
        for i, line in enumerate(f):
            # if i == 20:
            #     break
            # print(line)
            clean_line = line.replace(pattern, " ")
            
            
            ip = clean_line.split()[0]
            date = re.findall(r"\[(.*?)\]",clean_line)
            date = date[0] if date else None
            request_match = re.findall(r"\"(.*?)\"", clean_line)
            if not request_match:
                continue
            request = request_match[0]
            status_code = clean_line.rsplit(' ', 2)[1]
            size = clean_line.rsplit(' ', 1)[1].strip()
            
            line_dict = {"host":ip, "timestamp": date, "request": request,
                              "status": status_code, "bytes":size}
            
            line_list.append(line_dict)
            # print(clean_line)
            # print(ip)
            # print(date)
            # print(request)
            # print(status_code)
            # print(size)
            
        # print(line_list)
    df = pd.DataFrame(line_list)
    df = df.reset_index(drop=True)
    df.to_csv("access_logs.csv", index=False)

open_txt()