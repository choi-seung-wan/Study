# mkdir file -> 새로운 디렉토리 생성
# cd file -> file 디렉토리로 이동
# git init -> git 저장소 새로 생성 => 현재 디렉토리를 저장소로 변경
#
# git add file -> 인덱스(저장소에 커밋하기 전의 임시 저장소)에 파일 추가
# git commit -m "file" -> 파일 저장소에 기록
# git status -> 현재 파일 목록 확인
# git remote add origin https://github.com username/repositaryName -> 원격 저장소의 정보를 추가
# git push origin master -> 로컬 저장소의 변경 사항을 github 원격 저장소에 반영
#                           github id/pw 작성 시 github에 push 후 원격 저장소에 반영
#
# branch -> 동시에 여러 버전 관리를 할 수 있는 구조
# git branch
# * master branch
# -> 현재 브랜치 목록을 확인하여 브랜치가 master branch 것이고 작업 중 브랜치가 master branch로 설정
# git branch subdir1 -> 'subdir1'이란 브랜치 생성
# git checkout subdir1 -> 지점 이동
# git checkout -b subdir1 -> 지점 생성 및 이동
#
# git checkout master
# git merge subdir1
# git push origin master
# -> master로 지점 이동 후 subdir1 지점에서 만든 File 목록을 master에 추가
#
# git branch -d BRANCH -> BRANCH 브랜치 삭제
#
# git log -> 로컬 저장소의 commit history 탐색
# git grep "검색 단어" -> 저장소 파일 내용 검색
# git clone [url] -> 기존 원격 저장소를 로컬 저장소에 다운로드
# git remote -> 원격 저장소 조작 ( None = 이름 목록
#                                -v = 원격 저장소 목록
#                                add [name] [url] = 원격 저장소 추가
#                                rm [name] = 원격 저장소 제거)
# git reset -> 로컬 저장소 commit 취소
# git pull -> 원격 브랜치 변경 사항 캡처