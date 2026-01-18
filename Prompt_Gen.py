from tools import gemini_api,read_json,write_dict_to_json,create_directory,read_txt
# import pandas as pd
# from retrieval import api_recall,db_create
import os
# from langchain.embeddings import HuggingFaceBgeEmbeddings
def prompt_generation(user_input):
    prompt ="""Task Description:
Develop a Node.js plugin for Microsoft Word that dynamically generates and executes the Word.run() function based on user input to modify document formatting. Ensure the solution uses JavaScript Word API 1.1 for all interactions with the Word document. Use the provided APIs Knowlegde and API documentations for guidance. Read the API documentation thoroughly to generate the required code according to user input.

User Input:
"""+user_input+"""

Function Structure:
```javascript
Word.run(async function (context) {
// Code to be implemented here
await context.sync();
});
```

Output: 
Complete the Word.run() above to perform the user's formatting requests. The code should include proper loading of the paragraph properties, application of the desired styles, and any necessary synchronization with the Word document context. Please provide a complete and executable Word.run() function:"""
    return prompt


def RAG_prompt_gen(result_file, index_dir, embedding, recall_k, save_path):

    data_list = read_json(result_file)["data_list"]
    results = []

    for data in data_list:
        apis = """[paragraphs.items]: Gets the loaded children in this collection. Must be called before reading properties context.sync().
Example:
```javascript
const paragraphs = context.document.body.paragraphs;
paragraphs.load("$none");
await context.sync();
const paragraph = paragraphs.items[1];
```
----------------
[getSelection()]: Gets the current selection of the document. Multiple selections are not supported.
```TypeScript
return:Word.Range;
```
Example:
```javascript
const range = context.document.getSelection();
var paragraphs = range.paragraphs;
var first_paragraph = range.paragraphs.getFirst();
var font = range.font;
```
----------------
"""
        # print(data["id"])
        user_input = data["best_rewrite"]
        recall_docs = api_recall(embeddings=embedding,index_dir=index_dir,query=user_input,recall_k=recall_k)
        for doc in recall_docs:
            apis += doc[0].page_content+"\n"

        prompt = prompt_generation(user_input=user_input,apis=apis)
        results.append({"id":data["id"],"user_input":user_input,"prompt":prompt,"docs":str(recall_docs)})

    write_dict_to_json({"description": "RAG, {} docs".format(recall_k),"data_list":results},save_path)


def whole_theo_prompt_gen():
    import pandas as pd
    original_datas = read_json("../Data3.0/original_data/whole_data.json")["data_list"]
    label_datas = read_json("../Data3.0/label_data/label_result/whole_label_result.json")["data_list"]
    single_pd = pd.read_excel("../Data3.0/property.xlsx", sheet_name="whole")
    theo_results = []
    unit_reflect = {}
    unit_dict = {" ": None, "cm": "centimeter", "pt": "points", "lines": "lines", "ch": "character"}
    single_pd = pd.read_excel("./property.xlsx", sheet_name="whole")
    for i in range(137):
        index = str(i)
        unit_key = single_pd.iloc[i]["unit"]
        unit_value = unit_dict[unit_key]
        unit_reflect[index] = unit_value
    for index in range(len(label_datas)):
        data = original_datas[index]
        label_data = label_datas[index]
        result = {
            "id": data["id"],
            'original_input': data["user_input"],
            "best_rewrite": label_data["best_rewrite"]
        }

        apis = ""
        property_list, unit_list, position_list = [], [], []
        property_api, unit_api, location_api = "", "", ""

        position_list = ["paragraph","selected part"]
        for para_index, para in data["paragraphs"].items():
            # if para_index == "selected":
            #     position_list.append("selected part")
            # else:
            #     position_list.append("paragraph")

            property_list += para["property_read"]

            u_list = [unit_reflect[i[2]] for i in para["property_adjust"]]
            unit_list += u_list

        for property_name in list(set(property_list)):
            property_file = "../Data3.0/apis/property_apis/{}.txt".format(property_name)
            property_api += read_txt(property_file)

        for position_name in list(set(position_list)):
            position_file = "../Data3.0/apis/location_apis/{}.txt".format(position_name)
            location_api += read_txt(position_file)

        for unit_name in list(set(unit_list)):
            if unit_name:
                unit_file = "../Data3.0/apis/unit_apis/{}.txt".format(unit_name)
                unit_api += read_txt(unit_file)

        apis += location_api + property_api + unit_api
        best_rewrite = ""
        if 484 < int(data["id"]) < 484+125:
            best_rewrite = "For the first paragraph: "+result["best_rewrite"]
        else:
            best_rewrite = result["best_rewrite"]
        prompt = prompt_generation(best_rewrite, apis)

        result["property_api"] = property_api
        result["unit_api"] = unit_api
        result["location_api"] = location_api
        result["prompt"] = prompt
        theo_results.append(result)

    write_dict_to_json(
        {"Description": "Whole theoretical, all apis, all position description", "data_list": theo_results},
        "../Data3.0/prompt_data/simulation_data/whole_theo.json")


