from tools import read_json,write_dict_to_json
import random

whole_data = read_json("./original_data/whole_data.json")["data_list"]
test_data = read_json("./original_data/test_data.json")["data_list"]

posi_add = ["For the opening paragraph", "In the first paragraph", "For the paragraph one", "For the first paragraph", "For the initial paragraph",
            "In the initial paragraph", "Turning to Paragraph 1", "In the opening paragraph"]

for data in whole_data[485:610]:
    index = int(data["id"]) % 7
    add = posi_add[index]
    data["user_input"] = add+", "+ data["user_input"]

all_data = whole_data+test_data

for i in range(len(all_data)):
    all_data[i]["id"] = str(i)

write_dict_to_json(data={"Description":" all data.0-484,\ntrain,485-621: atomic,\n 622-1288：test\n","data_list":all_data},json_file_path = "./original_data/all_data.json")

whole_label_data = read_json("./label_data/label_result/whole_label_result.json")["data_list"]
test_label_data = read_json("./label_data/label_result/test_1288_label_result.json")["data_list"]
for data in whole_label_data[485:610]:
    index = int(data["id"]) % 7
    add = posi_add[index]
    data["user_input"] = add+", "+ data["user_input"]
    data["best_rewrite"] = add+", "+ data["best_rewrite"]

all_label_data = whole_label_data+test_label_data
for i in range(len(all_label_data)):
    all_label_data[i]["id"] = str(i)

write_dict_to_json(data={"Description":" all data.0-484,\ntrain,485-621: atomic,\n 622-1288：test\n","data_list":all_data},json_file_path = "./label_data/label_result/all_label_result.json")

val_data = []
test_data = []

for data in all_data:
    if int(data["id"]) % 2 == 0:
        test_data.append(data)
    else:
        val_data.append(data)


for i in range(len(val_data)):
    val_data[i]["id_all"] = val_data[i]["id"]
    val_data[i]["id"] = str(i)

for i in range(len(test_data)):
    test_data[i]["id_all"] = test_data[i]["id"]
    test_data[i]["id"] = str(i)

write_dict_to_json({"Description":"test data, half of all","data_list":test_data},"./dataset/test_data.json")
write_dict_to_json({"Description":"val data, half of all","data_list":val_data},"./dataset/val_data.json")

def get_label(dataset, save_path, all_data, desription = "test dataset label result"):
    results = []
    for data in dataset:
        index_id = int(data["id_all"])
        sample = all_data[index_id]
        sample["id_all"] = sample["id"]
        sample["id"] = data["id"]
        results.append(sample)

    write_dict_to_json({"Description": desription, "data_list": results},
                       save_path)


get_label(test_data,"./dataset/test_dataset_label_result.json",all_data=all_label_data)
get_label(val_data,"./dataset/val_dataset_label_result.json",all_data=all_label_data,desription="val dataset label result")