# Tistory uploader

깃헙 Push와 티스토리 포스팅을 하나의 명령어로 해결하세요! <br>

<br><br>

## 사용법
- 레포지토리를 `clone` 받습니다.
- 본인의 레포지토리로 `origin` 을 변경합니다.
- 필수 환경변수를 세팅합니다.
- upload 폴더 안에 올리고 싶은 글을 md 파일로 작성합니다.
- shell 에서 `make run` 명령어를 입력합니다.
- 공개여부를 선택합니다.
- 카테고리를 선택합니다.

<br>

### 동작 확인방법

- 깃헙에 정상적으로 Push 되었는지 확인합니다.
- 티스토리에 정상적으로 포스팅 되었는지 확인합니다.
- 작성한 md 파일이 `contents/` 경로로 이동했는지 확인합니다.
- 디스코드로 알림 메시지가 왔는지 확인합니다.


<br><br>

## 환경변수 설정

- ACCESS_TOKEN (필수) 
- BLOG_NAME (필수) 
- DISCORD_WEBHOOK_URL (선택)

```
ACCESS_TOKEN 은 티스토리로 부터 발급받을 수 있습니다.
BLOG_NAME 은 본인의 티스토리 이름입니다.
```


<br><br>

## 참고
- [Tistory API docs](https://tistory.github.io/document-tistory-apis/)