def txt_prompt(number,prompt_file,user_input):
    if type(number) == type(1):
        number +=1
    prompt = read_txt(prompt_file)
    user_input = """Input {}: {}\nOutput {}:""".format(number,user_input,number)
    return prompt+user_input

def zero_shot_prompt_gen():
    for file_name,save_name in [("./dataset/test_dataset_label_result.json","./prompt_data/direct_prompt/test_0_shot_prompt.json"),("./dataset/val_dataset_label_result.json","./prompt_data/direct_prompt/val_0_shot_prompt.json")]:
        create_directory(os.path.dirname(save_name))
        data_list = read_json(file_name)["data_list"]
        results = []
        for data in data_list:
            prompt = prompt_generation(data["best_rewrite"])
            user_input = data["best_rewrite"]
            index = data["id"]
            result = {"id":index,"user_input":user_input,"prompt":prompt}
            results.append(result)
        write_dict_to_json({"Description":"directly prompt with zero-shot","data_list":results},save_name)

def few_shot_prompt_gen(number, original_file, prompt_file, save_path):
    data_list = read_json(original_file)["data_list"]
    results = []
    for data in data_list:
        user_input = data["best_rewrite"]
        prompt = txt_prompt(number,prompt_file,user_input)
        results.append({"id":data["id"],"user_input":user_input,"prompt":prompt})

    write_dict_to_json({"description": "few-shot, k = ".format(number), "data_list": results}, save_path)

def error_info_prompt(result_dir, code_file, save_file):
    if not os.path.exists(code_file):
        print("Missing code file: {}".format(code_file))
        print("Please generate it first or update method_name_list/model_name_list.")
        return
    data_list = read_json(code_file)["list"]
    error_samples = []
    for data in data_list:
        result_path = os.path.join(result_dir,"{}.json".format(data["id"]))
        result = read_json(result_path)
        # print(result["id"])
        if result["code_type"] == "Code Error" and data["code"]:
            error_code = data["code"].replace("await Word.run","Word.run")
            error_info = result["error_message"]
            prompt = """```
{}
```
When I run this function, I meet the following error, error_message:
{}
Help me refine the code.
You should only output the codes without any explanation and natural language.
Wrap your code with "```""".format(error_code,error_info)
            error_samples.append({"id":data["id"],"prompt":prompt,"error_info":error_info})

        else:
            continue

    write_dict_to_json({"description":"error code self refine","length":len(error_samples),"data_list":error_samples},save_file)


