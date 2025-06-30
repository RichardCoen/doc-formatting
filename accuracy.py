import math
import os
from tools import write_dict_to_json,read_json,create_directory
import json


def accuracy(property_file, gene_folder, example_folder, init_folder, save_result_path):

    data_list = read_json(property_file)["data_list"]
    acc_rate_list = []
    acc_rate_dict = {}
    code_states = {}
    code_error = 0
    error_tigger_dict = {}

    for data in data_list:
        file_name = "{}.json".format(data["id"])
        gene_file_path = os.path.join(gene_folder, file_name)
        example_file_path = os.path.join(example_folder, file_name)
        init_file_path = os.path.join(init_folder,file_name)
        code_type = read_json(gene_file_path)["code_type"]
        difficulty = data["difficulty"]

        gene_result = read_json(gene_file_path)["paragraphs_attributions"]
        example_result = read_json(example_file_path)["paragraphs_attributions"]
        init_result = read_json(init_file_path)["paragraphs_attributions"]
        acc_number = 0
        if code_type == "Code Error":
            code_states[data["id"]] = 0
            code_error+=1

        else:
            code_states[data["id"]] = 1
            for key, paragraph in data["paragraphs"].items():
                # 找到每个段落被修改的属性
                property_read_list = paragraph["property_read"]
                for prop in property_read_list:
                    gene_prop_value = gene_result[key][prop]
                    example_prop_value = example_result[key][prop]
                    if type(gene_prop_value) == type(1) or type(gene_prop_value) == type(1.0):
                        if math.fabs(gene_prop_value - example_prop_value) <= 1e-4:
                            acc_number += 1
                    else:
                        if gene_prop_value == example_prop_value:
                            acc_number += 1

       # 计算geneted_result和init_result的相同数量
       #  different_number = 0
       #  for para_key in example_result.keys():
       #      init_para = init_result[para_key]
       #      gene_para = gene_result[para_key]
       #
       #      if para_key == "10":
       #          continue
       #      for prop_key in init_para.keys():
       #          init_prop_value = init_para[prop_key]
       #          gene_prop_value = gene_para[prop_key]
       #
       #          if para_key == "selected" and prop_key in ["outlineLevel","firstLineIndent","leftIndent","rightIndent","lineSpacing","spaceBefore","spaceAfter","alignment"]:
       #              continue
       #          # 数据类型相等
       #          if type(gene_prop_value) == type(init_prop_value):
       #              #都是数值类型的情况
       #              if type(gene_prop_value) == type(1) or type(gene_prop_value) == type(1.0):
       #                  if math.fabs(gene_prop_value - init_prop_value) > 1e-4:
       #                      different_number += 1
       #              #是别的类型的情况：
       #              else:
       #                  if gene_prop_value != init_prop_value:
       #                      different_number += 1
       #          #数据类型都不相等
       #          else:
       #              different_number += 1

        acc_rate = acc_number / data["property_number"]
        acc_rate_dict[data["id"]] = acc_rate
        acc_rate_list.append(acc_rate)


        # error_trigger = different_number - acc_number
        # error_tigger_dict[data["id"]] = error_trigger

    acc = round(sum(acc_rate_list)/len(acc_rate_dict),4)
    code_error = round(code_error/len(code_states),4)
    wrong = round(1-acc-code_error,4)
    write_dict_to_json({"description":"accuracy result","acc": acc,"code_error_rate":code_error,"wrong":wrong,"acc_wo_atomic": sum(acc_rate_list[:485])/485,"error_tigger_dict":error_tigger_dict,"code_state": code_states,"acc_dict":acc_rate_dict,},save_result_path)


