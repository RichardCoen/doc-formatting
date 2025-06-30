from tools import read_json,write_dict_to_json,read_txt
import os
import random
def write_txt(file_name, content):
    """
    将内容写入指定的.txt文件。

    参数:
    - file_name (str): 文件名，可以包括路径，例如 'example.txt' 或 'path/to/example.txt'。
    - content (str): 要写入文件的内容。
    """
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"内容已成功写入文件 {file_name}")
    except Exception as e:
        print(f"写入文件时出错: {e}")


def write_shot(save_path,code_file):
    data_list = read_json(code_file)["data_list"]
    shot_list = []
    for data in data_list:
        if data["property_number"] > 4:
            continue
        else:
            user_input = data["user_input"]
            code = data["test_code"]
            shot_list.append({"user_input":user_input,"code":code})
            write_dict_to_json({"data_list":shot_list},save_path)

def random_prompt(shot_list_file,label_file,shot_number,save_file):
    data_list = read_json(label_file)["data_list"]
    shot_list = read_json(shot_list_file)["data_list"]
    prompt_list = []
    for data in data_list:
        sample = {"id":data["id"],"user_input":data["best_rewrite"],"shot_list":[],"prompt":"""Task Description:
Develop a Node.js plugin for Microsoft Word that dynamically generates and executes the Word.run() function based on user input to modify document formatting. Ensure the solution uses JavaScript Word API 1.1 for all interactions with the Word document. Read the input-output samples below to generate code based on user input.

Input Sample:
"""}
        random_shot_list = random.sample(shot_list, shot_number)
        #组合random shot
        for i in range(shot_number):
            input_number = i+1
            shot = random_shot_list[i]
            # print(shot)
            sample["shot_list"].append(shot)
            sample["prompt"] += """\nInput {}:\n{}\n\nOutput {}:\n{}""".format(input_number,shot["user_input"],input_number,shot["code"])

        sample["prompt"] += """Input {}:\n{}\n\nOutput {}:""".format(shot_number+1, data["best_rewrite"],shot_number+1)
        prompt_list.append(sample)

    write_dict_to_json({"Description":"Random Shot for Few-shot","data_list":prompt_list},save_file)

if __name__ == '__main__':

    # write_shot(save_path="./prompt_data/shot/used_for_Test.json",code_file="./dataset/val_data.json")
    # write_shot(save_path="./prompt_data/shot/used_for_Val.json",code_file="./dataset/Test_data.json")
    #Test dataset for random shot
    shot_list_file = "./prompt_data/shot/used_for_Test.json"
    label_file = "./dataset/test_dataset_label_result.json"
    shot_number = 17
    save_file = "prompt_data/random_shot_fewshot/Test/random1prompt.json"
    random_prompt(shot_list_file,label_file,shot_number,save_file)