def refine_RAG_Prompt(result_dir, code_file, index_dir, embedding, recall_k, save_path):
    data_list = read_json(code_file)["list"]
    error_samples = []
    for data in data_list:
        result_path = os.path.join(result_dir, "{}.json".format(data["id"]))
        result = read_json(result_path)
        if result["code_type"] == "Code Error":
            error_code = data["code"].replace("await Word.run", "Word.run")
            error_info = result["error_message"]
            apis = ""
            recall_docs = api_recall(embeddings=embedding, index_dir=index_dir, query=str(error_info), recall_k=recall_k)
            for doc in recall_docs:
                apis += doc[0].page_content + "\n"
            prompt = """Task Description:
When I run the function generated by llm, I meet the following error_message. Please read the function generated by llm, the error message and the Api documentation apis. Help me refine the code.

Function generated by llm:
```
{}
```

Error_message:
{}

APIs Knowledge:
Api documentation apis you may need, each api structure may include [api_name], TypeScript and Example code. Detailed instructions are as follows :
[api_name]: This tag represents the API's name and description. It describes the primary function and purpose of the API.
```TypeScript```: This tag describes the TypeScript data type of the API. This part may not be present under the respective API if this api is a method.
Example: provides example code that demonstrates how to use the API.
Each API is separated by a line of dashes (----------------) to clearly distinguish between different APIs.

Api documentation apis:
{}
Output:
You should only output the codes without any explanation and natural language. Wrap your code with '```'""".format(error_code, error_info,apis)
            error_samples.append({"id": data["id"], "prompt": prompt})
        else:
            continue

    write_dict_to_json(
        {"description": "error code self refine", "length": len(error_samples), "data_list": error_samples}, save_path)


def RAG_with_few_shot(rag_file, shot_k, save_path):
    rag_list = read_json(rag_file)["data_list"]
    prompt_list = []
    for rag in rag_list:
        rag_prompt = rag["prompt"]
        user_input = rag["user_input"]
        rag_prompt.replace("Read the API documentation thoroughly to generate the required code according to user input.","Read the API documentation and input-output samples below to generate code based on user input.")
        rag_prompt = rag_prompt.split("User Input:\n")[0]
        shot_samples = read_txt("./prompt_data/fewshot_sample/{}-shot.txt".format(shot_k)).split("Read the input-output samples below to generate code based on user input.\n\n")[-1]
        rag_prompt+=shot_samples
        user_input = """Input {}: {}\nOutput {}:""".format(shot_k+1, user_input, shot_k+1)
        prompt = rag_prompt + user_input
        prompt_list.append({"id":rag["id"],"user_input":rag["user_input"],"prompt":prompt})

    # print(prompt_list[0]["prompt"])
    write_dict_to_json({"Description":"rag with few-shot","data_list":prompt_list},save_path)


def refine_prompt():
    dataset = 'Val'
    # method_name_list = ["RAG_few_shot/e5_15/17_shot"]
    # method_name_list = ["few_shot/17_shot","doc_prompt/e5_20","RAG_few_shot/e5_15/17_shot","self_debug"]
    method_name_list = ["direct_prompt"]
    model_name_list = ["gpt4"]
    # model_name_list =["gemini_pro", "gpt35", "deepseek_v2", "deepseek_coder", "qwen_turbo","gpt4"]
    # model_name_list = ["qwen2","codeqwen","llama3"]
    # model_name_list = ["qwen2",]
    for method_name in method_name_list:
        for model_name in model_name_list:
            result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
            code_file = "./code_generation/{}/{}/{}_code.json".format(dataset, model_name, method_name)
            create_directory("./prompt_data/refine/{}/{}/{}".format(dataset, model_name, method_name))
            save_file = "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset, model_name, method_name)
            error_info_prompt(result_dir,
                              code_file,
                              save_file)


