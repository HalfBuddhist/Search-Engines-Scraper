from search_engines import Bing

engine = Bing()
results = engine.search("蚌埠市人民政府办公室关于印发蚌埠市食品安全事故应急预案的通知", pages=1)
links = results.links()

print(links)
print(results[0].get("title"))
print(results[0].get("text"))
