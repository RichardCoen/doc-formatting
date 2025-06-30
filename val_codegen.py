from Code_Generation import CodeGen_Simul, generated_code_integration
from tools import gpt35_zz,copy_files

def gpt_gen():
    # gpt-3.5-turbo-0125
    i = 20
    dataset_name = "Val"
    model_name = "gpt35"
    api = gpt35_zz
    # method_name = "doc_prompt/e5_{}".format(i)
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    # "./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i),0,955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "self_debug"
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/self-debug/val_selfdebug_prompt.json",1, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # method_name = "few_shot/17_shot"
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/fewshot_prompt/val_dataset/17_shot_prompt.json",38, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # RAG+Few-shot

    # n_shot = 17
    # embedding_name = "e5"
    # doc_number = 15
    # method_name = "RAG_few_shot/{}_{}/{}_shot".format(embedding_name, doc_number, n_shot)
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name, embedding_name,
    #                                                                                 doc_number, n_shot), 843, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # zero-shot
    # method_name = "direct_prompt"
    # CodeGen_Simul(api, dataset_name, model_name, method_name, "./prompt_data/direct_prompt/val_0_shot_prompt.json",
    #               0, 955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # refine1

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
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine1/17_shot"
    # refile_prompt_name = "few_shot/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine1/e5_20"
    # refile_prompt_name = "doc_prompt/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    # method_name = "self_debug_refine1"
    # refile_prompt_name = "self_debug"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # # refine3
    api = gpt35_zz
    refine_time = 3
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
    # method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time, doc_number, n_shot)
    # refile_prompt_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time - 1, doc_number, n_shot)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(api, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name,
    #                                                                     refile_prompt_name, refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "few_shot_refine3/17_shot"
    # refile_prompt_name = "few_shot_refine2/17_shot"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_3.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)
    #
    # method_name = "doc_prompt_refine3/e5_20"
    # refile_prompt_name = "doc_prompt_refine2/e5_20"
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, refile_prompt_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_3.json".format(dataset_name, model_name, refile_prompt_name), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)

    # refine2
    # refine_time = 2
    # refine_time = 3
    # method_name = "self_debug_refine{}".format(refine_time)
    # refile_prompt_name = "self_debug"
    # last_method_name = "self_debug_refine{}".format(refine_time-1)
    # copy_files(src_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, last_method_name),
    #            dst_dir="./code_result/{}/{}/{}".format(dataset_name, model_name, method_name))
    # CodeGen_Simul(gpt35_zz, dataset_name, model_name, method_name,
    #               "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset_name, model_name, refile_prompt_name,refine_time), 0,
    #               955)
    # generated_code_integration("./dataset/val_data.json", dataset_name, model_name, method_name)


if __name__ == '__main__':
    gpt_gen()