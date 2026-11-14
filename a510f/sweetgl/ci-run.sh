#!/bin/sh
# (a GitHub artifact upload timeout is not a build failure: push again)
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
errs = [l[:400] for l in lines if re.search(r'error:|ERROR:|^Error|Undefined symbols|undefined symbol|^FAILED|^ld: |^  "_|not found|No such file|Traceback|Assertion', l)]
def ann(title, body):
    body = body[-3000:].replace('%', '%25').replace('\r', '').replace('\n', '%0A')
    print('::error title=%s::%s' % (title, body))
for i in range(0, min(len(errs), 60), 12):
    ann('%s errors %d' % (name, i // 12 + 1), '\n'.join(errs[i:i + 12]))
ann('%s tail' % name, '\n'.join(l[:300] for l in lines[-25:]))
PY
fi
exit $rc