def diffuculty_statistic(acc_file, property_file,save_name):

    data_list = read_json(property_file)["data_list"]
    acc_list = read_json(acc_file)
    difficulty_results = {
        "acc":
            {"easy": [],
             "middle": [],
             "challenged": [],
             "hard": []},
        "code_error":
            {"easy": [],
             "middle": [],
             "challenged": [],
             "hard": []}
    }
    for data in data_list:
        difficulty = data["difficulty"]
        key = data["id"]
        acc_rate = acc_list["acc_dict"][key]
        error_state = acc_list["code_state"][key]
        if 1 < difficulty < 6:
            difficulty_results["acc"]["easy"].append(acc_rate)
            difficulty_results["code_error"]["easy"].append(1-error_state)
        elif 6 <= difficulty < 11:
            difficulty_results["acc"]["middle"].append(acc_rate)
            difficulty_results["code_error"]["middle"].append(1-error_state)
        elif 11 <= difficulty < 16:
            difficulty_results["acc"]["challenged"].append(acc_rate)
            difficulty_results["code_error"]["challenged"].append(1-error_state)
        else:
            difficulty_results["acc"]["hard"].append(acc_rate)
            difficulty_results["code_error"]["hard"].append(1-error_state)

    difficulty_distribution = {
    "acc":
        {"easy": [],
        "middle": [],
        "challenged": [],
        "hard": []},
        "code_error":
            {"easy": [],
            "middle": [],
            "challenged": [],
            "hard": []}
            }
    for key1 in ["acc", "code_error"]:
        for key2 in ["easy","middle","challenged","hard"]:
            difficulty_distribution[key1][key2] = round(sum(difficulty_results[key1][key2])/len(difficulty_results[key1][key2]),4)

    write_dict_to_json({"difficulty_distri":difficulty_distribution,"details":difficulty_results},save_name)

def property_statistic(acc_file, property_file,save_name):

    data_list = read_json(property_file)["data_list"]
    acc_list = read_json(acc_file)
    property_results = {
        "acc":{},"error_rate":{},"wrong":{}
    }
    for data in data_list:
        prop_number = data["property_number"]
        key = data["id"]
        acc_rate = acc_list["acc_dict"][key]
        error_rate = 1- acc_list["code_state"][key]
        if prop_number in property_results["acc"].keys():
            property_results["acc"][prop_number].append(acc_rate)
            property_results["error_rate"][prop_number].append(error_rate)
        else:
            property_results["acc"][prop_number] = [acc_rate]
            property_results["error_rate"][prop_number] = [error_rate]

    keys = list(property_results["acc"].keys())
    result = {"acc":{},"error_rate":{},"wrong":{}}
    for key in keys:
        result["acc"][key] = round(sum(property_results["acc"][key])/len(property_results["acc"][key]),4)
        result["error_rate"][key] = round(sum(property_results["error_rate"][key]) / len(property_results["error_rate"][key]), 4)
        result["wrong"][key] = round(1- result["acc"][key]-result["error_rate"][key] , 4)

    property_sta = {}
    property_sta["property_number"] = list(dict(sorted(result["acc"].items(), key=lambda item: int(item[0]))).keys())
    property_sta["acc"] = list(dict(sorted(result["acc"].items(), key=lambda item: int(item[0]))).values())
    property_sta["error_rate"] = list(dict(sorted(result["error_rate"].items(), key=lambda item: int(item[0]))).values())
    property_sta["wrong"] = list(
        dict(sorted(result["wrong"].items(), key=lambda item: int(item[0]))).values())

    write_dict_to_json({"property influence": property_sta},save_name)

