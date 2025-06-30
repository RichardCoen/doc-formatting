from  tools import  gemini_api,copy_files
from Code_Generation import  CodeGen_Simul,generated_code_integration

def gemini_ablation():
    dataset_name = 'Test'
    model_name = "gemini_pro"
    api = gemini_api
    method_name = "doc_prompt_refine1/e5_15"
    refile_prompt_name = "doc_prompt/e5_15"
    copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
           dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    CodeGen_Simul(api, dataset_name, model_name, method_name,
              "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
              955)
    generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

if __name__ == '__main__':
    gemini_ablation()