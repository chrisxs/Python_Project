import sys
import math

def calc_resistivity(material, temperature):
    if material == 1:
        resistivity = 1.678 * 10**(-8) * (1 + 0.00393 * (temperature - 20))
    elif material == 2:
        resistivity = 2.82 * 10**(-8) * (1 + 0.0039 * (temperature - 20))
    else:
        raise ValueError('无效的线缆材质')
    return resistivity

def calc_voltage_drop(voltage, current, wire_area, length, material, temperature):
    resistivity = calc_resistivity(material, temperature)
    resistance = resistivity * length / wire_area
    voltage_drop = 2 * current * resistance
    return voltage_drop

try:
    voltage = float(input('请输入工作电压（伏特）：'))
    current = float(input('请输入负载电流（安培）：'))
    wire_area = float(input('请输入线芯截面积（平方毫米）：')) / 10**6
    length = float(input('请输入长度（米）：'))
    material = int(input('请输入线缆材质（1=铜，2=铝）：'))
    temperature = float(input('请输入工作温度（摄氏度）：'))
except ValueError:
    print('输入错误：请输入合法的数值')
    sys.exit()

try:
    voltage_drop = calc_voltage_drop(voltage, current, wire_area, length, material, temperature)
except ValueError as e:
    print('输入错误：', e)
    sys.exit()

print(f'直流电的电降压值为 {voltage_drop:.3f} 伏特')
