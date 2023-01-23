from dicts.drops import drop_dict

blue = 0
green = 0
gold = 0
red = 0

for key in drop_dict.keys():
    match drop_dict[key]["type"]:
        case "blue":
            blue += 1
        case "green":
            green += 1
        case "gold":
            gold += 1
        case "red":
            red += 1
