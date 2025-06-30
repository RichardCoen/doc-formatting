from tools import read_json,write_dict_to_json,create_directory

def error_statistic(dataset_name,model_name,method_name):
    error_dir = {}
    data_list = read_json("./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name,model_name,method_name))["data_list"]
    for data in data_list:
        if data["error_info"]["error_name"]:
            key = data["error_info"]["error_name"]
            if data["error_info"]["error_name"] in error_dir:
                error_dir[key]+=1
            else:
                error_dir[key] =1

    count = sum(list(error_dir.values()))
    error_rate = {}
    for k in error_dir.keys():
        error_rate[k] = error_dir[k]/count

    save_file = "./error/{}/{}/{}/refine_1.json".format(dataset_name,model_name,method_name)
    create_directory("./error/{}/{}/{}/".format(dataset_name,model_name,method_name))
    write_dict_to_json({"dataset":dataset_name,"model":model_name,"method":method_name,"error_rate":error_rate,"error_count":error_dir},save_file)


if __name__ == '__main__':
    dataset_name = "Val"
    # model_name = "gpt4"
    model_name = "codeqwen"
    for method_name in ["few_shot/17_shot","doc_prompt/e5_20","RAG_few_shot/e5_15/17_shot","self_debug"]:
        error_statistic(dataset_name, model_name, method_name)