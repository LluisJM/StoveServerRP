from beet import Model, ResourcePack, NamespaceFileScope
from beet.core.utils import JsonDict
from beet.contrib.vanilla import Vanilla
from generator.libs.debugger import debug
from typing import ClassVar

class OldItemModel(Model):
    """Class representing an item model."""

    scope: ClassVar[NamespaceFileScope] = ("models/item",)
    extension: ClassVar[str] = ".json"


def create_flat_model(rp: ResourcePack, path: str) -> str:
    return create_child_model(rp, "item/generated")

def create_child_model(rp: ResourcePack, parent: str, path: str) -> str:
    if path in rp.item_models:
        raise ValueError(f"duplicated model; {path} already exists")

    rp[path] = Model(dict({
        "parent": parent, 
        "textures": {
            "layer0": path
        }
    }))
    debug(__name__, f"created item model {path}")
    return path

def give_custom_models(rp: ResourcePack, model: str, vanilla: Vanilla, models: list[str]):
    overrides: JsonDict = []
    if models.__len__() <= 0:
        raise ValueError("model list is empty")

    for i in range(models.__len__()):
        override = {
            "predicate": {
                "custom_model_data": i + 1
            },
            "model": models[i]
        }
        overrides.append(override)
    
    if not vanilla.assets.models.__contains__(model):
        raise ValueError(f'item model for "{model}" doesn\'t exist')

    new_model = vanilla.assets.models.get(model)
    new_model.data.setdefault("overrides", overrides)
    rp[model] = new_model
    debug(__name__, f"added model {model} with {models.__len__()} override(s)")