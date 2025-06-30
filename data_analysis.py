from tools import read_json,write_dict_to_json
def average_dict(data_dict):
    result = {}
    for key ,value in data_dict.items():
        result[key] = sum(value)/len(value)
    sorted_dict = sorted(result.items(), key=lambda item: item[0])
    return sorted_dict

def acc_distribution(acc_result_file,original_file):
    acc_dict= read_json(acc_result_file)["acc_dict"]
    original_data_list = read_json(original_file)["data_list"]
    property_number_statistic = {}
    input_dif_statistic = {}
    for key, acc in acc_dict.items():
        index = int(key)
        # if index>484:
        #     break
        orig_data = original_data_list[index]
        prop_number = orig_data["property_number"]
        if prop_number in property_number_statistic.keys():
            property_number_statistic[prop_number].append(acc)
        else:
            property_number_statistic[prop_number]=[acc]
        difficulty = orig_data["difficulty"]
        if difficulty in input_dif_statistic.keys():
            input_dif_statistic[difficulty].append(acc)
        else:
            input_dif_statistic[difficulty]=[acc]

    # for key,value in property_number_statistic.items():
    #     print("{}:{}".format(key,len(value)))
    #
    # print("#"*20)
    # for key,value in input_dif_statistic.items():
    #     print("{}:{}".format(key,len(value)))

    property_number_statistic = average_dict(property_number_statistic)
    input_dif_statistic = average_dict(input_dif_statistic)

    result = {
        "property_number_statistic": property_number_statistic,
        "input_dif_statistic": input_dif_statistic,
    }


    print(result["property_number_statistic"])
    print("-"*20)
    print(result["input_dif_statistic"])



def input_length(data_file,key = "best_rewrite"):
    data_list = read_json(data_file)["data_list"]
    words = {}
    for data in data_list:
        length = len(data[key].split())
        length = (length//10+1)*10
        if length in words.keys():
            words[length]+=1
        else:
            words[length] =1
    return dict(sorted(words.items()))


def prop_number(data_file, key = "property_number"):
    data_list = read_json(data_file)["data_list"]
    prop_numbers = {}
    for data in data_list:
        prop = data[key]
        if prop in prop_numbers.keys():
            prop_numbers[prop] += 1
        else:
            prop_numbers[prop] = 1
    return dict(sorted(prop_numbers.items()))


def prop_difficulty(data_file, key="difficulty"):
    data_list = read_json(data_file)["data_list"]
    prop_numbers = {}
    for data in data_list:
        prop = data[key]
        if prop in prop_numbers.keys():
            prop_numbers[prop] += 1
        else:
            prop_numbers[prop] = 1
    difficulty =  dict(sorted(prop_numbers.items()))
    dif_dis = {
        "easy":0,
        "middle":0,
        "challenged":0,
        "hard":0
    }
    for key,value in difficulty.items():
        # if 1 < key <6:
        #     dif_dis["easy"]+=value
        # elif 6<= key <11:
        #     dif_dis["middle"] += value
        # elif 10<= key <16:
        #     dif_dis["challenged"] +=value
        # else:
        #     dif_dis["hard"] += value

        if 1 < key <6:
            dif_dis["easy"]+=value
        elif 6<= key <11:
            dif_dis["middle"] += value
        elif 11<= key <16:
            dif_dis["challenged"] +=value
        else:
            dif_dis["hard"] += value
    return dif_dis

def prop_distribution(data_file):
    data_list = read_json(data_file)["data_list"]
    prop_numbers = {}
    for data in data_list:
        para_list = data["paragraphs"].values()
        for para in para_list:
            prop_list = para["property_read"]
            for prop in prop_list:
                if prop in prop_numbers.keys():
                    prop_numbers[prop] += 1
                else:
                    prop_numbers[prop] = 1

    return dict(sorted(prop_numbers.items()))


def draw_difficulty_pie():
    import matplotlib.pyplot as plt
    # 数据
    labels = ['easy', 'middle', 'challenged', 'hard']
    sizes = [516, 929, 358, 108]
    colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff6666']  # 自定义颜色
    # 设置图片大小
    fig, ax = plt.subplots(figsize=(6, 4))  # 设置图片大小为8x8英寸
    # 创建饼图
    wedges, texts, autotexts = ax.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=140)
    # 添加图例
    ax.legend(wedges, labels, title="Levels", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    # 添加标题
    plt.title('Distribution of Difficulty Levels')
    # 保存图表到本地
    plt.savefig('../chart/analysis/difficulty_levels_distribution.png')
    # 显示图表
    # plt.show()

def draw_prop_bar():
    import matplotlib.pyplot as plt
    # 数据
    properties = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
    inputs = [137, 105, 455, 125, 357, 398, 43, 164, 36, 64, 27]
    # 设置图片大小
    plt.figure(figsize=(10, 6))
    # 创建条形图
    plt.bar(properties, inputs, color='#66b3ff')
    # 添加标签和标题
    plt.xlabel('Number of Property')
    plt.ylabel('Number of Input')
    plt.title('Distribution of Property Number')
    # 保存图表到本地
    plt.savefig('../chart/analysis/property_distribution.png')

    # 显示图表
    # plt.show()

def draw_input_bar():
    import matplotlib.pyplot as plt
    # 数据
    words = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 150]
    inputs = [8, 89, 209, 156, 180, 135, 65, 46, 38, 14, 6, 6, 3, 1]
    # 设置图片大小
    plt.figure(figsize=(12, 6))
    # 创建条形图
    plt.bar(words, inputs, width=10, align='edge', color='#66b3ff', edgecolor='black')
    # 设置x轴刻度
    plt.xticks(words)
    # 添加标签和标题
    plt.xlabel('Words of Input')
    plt.ylabel('Number of Input')
    plt.title('Distribution of Words of Input')
    # 保存图表到本地
    plt.savefig('../chart/analysis/words_input_distribution.png')
    # 显示图表
    plt.show()

