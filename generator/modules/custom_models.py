from beet import ResourcePack
from beet.contrib.vanilla import Vanilla
from generator.libs.debugger import debug
from generator.libs.custom_models import *

def create_plush_model(rp: ResourcePack, player: str, variant: str = "default") -> str:
    return create_child_model(rp, "stove:plush", f"stove:plush/{player}/{variant}")

def main(rp: ResourcePack, vanilla: Vanilla):
    debug(__name__, f"running module", True)

    plushes: list[str] = []
    for texture in rp.textures:
        if texture.startswith("stove:plush/"):
            split: list[str] = texture.split("/")
            plushes.append(create_plush_model(rp, split[-2], split[-1]))

    give_custom_models(rp, "minecraft:item/paper", vanilla, plushes)
