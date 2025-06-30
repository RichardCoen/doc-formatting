from tools import read_json,write_dict_to_json
l =[]
data = read_json("./dataset/test_dataset_label_result.json")["data_list"]
for d in data:
    l.append({"id":d["id"],"instruction":d["best_rewrite"]})

write_dict_to_json({"description":"test dataset","data_list":l},"./dataset/data/val.json")