def val_acc():

    property_file = "./dataset/val_data.json"
    example_folder = "./code_result/val_example"
    init_folder = "./code_result/val_init/"
    dataset = "Val"
    # model_names = ["qwen2",]
    # model_names = ["llama3", ]
    # model_names = ["deepseek_coder", "gpt35", "deepseek_v2", "qwen_turbo", "gpt4", "gemini_pro",]
    model_names = ["deepseek_coder", "gpt35", "deepseek_v2", "qwen_turbo", "gpt4","gemini_pro","codeqwen","llama3","qwen2"]
    # model_names = ["codeqwen", ]
    for model_name in model_names:
        # method_names = ["few_shot/17_shot", "doc_prompt/e5_20","self_debug","RAG_few_shot/e5_15/17_shot","direct_prompt"]
        method_names = ["RAG_few_shot_refine2/e5_15/17_shot"]
        # method_names = ["direct_prompt"]
        # method_names = ["direct_prompt_refine3"]

        # method_names = ["few_shot_refine3/17_shot", "doc_prompt_refine3/e5_20",  "RAG_few_shot_refine3/e5_15/17_shot","self_debug_refine3","direct_prompt_refine3"]

        for method_name in method_names:
            result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
            create_directory("./acc/{}/{}/{}/".format(dataset, model_name,method_name))
            accuracy(property_file, result_dir, example_folder, init_folder,
             "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))



def tes_acc():
    property_file = "./dataset/test_data.json"
    example_folder = "./code_result/test_example"
    init_folder = "./code_result/test_init/"
    dataset = "Test"

    #RAG
    # for i in [5,10,15,20]:
    #     model_name = "gemini_pro"
    #
    #     method_name = "doc_prompt/bge_{}".format(i)
    #     result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #     create_directory("./acc/{}/{}/doc_prompt/".format(dataset, model_name))
    #     accuracy(property_file, result_dir, example_folder, init_folder,
    #              "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))
    #
    #     method_name = "doc_prompt/gte_{}".format(i)
    #     result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #     create_directory("./acc/{}/{}/doc_prompt/".format(dataset, model_name))
    #     accuracy(property_file, result_dir, example_folder, init_folder,
    #              "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))
    #
    #     method_name = "doc_prompt/e5_{}".format(i)
    #     result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #     create_directory("./acc/{}/{}/doc_prompt/".format(dataset, model_name))
    #     accuracy(property_file, result_dir, example_folder, init_folder,
    #              "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))
    #
    #     method_name = "doc_prompt/mxbai_{}".format(i)
    #     result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #     create_directory("./acc/{}/{}/doc_prompt/".format(dataset, model_name))
    #     accuracy(property_file, result_dir, example_folder, init_folder,
    #              "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))

    #n shot
    # model_name = "gemini_pro"
    # model_name = "code_qwen"
    # model_name = "qwen2"
    # for i in [1,5,9,13,17,21]:
    #     # for model_name in ["gemini_pro","code_qwen"]:
    #     for model_name in ["deepseek_v2", ]:
    #         method_name = "few_shot/{}_shot".format(i)
    #         result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #         create_directory("./acc/{}/{}/few_shot".format(dataset, model_name))
    #         accuracy(property_file, result_dir, example_folder, init_folder,
    #                  "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))

    # for n_shot in [13, 17, 21]:
    #     for doc_number in [5, 10, 15, 20]:
    #             method_name = "RAG_few_shot/e5_{}/{}_shot".format( doc_number, n_shot)
    #             result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #             create_directory("./acc/{}/{}/{}/".format(dataset, model_name, method_name))
    #             accuracy(property_file, result_dir, example_folder, init_folder,
    #                      "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))
    # for n_shot in [13, 17, 21]:
    #     for doc_number in [5, 10, 15, 20]:
    #         for refine_time in [1,2,3,4,5]:
    #             method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time, doc_number, n_shot)
    #             result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #             create_directory("./acc/{}/{}/{}/".format(dataset, model_name, method_name))
    #             accuracy(property_file, result_dir, example_folder, init_folder,
    #                      "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))

    #random shot

    for n_shot in [1,5,9,13,17,21]:
        model_name = 'deepseek_v2'
        model_name = 'qwen2'
        method_name = "random_fewshot/{}_shot".format(n_shot)
        result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
        create_directory("./acc/{}/{}/{}/".format(dataset, model_name, method_name))
        accuracy(property_file, result_dir, example_folder, init_folder,
                                 "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))

    for n_shot in [1,5,9,13,17,21]:
        model_name = 'deepseek_v2'
        model_name = 'qwen2'
        method_name = "another_fewshot/{}_shot".format(n_shot)
        result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
        create_directory("./acc/{}/{}/{}/".format(dataset, model_name, method_name))
        accuracy(property_file, result_dir, example_folder, init_folder,
                                 "./acc/{}/{}/{}_acc.json".format(dataset, model_name, method_name))

def difficulty_anly():
    pass
    #val
    # for model_name in ["gemini_pro","gpt35","gpt4","deepseek_v2"]:
    #     diffuculty_statistic(property_file="./dataset/val_data.json",
    #                          acc_file="./acc/Val/{}/RAG_few_shot_refine3/e5_15/17_shot_acc.json".format(model_name),
    #                          save_name="./acc/acc_analysis/difficulty/val_{}_ragshot.json".format(model_name))
    #
    for model_name in ["gemini_pro","gpt35","gpt4","deepseek_v2"]:
        property_statistic(property_file="./dataset/val_data.json",
                             acc_file="./acc/Val/{}/RAG_few_shot/e5_15/17_shot_acc.json".format(model_name),
                             save_name="./acc/acc_analysis/property/val_{}_ragshot.json".format(model_name))

    # for model_name in ["gemini_pro","gpt35","gpt4","deepseek_v2"]:
    #     for refine_time in [3]:
    #         property_statistic(property_file="./dataset/val_data.json",
    #                          acc_file="./acc/Val/{}/RAG_few_shot_refine{}/e5_15/17_shot_acc.json".format(model_name,refine_time,),
    #                          save_name="./acc/acc_analysis/property/val_{}_ragshot_refine{}.json".format(model_name,refine_time))


if __name__ == '__main__':
    pass
    # val_acc()
    tes_acc()
    # difficulty_anly()



