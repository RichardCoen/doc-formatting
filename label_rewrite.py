from tools import write_dict_to_json,read_json,create_directory
from  Prompt_Gen import prompt_generation

def label_result(file1 = "./label_data/atomic_label_result/DFM-137-cl-1.0.json",file2 = "./label_data/atomic_label_result/DFM-37-rsh-1.0.json",file3 = "./label_data/atomic_label_result/DFM-137-gwx-1.0.json",save_path="./label_data/label_result/atomic_label_result.json"):
    label_results_1 = read_json(file1)["data"]
    label_results_2 = read_json(file2)["data"]
    label_results_3 = read_json(file3)["data"]

    best_result = []
    for i in range(len(label_results_1)):
        print(label_results_1[i]["id"])
        result_scores = {
            "rewrite1_score": 0,
            "rewrite2_score": 0,
            "rewrite3_score": 0
        }
        for k in result_scores.keys():
            result_scores[k] = int(label_results_1[i][k])+int(label_results_2[i][k])+int(label_results_3[i][k])

        max_score_key,max_score = max(result_scores.items(), key=lambda item: item[1])

        best_rewrite = label_results_1[i]["user_input"]

        if max_score > 0:
            max_score_key = max_score_key[:8]
            best_rewrite = label_results_1[i][max_score_key]

        best_result.append({
            "id":label_results_1[i]["id"],
            "user_input":label_results_1[i]["user_input"],
            "rewrite1":label_results_1[i]["rewrite1"],
            "rewrite2": label_results_1[i]["rewrite2"],
            "rewrite3": label_results_1[i]["rewrite3"],
            "rewrite_scores":result_scores,
            "best_rewrite": best_rewrite
        })

    write_dict_to_json({"Description":"Best rewrite choose.","data_list":best_result},save_path)

def direct_prompt_generation(file_name,save_path="./prompt_data/direct_prompt/whole_direct.json"):
    data_list = read_json(file_name)["data_list"]
    results = []
    for data in data_list:
        prompt = prompt_generation(data["best_rewrite"])
        result = {"id": data["id"], "original_input": data["user_input"], "best_rewrite": data["best_rewrite"],
              "prompt": prompt}
        results.append(result)
    write_dict_to_json({"description": "whole data prompts, directly, with best rewrite input and prompts","data_list":results},save_path)

def direct_wp_prompts_generation(file_name,save_path="./prompt_data/direct_prompt/whole_direct_wp.json"):
    data_list = read_json(file_name)["data_list"]
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
[paragraph.getFirst()]: Gets the first paragraph in this collection. ItemNotFoundIf the collection is empty, an error is raised.
Example:
```javascript
const paragraph = context.document.getSelection().paragraphs.getFirst();
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
        prompt = prompt_generation(data["best_rewrite"],apis=apis)
        result = {"id": data["id"], "original_input": data["user_input"], "best_rewrite": data["best_rewrite"],
              "prompt": prompt}
        results.append(result)
    write_dict_to_json({"description": "whole data prompts, with best rewrite input and prompts, with position apis","data_list":results},save_path)



if __name__ == '__main__':
    pass
    # atomic data
    # atomic_prompts_generation()
    # label_result()

    # whole data
    # file1 = "./label_data/train_label_result/DFM-485-cl-1.0.json"
    # file2 = "./label_data/train_label_result/DFM-485-gwx-1.0.json"
    # file3 = "./label_data/train_label_result/DFM-485-rsh-1.0.json"
    # label_result(file1,file2,file3,"./label_data/label_result/train_label_result.json")

    # file_name = "./label_data/label_result/whole_label_result.json"
    # direct_prompt_generation(file_name)
    # direct_wp_prompts_generation(file_name)

    #whole data
    file1 = "./label_data/test_label_result/DFM-1289-cl-1.0.json"
    file2 = "./label_data/test_label_result/DFM-1289-gwx-1.0.json"
    file3 = "./label_data/test_label_result/DFM-1289-rsh-1.0.json"
    label_result(file1,file2,file3,"./label_data/label_result/test_label_result.json")