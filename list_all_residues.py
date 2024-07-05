from pymol import cmd

def get_residue_names(result, resn, type_):
    if not result.get("aa"):
        result["aa"] = set()

    if not result.get("het"):
        result["het"] = set()

    if type_ == "ATOM":
        result["aa"].add(resn)
    else:
        result["het"].add(resn)

namespace = {
    "result": {},
    "get_residue_names": get_residue_names
}

cmd.iterate("all", "get_residue_names(result, resn, type)", space=namespace)

print(namespace["result"])
