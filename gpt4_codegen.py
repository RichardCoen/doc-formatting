from tools import gpt4_zz,copy_files,deepseek_v2_l
from Code_Generation import CodeGen_Simul,generated_code_integration
def val_code_gen():
    # gpt-4-turbo-0425
    i = 20
    dataset_name = "Val"
    model_name = "gpt4"
    api = gpt4_zz
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    # "./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i),0,955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "self_debug"
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/val_selfdebug_prompt.json",0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json",137, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # # RAG+Few-shot
    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,
    #                                                                                 doc_number, n_shot), 0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "direct_prompt"
    # CodeGen_Simul(api, dataset_name, model_name, method_name,"./prompt_data/direct_prompt/val_0_shot_prompt.json", 31, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # refine 1
    # method_name = "direct_prompt_refine1"
    # refile_prompt_name = "direct_prompt"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # n_shot = 17
    # doc_number = 15
    # method_name = "RAG_few_shot_refine1/e5_{}/{}_shot".format(doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot/e5_{}/{}_shot".format(doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine1/17_shot"
    # refile_prompt_name = "few_shot/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine1/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "self_debug_refine1"
    # refile_prompt_name = "self_debug"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # refine2
    refine_time = 3
    # refine 3
    # refine_time = 3
    method_name = "direct_prompt_refine{}".format(refine_time)
    last_method_name = "direct_prompt_refine{}".format(refine_time - 1)
    copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
               dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    CodeGen_Simul(api, dataset_name, model_name, method_name,
                  "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
                                                                        last_method_name, refine_time), 0,
                  955)
    generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


    # n_shot = 17
    # doc_number = 15
    # method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time,doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time-1,doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name,refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine{}/17_shot".format(refine_time)
    # refile_prompt_name = "few_shot_refine{}/17_shot".format(refine_time-1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name,refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine{}/e5_20".format(refine_time)
    # refile_prompt_name = "doc_prompt_refine{}/e5_20".format(refine_time-1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                    refile_prompt_name,refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "self_debug_refine{}".format(refine_time)
    # last_method_name = "self_debug_refine{}".format(refine_time - 1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     last_method_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

if __name__ == '__main__':
    # val_code_gen()

    # Prompt = "Task Description:\nDevelop a Node.js plugin for Microsoft Word that dynamically generates and executes the Word.run() function based on user input to modify document formatting. Ensure the solution uses JavaScript Word API 1.1 for all interactions with the Word document. Use the provided APIs Knowlegde and API documentations for guidance. Read the API documentation thoroughly to generate the required code according to user input.\n\nUser Input:\nFor the initial paragraph, please remove the bold formatting and set the outline level to Level 5.\n\nFunction Structure:\n```javascript\nWord.run(async function (context) {\n// Code to be implemented here\nawait context.sync();\n});\n```\n\nOutput: \nComplete the Word.run() above to perform the user's formatting requests. The code should include proper loading of the paragraph properties, application of the desired styles, and any necessary synchronization with the Word document context. Please provide a complete and executable Word.run() function:"
    # print(Prompt)

    dataset_name = "Test"
    model_name = "deepseek_v2"
    api = deepseek_v2_l
    for i in [9]:
        method_name = "few_shot/{}_shot".format(i)
        # CodeGen_Simul(api, dataset_name, model_name, method_name,
        #               "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i), 680, 956)
        generated_code_integration("./dataset/test_data.json", dataset_name, model_name, method_name)
