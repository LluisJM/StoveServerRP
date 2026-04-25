from beet import DataPack, ResourcePack, Function, TextFile, ItemModifier
from generator.libs.debugger import debug

import json

def to_nbt(obj):
    return json.dumps(obj, ensure_ascii=False)

formatted_names: dict[str, str] = {
    "axe": "AxE",
    "gerrit": "gerrit",
    "lluis": "Lluís",
    "manatee": "miniti",
    "ondra": "ondra"
}

rarities: dict[str, int] = {
    "default": 1
}

collection_colors: dict[str, str] = {
    "default": "green",
    "evil": "red",
    "legacy": "light_purple",
    "roleplay": "blue"
}

def main(dp: DataPack, custom_model_data: dict[str, int]):
    debug(__name__, f"running module", True)

    for model in custom_model_data:
        if model.startswith("stove:item/plush/"):
            split = model.split("/")
            name = split[-2]
            variant = split[-1]

            formatted_name = formatted_names[name] if name in formatted_names else name.capitalize()
            rarity = rarities[variant] if variant in rarities else 2
            formatted_rarity = ""
            for i in range(rarity):
                formatted_rarity += "\u2605"
            for i in range(3 - rarity):
                formatted_rarity += "\u2606"

            def with_format(string: str, color: str = "gray", italic: bool = False) -> dict:
                return {
                    "text": string, 
                    "color": color, 
                    "italic": italic
                }
            lore = [
                with_format(f"Rarity: {formatted_rarity}"),
                with_format(f"{variant.capitalize()} Collection", collection_colors[variant], True)
            ]

            dp[model] = ItemModifier({
                "function": "minecraft:sequence",
                "functions": [
                    {
                        "function": "minecraft:set_name",
                        "name": {
                            "text": f"{formatted_name} Plushie", 
                            "color": collection_colors[variant]
                        },
                        "target": "item_name"
                    },
                    {
                        "function": "minecraft:set_lore",
                        "lore": lore,
                        "mode": "replace_all"
                    },
                    {
                        "function": "minecraft:set_custom_model_data",
                        "value": custom_model_data[model]
                    }
                ]
            })
            dp[model] = Function(f"""
                if entity @s[nbt={{SelectedItem:{{id:"minecraft:paper"}}}}]:
                    item modify entity @s weapon.mainhand {model}
                if entity @s[nbt={{SelectedItem:{{id:"minecraft:paper"}}}}]:
                    tellraw @s "Set model {model} successfully"
                if entity @s[nbt=!{{SelectedItem:{{id:"minecraft:paper"}}}}]:
                    tellraw @s "§cCould not set model {model}; not holding minecraft:paper"
            """)
            debug(__name__, f'created give function for {formatted_name} ({variant.capitalize()}) plush at "{model}"')