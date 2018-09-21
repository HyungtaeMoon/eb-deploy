#!/usr/bin/env bash
git add -A
git add -f .secrets/

# eb deploy 실행
eb deploy --profile sub-baeminchan-django-eb --staged

# .secrets와 requirements를 staging area엑서 제거
git reset HEAD .secrets/ requirements.txt
git reset