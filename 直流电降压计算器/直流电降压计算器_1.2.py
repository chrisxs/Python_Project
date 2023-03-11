print("弱电工具箱：直流电导线降压计算器")
print("****注意：此工具仅作参考用途，计算精度存在约±+0.007的误差值，请按现场实际为准****")
print("来源主页：chrisxs.com")
while True:
    # 获取用户输入
    material = input("请输入导线的材质（铜输入：1，铝输入：2）：")
    # 添加材质输入的错误处理
    while material not in ['铜', '铝', '1', '2']:
        material = input("材质输入有误，请重新输入（铜输入：1，铝输入：2）：")

    try:
        area = float(input("请输入导线的截面面积（单位:平方毫米）："))
        length = float(input("请输入导线的长度（单位:米）："))
        input_voltage = float(input("请输入输入电压（单位:伏特）："))
        load_voltage = float(input("请输入负载电压（单位:伏特）："))
        load_current = float(input("请输入负载电流（单位:安培）："))
        temperature = float(input("请输入环境温度（单位:摄氏度）："))
    except ValueError:
        print("您输入的值不正确，请重新输入。")
        continue

    # 计算电阻和电压降
    resistance = 0
    if material == "铜" or material == "1":
        resistance = 0.01724 * (1 + 0.00393 * (temperature - 20))* 1.8593
    elif material == "铝" or material == "2":
        resistance = 0.0283 * (1 + 0.00403 * (temperature - 20))* 1.8593

    voltage_drop = resistance * load_current * length

    # 输出结果
    print("导线的直流电电压降压为：%.3f伏特" % voltage_drop)

    # 错误处理
    if voltage_drop / load_voltage > 0.1:
        print("电压降压严重，请注意！")

    # 询问用户是否继续运行程序
    run_again = input("是否要重新运行程序？（y/n）：")
    if run_again.lower() == "n":
        break
