from tools import read_json,write_dict_to_json

#
# for i in [1,5,9,13,17,21]:
#     data = read_json("./code_generation/Test/gemini_pro/few_shot/{}_shot_code.json".format(i))
#     data_code = data["list"][243:305]
#     data["list"] = data_code
#
#
# for i in [5,10,15,20]:
#     data = read_json("./code_generation/Test/gemini_pro/doc_prompt/bge_{}_code.json".format(i))
#     data_code = data["list"][243:305]
#     data["list"] = data_code
#     write_dict_to_json(data,"./judge_code/bge_{}_code_judge.json".format(i))
#
#     data = read_json("./code_generation/Test/gemini_pro/doc_prompt/gte_{}_code.json".format(i))
#     data_code = data["list"][243:305]
#     data["list"] = data_code
#     write_dict_to_json(data,"./judge_code/gte_{}_code_judge.json".format(i))
#
#     data = read_json("./code_generation/Test/gemini_pro/doc_prompt/e5_{}_code.json".format(i))
#     data_code = data["list"][243:305]
#     data["list"] = data_code
#     write_dict_to_json(data,"./judge_code/e5_{}_code_judge.json".format(i))
#
#     data = read_json("./code_generation/Test/gemini_pro/doc_prompt/mxbai_{}_code.json".format(i))
#     data_code = data["list"][243:305]
#     data["list"] = data_code
#     write_dict_to_json(data,"./judge_code/mxbai_{}_code_judge.json".format(i))

from tools import read_json
count = 0
data_list = read_json("./dataset/test_dataset_label_result.json")["data_list"]
for data in data_list:
    value = list(data["rewrite_scores"].values())
    if max(value)>0:
        continue
    else:
        count+=1

data_list = read_json("./dataset/val_dataset_label_result.json")["data_list"]
for data in data_list:
    value = list(data["rewrite_scores"].values())
    if max(value)>0:
        continue
    else:
        count+=1

print(count)
print(count/1911)
print(68/1911)