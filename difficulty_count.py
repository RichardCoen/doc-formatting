import pandas as pd
from tools import read_json,write_dict_to_json

diff_data = pd.read_excel("./property.xlsx",sheet_name="whole")["difficulty"]

# print(diff_data[5])
def difficulty_count(file_name):
    data_file = read_json(file_name)
    number = len(data_file["data_list"])

    for i in range(number):
        data = data_file["data_list"][i]
        difficulty = len(data["paragraphs"].keys())
        # print(difficulty)
        for para in data["paragraphs"].values():
            samples = para["property_adjust"]
            for sample in samples:
                index = int(sample[2])
                dif_score = diff_data[index]
                difficulty+=dif_score

        data_file["data_list"][i]["difficulty"] = int(difficulty)
        # print(difficulty)

    write_dict_to_json(data_file,file_name)


difficulty_count("./original_data/all_data.json")
