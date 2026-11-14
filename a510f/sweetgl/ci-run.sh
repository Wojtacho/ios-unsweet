#!/bin/sh
# ci-run.sh NAME CMD...: run CMD, log to $RUNNER_TEMP/NAME.log; on failure
# post the error lines and the log's tail as GitHub annotations (the public
# API shows annotations, not job logs).
N=$1; shift
L=${RUNNER_TEMP:-/tmp}/$N.log
"$@" > "$L" 2>&1
rc=$?
tail -40 "$L"
if [ $rc -ne 0 ]; then
	python3 -I - "$L" "$N" <<'PY'
import re, sys
log, name = sys.argv[1], sys.argv[2]
lines = open(log, errors='replace').read().splitlines()
errs = [l for l in lines if re.search(r'error|ERROR|Error|undefined|FAILED|not found|No such', l)]
def ann(title, body):
    body = body[-3500:].replace('%', '%25').replace('\r', '').replace('\n', '%0A')
    print('::error title=%s::%s' % (title, body))
for i in range(0, min(len(errs), 60), 12):
    ann('%s errors %d' % (name, i // 12 + 1), '\n'.join(errs[i:i + 12]))
ann('%s tail' % name, '\n'.join(lines[-45:]))
PY
fi
exit $rc