def refine2_prompt():
    dataset = 'Val'
    # method_name_list = ["RAG_few_shot_refine1/e5_15/17_shot"]
    method_name_list = ["few_shot_refine1/17_shot", "doc_prompt_refine1/e5_20", "RAG_few_shot_refine1/e5_15/17_shot","self_debug_refine1"]
    # model_name_list = ["gemini_pro", "gpt35", "deepseek_v2", "deepseek_coder", "qwen_turbo","codeqwen","gpt4","llama3"]
    # model_name_list = ["gpt35", "deepseek_v2", "deepseek_coder", "qwen_turbo"]
    # model_name_list = ["qwen2","codeqwen","llama3"]
    # model_name_list = ["codeqwen"]
    method_name_list = ["direct_prompt_refine1"]
    model_name_list = ["gpt4"]
    # model_name_list = ["gemini_pro", "gpt35", "deepseek_v2", "deepseek_coder", "qwen_turbo", "gpt4"]
    for method_name in method_name_list:
        for model_name in model_name_list:
            result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
            code_file = "./code_generation/{}/{}/{}_code.json".format(dataset, model_name, method_name)
            create_directory("./prompt_data/refine/{}/{}/{}".format(dataset, model_name, method_name))
            save_file = "./prompt_data/refine/{}/{}/{}/refine_2.json".format(dataset, model_name, method_name)
            error_info_prompt(result_dir,
                              code_file,
                              save_file)


    # dataset = 'Test'
    # method_name_list = ["RAG_few_shot_refine/e5_15/17_shot","RAG_few_shot_refine/e5_15/21_shot","RAG_few_shot_refine/e5_15/13_shot"]
    # model_name_list = ["gemini_pro"]
    # for method_name in method_name_list:
    #     for model_name in model_name_list:
    #         result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    #         code_file = "./code_generation/{}/{}/{}_code.json".format(dataset, model_name, method_name)
    #         create_directory("./prompt_data/refine/{}/{}/{}".format(dataset, model_name, method_name))
    #         save_file = "./prompt_data/refine/{}/{}/{}/refine_2.json".format(dataset, model_name, method_name)
    #         error_info_prompt(result_dir,
    #                           code_file,
    #                           save_file)

def refine3_prompt():
    dataset = 'Val'
    # method_name_list = ["RAG_few_shot_refine2/e5_15/17_shot"]
    # method_name_list = ["few_shot_refine2/17_shot", "doc_prompt_refine2/e5_20", "RAG_few_shot_refine2/e5_15/17_shot","self_debug_refine2"]
    # model_name_list = ["gemini_pro", "gpt35", "deepseek_v2", "deepseek_coder", "qwen_turbo", "codeqwen", "gpt4",
    #                    "llama3"]
    # model_name_list = [ "gpt35", "deepseek_v2", "deepseek_coder", "qwen_turbo","gpt4","gemini_pro"]
    # model_name_list= ["codeqwen"]
    # model_name_list = ["llama3","codeqwen"]
    # model_name_list = ["qwen2", "codeqwen", "llama3"]
    # model_name_list = ["codeqwen"]
    method_name_list = ["direct_prompt_refine2"]
    model_name_list = ["gpt4"]
    # model_name_list = ["gemini_pro", "gpt35", "deepseek_v2", "deepseek_coder", "qwen_turbo", "gpt4"]
    for method_name in method_name_list:
        for model_name in model_name_list:
            result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
            code_file = "./code_generation/{}/{}/{}_code.json".format(dataset, model_name, method_name)
            create_directory("./prompt_data/refine/{}/{}/{}".format(dataset, model_name, method_name))
            save_file = "./prompt_data/refine/{}/{}/{}/refine_3.json".format(dataset, model_name, method_name)
            error_info_prompt(result_dir,
                              code_file,
                              save_file)

def gpt_only_refine_prompt(stage=1):
    dataset = "Val"
    model_name = "gpt4"
    if stage == 1:
        method_name = "direct_prompt"
        save_file = "./prompt_data/refine/{}/{}/{}/refine_1.json".format(dataset, model_name, method_name)
    elif stage == 2:
        method_name = "direct_prompt_refine1"
        save_file = "./prompt_data/refine/{}/{}/{}/refine_2.json".format(dataset, model_name, method_name)
    elif stage == 3:
        method_name = "direct_prompt_refine2"
        save_file = "./prompt_data/refine/{}/{}/{}/refine_3.json".format(dataset, model_name, method_name)
    else:
        raise ValueError("stage must be 1, 2, or 3.")

    result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
    code_file = "./code_generation/{}/{}/{}_code.json".format(dataset, model_name, method_name)
    create_directory("./prompt_data/refine/{}/{}/{}".format(dataset, model_name, method_name))
    error_info_prompt(result_dir, code_file, save_file)