def shot_number():
    import matplotlib.pyplot as plt

    # 数据
    few_shot = [1, 5, 9, 13, 17, 21]
    acc_gemini = [0.19, 0.4863, 0.6174, 0.6349, 0.7864, 0.7590]
    acc_codeqwen = [0.2023, 0.4913, 0.5173, 0.5348, 0.6151, 0.5158]
    exception_gemini = [0.6360, 0.3724, 0.2636, 0.2626, 0.0952, 0.1245]
    exception_codeqwen = [0.6245, 0.2678, 0.2448, 0.2395, 0.1339, 0.2416]
    wrong_gemini =[ 0.174,0.1413,0.1203,0.098,0.1184,0.1165]
    wrong_codeqwen = [0.1732,0.2409,0.2379,0.2257,0.2510 ,0.2426]

    # 创建图形和轴
    fig, ax1 = plt.subplots()

    # 绘制准确率曲线
    ax1.set_xlabel('Few-shot (n)')
    ax1.set_ylabel('Accuracy')
    ax1.plot(few_shot, acc_gemini, label='Gemini Accuracy', color='tab:blue')
    ax1.plot(few_shot, acc_codeqwen, label='Codeqwen Accuracy', color='tab:green')
    ax1.tick_params(axis='y')
    ax1.set_xticks(few_shot)
    ax1.set_ylim(0, 1)  # 统一y轴范围为0-1

    # 创建第二个y轴
    ax2 = ax1.twinx()
    ax2.set_ylabel('Error Rate')
    ax2.plot(few_shot, exception_gemini, label='Gemini Exception Coverage', color='tab:red', linestyle='dashed')
    ax2.plot(few_shot, exception_codeqwen, label='Codeqwen Exception Coverage', color='tab:orange', linestyle='dashed')
    ax2.tick_params(axis='y')
    ax2.set_ylim(0, 1)  # 统一y轴范围为0-1


    # 创建第3个y轴
    ax3 = ax1.twinx()
    ax3.set_ylabel('Error Rate')
    ax3.plot(few_shot, exception_gemini, label='Gemini Exception Coverage', color='tab:red', linestyle='dashed')
    ax3.plot(few_shot, exception_codeqwen, label='Codeqwen Exception Coverage', color='tab:orange', linestyle='dashed')
    ax3.tick_params(axis='y')
    ax3.set_ylim(0, 1)  # 统一y轴范围为0-1


    fig.legend(loc=(0.65,0.74),fontsize = 6)

    # 显示图形
    plt.title('Accuracy and Error Rate vs Shot Number')
    plt.savefig('../chart/analysis/shot_number.png')
    plt.show()


