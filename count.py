import pandas as pd
from collections import Counter
import os

file_list = ["唯库.csv", "洛基英语.csv", "懂你英语.csv"]
filepath_list = ["results/" + filename for filename in file_list]
# filecount_list = ["statics/"+filename for filename in file_list]
print(filepath_list)

for fp in filepath_list:
    st_df = pd.DataFrame(columns=["account_tag", "wx_account_name", "count"])
    f_csv = pd.read_csv(fp)
    wx_account_name = list(f_csv["wx_account_name"])
    count_dict = Counter(wx_account_name)
    account_tag = fp.split("results/")[1].split(".csv")[0]
    st_df["account_tag"] = fp.split("results/")[1].split(".csv")[0]
    st_df["wx_account_name"] = list(count_dict.keys())
    st_df["count"] = list(count_dict.values())
    st_df.to_csv(os.path.join("statistics/", account_tag+".csv"), header=False)
