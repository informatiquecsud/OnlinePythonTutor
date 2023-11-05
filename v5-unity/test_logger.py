import os
import glob
import json
import bdb

from io import StringIO

from pg_logger import PGLogger

codedir = "example-code/python"

# list all txt files in codedir

codefiles = glob.glob(f"{codedir}/*.txt")

for path in codefiles[:1]:
    with open(path, "r") as f:
        code = f.read()

    out_s = StringIO()

    def json_finalizer(input_code, output_trace):
        ret = dict(code=input_code, trace=output_trace)
        json_output = json.dumps(ret, indent=None)
        out_s.write(json_output)

    cumulative_mode = True
    heap_primitives = False
    show_only_outputs = False
    finalizer_func = json_finalizer
    disable_security_checks = True
    allow_all_modules = True
    probe_exprs = []

    logger = PGLogger(
        cumulative_mode,
        heap_primitives,
        False,
        finalizer_func,
        disable_security_checks=True,
        allow_all_modules=allow_all_modules,
        probe_exprs=probe_exprs,
    )

    try:
        logger._runscript(code)
    except bdb.BdbQuit:
        pass
    finally:
        print(logger.finalize())