def prop_number_influence():

    import matplotlib.pyplot as plt
    # 数据
    prop_number = [1,2,3, 4,5, 6,7, 8,9,10,12 ]
    acc_codeqwen = [0.7681, 0.75, 0.7078, 0.6532, 0.6603, 0.6616, 0.6623, 0.5753, 0.5802, 0.3971, 0.5347]
    acc_gpt35 = [0.8696, 0.875, 0.8399, 0.8065, 0.8123, 0.8029, 0.8766, 0.7229, 0.6728, 0.7294, 0.6111]

    err_codeqwen = [0.029, 0.0962, 0.1145, 0.1774, 0.1508, 0.1574, 0.1818, 0.241, 0.2222, 0.4412, 0.3333]
    err_gpt35 = [0.0145, 0.0, 0.022, 0.0806, 0.0559, 0.0406, 0.0, 0.1205, 0.1667, 0.1176, 0.3333]

    # 创建图形和轴
    fig, ax1 = plt.subplots()
    # 绘制准确率曲线
    ax1.set_xlabel('Property Number (n)')
    ax1.set_ylabel('Accuracy')
    ax1.plot(prop_number,  acc_codeqwen, label='Codeqwen Accuracy Rate', color='tab:blue')
    ax1.plot(prop_number, acc_gpt35, label='GPT3.5 Accuracy Rate', color='tab:green')
    ax1.tick_params(axis='y')
    # 设置X轴刻度与few_shot数据对齐
    ax1.set_xticks(prop_number)
    ax1.set_ylim(0, 1)  # 统一y轴范围为0-1

    # 创建第二个y轴
    ax2 = ax1.twinx()
    ax2.set_ylabel('Error Rate')
    ax2.plot(prop_number, err_gpt35, label='GPT3.5 Error Rate', color='tab:red', linestyle='dashed')
    ax2.plot(prop_number, err_codeqwen, label='Codeqwen Error Rate', color='tab:orange', linestyle='dashed')
    ax2.tick_params(axis='y')
    ax2.set_ylim(0, 1)  # 统一y轴范围为0-1

    # 添加图例
    fig.tight_layout()  # 调整布局以防止重叠
    fig.legend(loc=(0.6,0.8),fontsize = 8)
    # fig.legend(loc='upper left', bbox_to_anchor=(0.5, 1.15), ncol=3)

    # 显示图形
    plt.title('Accuracy and Error Rate vs Property Number')
    plt.savefig('../chart/analysis/proper_number_influence.png', bbox_inches='tight')
    plt.show()


def para_distribution(data_file):
    data_list = read_json(data_file)["data_list"]
    para_numbers = {}
    for data in data_list:
        para_list = data["paragraphs"].keys()
        for para in para_list:
            if para in para_numbers.keys():
                para_numbers[para] += 1
            else:
                para_numbers[para] = 1

    return dict(sorted(para_numbers.items()))
if __name__ == '__main__':

    pass
    # acc_distribution("./acc/gemini_whole_theo_1_acc.json","./original_data/whole_data.json")
    # acc_distribution("./acc/qwen_plus_whole_theo_1_acc.json", "./original_data/whole_data.json")
    # acc_distribution("./acc/qwen_max_whole_theo_1_acc.json", "./original_data/whole_data.json")
    # acc_distribution("./acc/gemini_api_whole_BEG_RAG5_acc.json", "./original_data/whole_data.json")
    # acc_distribution("./acc/gemini_api_whole_BEG_RAG10_acc.json", "./original_data/whole_data.json")
    # acc_distribution("./acc/Val/gpt35/RAG_few_shot_refine3/e5_15/17_shot_acc.json", "./dataset/val_data.json")

    # print(input_length("./dataset/test_dataset_label_result.json"))
    # print(prop_number("./original_data/all_data.json"))
    # print(prop_difficulty("./original_data/all_data.json","difficulty"))
    d = prop_distribution("./original_data/all_data.json")
    # print(d)
    # sum_count = sum(list(d.values()))
    # for k,v in d.items():
    #     print(k,end=": ")
    #     print(round(v/sum_count,4)*100)

    # draw_pie()
    # draw_prop_bar()
    # draw_input_bar()
    # shot_number()
    # prop_number_influence()

    d = para_distribution("./original_data/all_data.json")
    sum_count = sum(list(d.values()))
    print(sum_count)
    for k,v in d.items():
        print(k,end=": ")
        print(round(v/sum_count,4)*100)
    print(d)

