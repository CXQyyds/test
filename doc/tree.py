from pyecharts.components import Table
from pyecharts.options import ComponentTitleOpts


table = Table()

headers = ["City name", "Area", "Population", "Annual Rainfall"]
rows = [
    ("Brisbane", 5905, 1857594, 1146.4),
    ("Adelaide", 1295, 1158259, 600.5),
    ("Darwin", 112, 120900, 1714.7),
]
table.add(headers, rows)
table.set_global_opts(
    title_opts=ComponentTitleOpts(title="Table-基本示例", subtitle="我是副标题支持换行哦")
)
table.render("table_base.html")

msgs = [(1,1,1),(2,2,2)]
aaa = list(msgs[1])
for i in msgs:
    msg = list(i)
    aaa.append(msg)

print(aaa)