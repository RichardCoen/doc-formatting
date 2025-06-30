from Code_Generation import CodeGen_Simul,generated_code_integration
from tools import read_json,write_dict_to_json,gpt35_zz,qwen_turbo,deepseek_coder,deepseek_v2,code_qwen,gemini_api,copy_files

# refine 1
dataset_name = 'Test'

# gemini_pro
model_name = "gemini_pro"
refile_prompt_name = "few_shot/17_shot"
method_name = "few_shot_refine/17_shot"
# copy_files(src_dir="./code_generation/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_generation/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
# generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

method_name = "doc_prompt_refine/e5_20"
refile_prompt_name = "doc_prompt/e5_20"
# copy_files(src_dir="./code_generation/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_generation/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(gemini_api, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
# generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

#deepseek_v2
model_name = "deepseek_v2"

refile_prompt_name = "few_shot/17_shot"
method_name = "few_shot_refine/17_shot"
# copy_files(src_dir="./code_generation/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
           # dst_dir="code_generation/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,
              # "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
# generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

method_name = "doc_prompt_refine/e5_20"
refile_prompt_name = "doc_prompt/e5_20"
# copy_files(src_dir="./code_generation/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_generation/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(deepseek_v2, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),105, 956)
# generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


# deepseek_coder
model_name = "deepseek_coder"

refile_prompt_name = "few_shot/17_shot"
method_name = "few_shot_refine/17_shot"
# copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

method_name = "doc_prompt_refine/e5_20"
refile_prompt_name = "doc_prompt/e5_20"
# copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(deepseek_coder, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)


#qwen_plus
model_name = "qwen_plus"

refile_prompt_name = "few_shot/17_shot"
method_name = "few_shot_refine/17_shot"
# copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(qwen_plus, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)

generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
method_name = "doc_prompt_refine/e5_20"
refile_prompt_name = "doc_prompt/e5_20"
# copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(qwen_plus, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

#gpt35

model_name = "gpt35"

refile_prompt_name = "few_shot/17_shot"
method_name = "few_shot_refine/17_shot"
# copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)

method_name = "doc_prompt_refine/e5_20"
refile_prompt_name = "doc_prompt/e5_20"
# copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
#            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
# CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
#               "./prompt_data/refine/{}/{}/refine_1.json".format(model_name,refile_prompt_name),0, 956)
generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)