def gemini_explore():


    dataset = 'Test'
    model_name = "gemini_pro"
    refine_time = 5
    for i in [5, 10, 15, 20]:
        for j in [13, 17, 21]:
            method_name = "RAG_few_shot_refine1/e5_{}/{}_shot".format(i,j)
            for model_name in ["gemini_pro"]:
                result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
                code_file = "./code_generation/{}/{}/{}_code.json".format(dataset, model_name, method_name)
                create_directory("./prompt_data/refine/{}/{}/{}".format(dataset, model_name, method_name))
                save_file = "./prompt_data/refine/{}/{}/{}/refine_2.json".format(dataset, model_name, method_name)
                error_info_prompt(result_dir,
                                  code_file,
                                  save_file)
            # method_name = "RAG_few_shot_refine{}/e5_{}/{}_shot".format(refine_time-1,i, j)
            # for model_name in ["gemini_pro"]:
            #     result_dir = "./code_result/{}/{}/{}".format(dataset, model_name, method_name)
            #     code_file = "./code_generation/{}/{}/{}_code.json".format(dataset, model_name, method_name)
            #     create_directory("./prompt_data/refine/{}/{}/{}".format(dataset, model_name, method_name))
            #     save_file = "./prompt_data/refine/{}/{}/{}/refine_{}.json".format(dataset, model_name, method_name,refine_time)
            #     error_info_prompt(result_dir,
            #                       code_file,
            #                       save_file)

