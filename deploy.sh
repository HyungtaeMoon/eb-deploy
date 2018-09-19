#!/usr/bin/env bash
# requirements 만들기
pipenv lock --requirements > requirements.txt

git add -f .secrets/ requirements.txt

# eb deploy 실행
eb deploy --profile sub-baeminchan-django-eb --staged

# .secrets와 requirements를 staging area엑서 제거
git reset HEAD .secrets/ requirements.txt

# requirements.txt 삭제
rm requirements.txt