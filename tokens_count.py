from tools import read_json,write_dict_to_json,create_directory
import os

def token_count(dataset_name,model_name,method_name):
    output_folder = "./code_generation/{}/{}/{}/".format(dataset_name,model_name,method_name)
    input_counts = []
    output_counts = []
    for root, dirs, files in os.walk(output_folder):
        for file in files:
            file_name = os.path.join(root, file)
            data = read_json(file_name)
            input_counts.append(data["input_tokens"])
            output_counts.append(data["output_tokens"])

    create_directory("Token_use/{}/{}/{}".format(dataset_name,model_name,method_name))
    save_path = "Token_use/{}/{}/{}/tokens.json".format(dataset_name,model_name,method_name)
    write_dict_to_json({"input_tokens_avg":int(sum(input_counts)/len(input_counts)),
                        "output_tokens_avg": int(sum(output_counts) / len(output_counts)),
                        "input_tokens_sum": sum(input_counts),
                        "output_tokens_sum":sum(output_counts),
                        },save_path)

if __name__ == '__main__':

    dataset_name = "Val"
    model_name = "gpt4"
    # method_names = ["direct_prompt","doc_prompt/e5_20","RAG_few_shot/e5_15/17_shot","self_debug","few_shot/17_shot"]
    method_names = ["direct_prompt_refine1", "doc_prompt_refine1/e5_20", "RAG_few_shot_refine1/e5_15/17_shot", "self_debug_refine1","few_shot_refine1/17_shot"]
    # method_names = ["direct_prompt_refine2", "doc_prompt_refine2/e5_20", "RAG_few_shot_refine2/e5_15/17_shot","self_debug_refine2","few_shot_refine2/17_shot"]
    # method_names = ["direct_prompt_refine3", "doc_prompt_refine3/e5_20", "RAG_few_shot_refine3/e5_15/17_shot","self_debug_refine3","few_shot_refine3/17_shot"]
    for method_name in method_names:
        token_count(dataset_name,model_name,method_name)
    pass