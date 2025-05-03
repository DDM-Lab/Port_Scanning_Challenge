#!/usr/bin/env python3
import json

new_flag = "picoCTF{N0ND3F4ULT_3NC0D1NG5_I5_FUN}"

metadata = {"flag": new_flag}

with open("/challenge/metadata.json", "w") as f:
    f.write(json.dumps(metadata))