if __name__ == '__main__':
    pass
    # whole_theo_prompt_gen()



    #RAG-refine
    # refine_RAG_Prompt(result_dir="./code_result/gemini_whole_9-shot/", code_file="./code_generation/gemini_whole_9-shot_code.json",
    #                   index_dir="./apis/property_w_unit_index/", embedding=model, recall_k=5, save_path="./prompt_data/few-shot-RAG_refine/gemini_whole_9-shot-refine1.json")

    # refine_RAG_Prompt(result_dir="./code_result/few-shot-RAG-refine/gemini_pro_whole_9-shot_refine1", code_file="./code_generation/few-shot-RAG-refine/gemini_pro_whole_9-shot_refine1_code.json",
    #                   index_dir="./apis/property_w_unit_index/", embedding=model, recall_k=5, save_path="./prompt_data/few-shot-RAG_refine/gemini_whole_9-shot-refine2.json")

    #RAG

    # model_name = "BAAI/bge-large-en-v1.5"
    # model_kwargs = {'device': 'cpu', "trust_remote_code": True}
    # encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    # model = HuggingFaceBgeEmbeddings(
    #     model_name=model_name,
    #     model_kwargs=model_kwargs,
    #     encode_kwargs=encode_kwargs,
    #     query_instruction="为这个句子生成表示以用于检索相关文章："
    # )
    # for i in [5, 10, 15, 20]:
    #     recall_k = i
    #     save_path = "./prompt_data/recall_prompt/test_dataset/bge/bge_RAG_{}_whole.json".format(i)
    #     RAG_prompt_gen(embedding=model, result_file="./dataset/test_dataset_label_result.json",
    #                    index_dir="./apis/bge/property_w_unit_index/", recall_k=i,
    #                    save_path=save_path)
    #
    # model_name = "mixedbread-ai/mxbai-embed-large-v1"
    # model_kwargs = {'device': 'cpu',"trust_remote_code":True}
    # encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    # model = HuggingFaceBgeEmbeddings(
    #     model_name=model_name,
    #     model_kwargs=model_kwargs,
    #     encode_kwargs=encode_kwargs,
    #     query_instruction="为这个句子生成表示以用于检索相关文章："
    # )
    # for i in [5,10,15,20]:
    #     recall_k = i
    #     save_path = "./prompt_data/recall_prompt/test_dataset/mxbai/MXBAI_RAG_{}_whole.json".format(i)
    #     RAG_prompt_gen(embedding=model, result_file="./dataset/test_dataset_label_result.json",
    #                    index_dir="./apis/MXBAI/property_w_unit_index/", recall_k=i,
    #                    save_path=save_path)


    # model_name = 'Alibaba-NLP/gte-large-en-v1.5'
    # model_kwargs = {'device': 'cpu',"trust_remote_code":True}
    # encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    # model = HuggingFaceBgeEmbeddings(
    #     model_name=model_name,
    #     model_kwargs=model_kwargs,
    #     encode_kwargs=encode_kwargs,
    #     query_instruction="为这个句子生成表示以用于检索相关文章："
    # )
    #
    # for i in [5,10,15,20]:
    #     recall_k = i
    #     save_path = "./prompt_data/recall_prompt/test_dataset/gte/gte_RAG_{}_whole.json".format(i)
    #     RAG_prompt_gen(embedding=model, result_file="./dataset/test_dataset_label_result.json",
    #                    index_dir="./apis/gte/property_w_unit_index/", recall_k=i,
    #                    save_path=save_path)
    #
    # model_name = "intfloat/e5-base-v2"
    # model_kwargs = {'device': 'cpu',"trust_remote_code":True}
    # encode_kwargs = {'normalize_embeddings': True}  # set True to compute cosine similarity
    # model = HuggingFaceBgeEmbeddings(
    #     model_name=model_name,
    #     model_kwargs=model_kwargs,
    #     encode_kwargs=encode_kwargs,
    #     query_instruction="为这个句子生成表示以用于检索相关文章："
    # )
    # db_create(embeddings=model, folder_path="./apis/property_w_unit/", save_path="./apis/e5/property_w_unit_index")

    # for i in [5,10,15,20]:
    #     recall_k = i
    #     save_path = "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_{}_whole.json".format(i)
    #     RAG_prompt_gen(embedding=model, result_file="./dataset/test_dataset_label_result.json",
    #                    index_dir="./apis/e5/property_w_unit_index/", recall_k=i,
    #                    save_path=save_path)

    # for i in [20]:
    #     recall_k = i
    #     save_path = "./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_{}_whole.json".format(i)
    #     RAG_prompt_gen(embedding=model, result_file="./dataset/val_dataset_label_result.json",
    #                    index_dir="./apis/e5/property_w_unit_index/", recall_k=i,
    #                    save_path=save_path)

    ### few-shot

    # for i in [1,3,5,7,9,11,13,15,17,19,21,23]:
    #     txt_file = "./prompt_data/fewshot_sample/{}-shot.txt".format(i)
    #     save_path = "./prompt_data/fewshot_prompt/test_dataset/{}_shot_prompt.json".format(i)
    #     few_shot_prompt_gen(i, original_file="./dataset/test_dataset_label_result.json", prompt_file=txt_file, save_path=save_path)
    #
    #     save_path = "./prompt_data/fewshot_prompt/val_dataset/{}_shot_prompt.json".format(i)
    #     few_shot_prompt_gen(i, original_file="./dataset/val_dataset_label_result.json", prompt_file=txt_file,
    #                     save_path=save_path)



    ### self-debug with human feedback
    # few_shot_prompt_gen("", original_file="./dataset/test_dataset_label_result.json", prompt_file="./prompt_data/self-debug/5-shot-feedback.txt",
    #                     save_path="./prompt_data/self-debug/test_selfdebug_prompt.json")
    #
    # few_shot_prompt_gen("", original_file="./dataset/val_dataset_label_result.json", prompt_file="./prompt_data/self-debug/5-shot-feedback.txt",
    #                     save_path="./prompt_data/self-debug/val_selfdebug_prompt.json")



    # n = 17
    # method_name = "few_shot/{}_shot".format(n)
    #
    #
    # model_name_list = ["gemini_pro","gpt35","code_qwen","deepseek_v2","deepseek_coder","qwen_plus"]
    # for model_name in model_name_list:
    #     result_dir = "./code_result/Test/{}/{}".format(model_name, method_name)
    #     code_file = "./code_generation/Test/{}/{}_code.json".format(model_name, method_name)
    #     create_directory("./prompt_data/refine/{}/{}".format(model_name,method_name))
    #     save_file = "./prompt_data/refine/{}/{}/refine_1.json".format(model_name, method_name)
    #     error_info_prompt(result_dir,
    #                       code_file,
    #                       save_file)
    #
    # method_name = "doc_prompt/e5_20".format(n)
    # for model_name in model_name_list:
    #     result_dir = "./code_result/Test/{}/{}".format(model_name, method_name)
    #     code_file = "./code_generation/Test/{}/{}_code.json".format(model_name, method_name)
    #     create_directory("./prompt_data/refine/{}/{}".format(model_name,method_name))
    #     save_file = "./prompt_data/refine/{}/{}/refine_1.json".format(model_name, method_name)
    #     error_info_prompt(result_dir,
    #                       code_file,
    #                       save_file)
    # pass



    #e5_20 17_shot
    # rag_file = "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_20_whole.json"
    # few_k = 17
    # embedding_name = "e5"
    # create_directory("./prompt_data/RAG_with_fewshot/e5")
    # save_path = "./prompt_data/RAG_with_fewshot/e5/e5_20_{}_shot.json".format(few_k)
    # RAG_with_few_shot(rag_file,few_k,save_path)

    # e5_15 17-shot
    # rag_file = "./prompt_data/recall_prompt/test_dataset/e5/e5_RAG_10_whole.json"
    # few_k = 21
    # embedding_name = "e5"
    # create_directory("./prompt_data/RAG_with_fewshot/{}".format(embedding_name))
    # doc_number = 20
    # save_path = "./prompt_data/RAG_with_fewshot/{}/{}_{}_{}_shot.json".format(embedding_name,embedding_name,doc_number,few_k)
    # RAG_with_few_shot(rag_file,few_k,save_path)

    #val data
    # rag_file = "./prompt_data/recall_prompt/val_dataset/e5/e5_RAG_15_whole.json"
    # few_k = 17
    # embedding_name = "e5"
    # create_directory("./prompt_data/RAG_with_fewshot/val/{}".format(embedding_name))
    # doc_number = 15
    # save_path = "./prompt_data/RAG_with_fewshot/val/{}/{}_{}_{}_shot.json".format(embedding_name,embedding_name,doc_number,few_k)
    # RAG_with_few_shot(rag_file,few_k,save_path)


    # model_name = "gemini_pro"
    # method_name = "RAG_few_shot/e5_20/21_shot"
    # result_dir = "./code_result/Test/{}/{}".format(model_name, method_name)
    # code_file = "./code_generation/Test/{}/{}_code.json".format(model_name, method_name)
    # create_directory("./prompt_data/refine/{}/{}".format(model_name,method_name))
    # save_file = "./prompt_data/refine/{}/{}/refine_1.json".format(model_name, method_name)
    # error_info_prompt(result_dir,
    #                       code_file,
    #                       save_file)



    # model_name = "gemini_pro"
    # method_name = "few_shot/13_shot"
    # result_dir = "./code_result/Test/{}/{}".format(model_name, method_name)
    # code_file = "./code_generation/Test/{}/{}_code.json".format(model_name, method_name)
    # create_directory("./prompt_data/refine/{}/{}".format(model_name,method_name))
    # save_file = "./prompt_data/refine/{}/{}/refine_1.json".format(model_name, method_name)
    # error_info_prompt(result_dir,code_file,save_file)

    # zero_shot_prompt_gen()

    # refine_prompt()
    # refine2_prompt()
    # refine3_prompt()
    gpt_only_refine_prompt(stage=1)
    # gpt_only_refine_prompt(stage=2)
    # gpt_only_refine_prompt(stage=3)

    # gemini_explore()


