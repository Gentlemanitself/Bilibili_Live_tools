from bilibili_api import live
import xlwt
import pandas as pd


def export_excel(export):
    # 将字典列表转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ['uid', 'uname', 'medal_name',
             'level', 'guard_level']
    pf = pf[order]
    # 指定生成的Excel表格名称
    file_path = pd.ExcelWriter('34027fan.xlsx')
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False)
    # 保存表格
    file_path.save()


if __name__ == '__main__':
    rank = live.get_seven_rank(34027)
    # 将分析完成的列表导出为excel表格
    print(rank)
