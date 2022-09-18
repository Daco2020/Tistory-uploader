# Tistory uploader

코드 에디터로 작성한 md 파일을 티스토리에 업로드합니다.<br>

<br>

## 설정
1. 레포지토리를 `clone` 받습니다.
2. 환경변수를 설정합니다.
  - ACCESS_TOKEN (필수 > 티스토리로 부터 발급)
  - BLOG_NAME (필수 > 본인의 티스토리 이름) 
  - DISCORD_WEBHOOK_URL (선택)

<br>

## 사용법
- 업로드하려는 글을 /targets 안에 .md 파일로 작성합니다.
- shell 에서 `make post` 명령어를 입력합니다.
- 글 공개여부와 카테고리를 선택합니다.

<br>

### 동작 확인방법

- 티스토리에 정상적으로 포스팅 되었는지 확인합니다.
- 작성한 md 파일이 `contents/` 경로로 이동했는지 확인합니다.

<br><br>

## 기타
- 디스코드 알림을 원한다면 `DISCORD_WEBHOOK_URL` 환경변수를 추가해주세요.
- `Makefile`을 수정하여 `git push` 혹은 다른 스크립트와 함께 사용할 수 있습니다.

<br><br>

## 티스토리 API 문서
- [Tistory API docs](https://tistory.github.io/document-tistory-apis/)
